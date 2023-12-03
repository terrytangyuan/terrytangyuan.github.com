# 1. Install Ruby

Run `brew upgrade ruby` to upgrade ruby on Mac M1/M2.

If you need to have ruby first in your PATH, run:
```
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
```

For compilers to find ruby you may need to set:
```
export LDFLAGS="-L/opt/homebrew/opt/ruby/lib"
export CPPFLAGS="-I/opt/homebrew/opt/ruby/include"
```

For pkg-config to find ruby you may need to set:
```
export PKG_CONFIG_PATH="/opt/homebrew/opt/ruby/lib/pkgconfig"
```

Run `gem install webrick` if seeing `require': cannot load such file -- webrick (LoadError)`.

If an old version of Ruby is used even though `which ruby` and `ruby -v` seem correct. Use the specific binary `/opt/homebrew/lib/ruby/gems/3.0.0/bin/jekyll s` instead.

# 2. Install Jekyll

Run `gem install jekyll; gem install jekyll-paginate` to install `jekyll` dependencies.
* Run `brew link --force openssl` if seeing `'openssl/ssl.h' file not found` when installing `jekyll`.

If `jekyll` cannot be found, try `gem install jekyll --user-install` and the binary should be available in `/Users/terrytangyuan/.gem/ruby/3.2.0/bin/jekyll`.

# 3. Start website locally

Run `jekyll s` to view in local host: http://127.0.0.1:4000/

# Additional Ruby issues

For additional issues with Ruby, e.g. Ruby might be too old, check out [this question](https://stackoverflow.com/questions/38194032/how-to-update-ruby-version-2-0-0-to-the-latest-version-in-mac-osx-yosemite).

Install `rvm` to manage Ruby versions if needed:
```
curl -sSL https://raw.githubusercontent.com/rvm/rvm/master/binscripts/rvm-installer | bash -s stable
rvm install ruby@latest
rvm list known

ruby -v
rvm use ruby-3.0.0 --default
```
