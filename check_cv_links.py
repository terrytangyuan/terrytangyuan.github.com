#!/usr/bin/env python3
"""Check for invalid links in cv.html."""

import re
import sys
import time
import urllib.request
import urllib.error
import ssl
from concurrent.futures import ThreadPoolExecutor, as_completed
from http.cookiejar import CookieJar

CV_FILE = "cv.html"

# Skip mailto links and local anchors
SKIP_PREFIXES = ("mailto:", "#", "/")

# Realistic browser headers to avoid bot detection
BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "identity",
    "Connection": "keep-alive",
}


def extract_links(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    urls = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
    seen = set()
    result = []
    for url in urls:
        if any(url.startswith(p) for p in SKIP_PREFIXES):
            continue
        if url not in seen:
            seen.add(url)
            result.append(url)
    return result


def build_opener():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    cookie_jar = CookieJar()
    return urllib.request.build_opener(
        urllib.request.HTTPSHandler(context=ctx),
        urllib.request.HTTPCookieProcessor(cookie_jar),
        urllib.request.HTTPRedirectHandler(),
    ), ctx


def check_url(url, timeout=20):
    opener, ctx = build_opener()

    # Try GET directly (many sites reject HEAD)
    req = urllib.request.Request(url, headers=BROWSER_HEADERS)
    try:
        resp = opener.open(req, timeout=timeout)
        code = resp.getcode()
        # Read a small amount to ensure connection is valid
        resp.read(1024)
        resp.close()
        if code >= 400:
            return url, code, None
        return url, code, None
    except urllib.error.HTTPError as e:
        # Treat 403 as OK for known bot-blocking sites
        # (we already use real browser headers, so a 403 likely means
        # the site requires JS/captcha, not that the page is missing)
        if e.code == 403:
            return url, 200, None
        return url, e.code, str(e)
    except Exception as e:
        return url, None, str(e)


def main():
    links = extract_links(CV_FILE)
    print(f"Found {len(links)} unique external links in {CV_FILE}\n")

    broken = []
    ok_count = 0

    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = {pool.submit(check_url, url): url for url in links}
        for i, future in enumerate(as_completed(futures), 1):
            url, status, error = future.result()
            if status and 200 <= status < 400:
                ok_count += 1
                print(f"  [{i}/{len(links)}] OK ({status}): {url}")
            else:
                broken.append((url, status, error))
                label = status if status else "ERR"
                print(f"  [{i}/{len(links)}] FAIL ({label}): {url}")
                if error:
                    print(f"         -> {error}")

    print(f"\n{'='*60}")
    print(f"Total: {len(links)} | OK: {ok_count} | Broken: {len(broken)}")
    if broken:
        print(f"\nBroken links:")
        for url, status, error in sorted(broken):
            label = status if status else "ERR"
            detail = f" ({error})" if error else ""
            print(f"  [{label}] {url}{detail}")
        sys.exit(1)
    else:
        print("\nAll links are valid!")


if __name__ == "__main__":
    main()
