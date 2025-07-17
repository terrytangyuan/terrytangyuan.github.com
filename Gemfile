source "https://rubygems.org"

# Use GitHub Pages gem which includes Jekyll and compatible plugins
gem "github-pages", "~> 232", group: :jekyll_plugins

# Additional plugins not included in github-pages
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.17"
  gem "jekyll-sitemap", "~> 1.4"
  gem "jekyll-seo-tag", "~> 2.8"
end

# Security and performance gems
gem "sassc", "~> 2.4" # Faster Sass compilation
gem "image_optim", "~> 0.31" # Image optimization
gem "html-proofer", "~> 5.0" # HTML validation and link checking

# Development dependencies
group :development do
  gem "webrick", "~> 1.8" # Required for Ruby 3.x
  gem "wdm", "~> 0.1", platforms: [:mingw, :x64_mingw, :mswin] # Windows support
end

# Security
gem "tzinfo", "~> 2.0"
gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby]

# Performance
gem "liquid-c", "~> 4.0" # Faster Liquid processing 