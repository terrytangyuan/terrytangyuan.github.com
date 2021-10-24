Run `gem install jekyll; gem install jekyll-paginate` to install jekyll dependencies

Run `jekyll s` to view in local host: http://127.0.0.1:4000/

# Fix for issue with Ruby and Jekyll on Mac M1

Run `brew upgrade ruby` to upgrade ruby on Mac M1.

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
