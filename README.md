# Yuan Tang's Personal Website

A modern Jekyll-based personal website with secure dependencies and automated deployment.

[![Build and Deploy](https://github.com/terrytangyuan/terrytangyuan.github.io/actions/workflows/pages.yml/badge.svg)](https://github.com/terrytangyuan/terrytangyuan.github.io/actions/workflows/pages.yml)

## 🚀 Features

- **Modern Jekyll 4.x** with security updates
- **Automated CI/CD** with GitHub Actions
- **Modern build tools** with dependency auditing and vulnerability scanning
- **Modern build tools** replacing legacy Grunt with npm scripts
- **Responsive design** optimized for all devices
- **SEO optimized** with structured data and meta tags
- **Performance optimized** with compressed assets and modern web standards

## 🛠 Tech Stack

- **Site Generator**: Jekyll 4.3.4+
- **CSS Preprocessor**: Sass (migrated from LESS)
- **JavaScript**: ES2022 with ESLint for code quality
- **Build Tools**: npm scripts (replaced Grunt)
- **Deployment**: GitHub Actions + GitHub Pages

## 🏗 Development Setup

### Prerequisites

- Ruby 3.2+
- Node.js 18+
- Bundler and npm

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/terrytangyuan/terrytangyuan.github.io.git
   cd terrytangyuan.github.io
   ```

2. **Install dependencies**
   ```bash
   npm run install:deps
   ```

3. **Build assets and serve locally**
   ```bash
   npm run dev
   ```

The site will be available at `http://localhost:4000` with live reload enabled.

### Available Scripts

- `npm run build` - Build production assets
- `npm run watch` - Watch for changes and rebuild
- `npm run serve` - Serve Jekyll site locally
- `npm run dev` - Development mode with watching and serving
- `npm run test` - Run HTML validation and checks
- `npm run clean` - Clean build artifacts
- `npm run format` - Format code with Prettier
- `npm run lint` - Lint JavaScript with ESLint
- `npm run validate` - Full validation (build + test)

### Building for Production

```bash
npm run build
bundle exec jekyll build
```



## 📦 Dependencies

### Ruby Gems
- Jekyll 4.3.4+ (static site generator)
- GitHub Pages compatibility gems
- Security and performance plugins

### Node.js Packages
- Sass (CSS preprocessing)
- Terser (JavaScript minification)
- ESLint (code linting)
- Prettier (code formatting)

All dependencies are regularly updated and audited for security vulnerabilities.

## 🚀 Deployment

The site automatically deploys to GitHub Pages when changes are pushed to the `master` branch:

1. **Automated builds** via GitHub Actions
2. **HTML validation** and link checking
3. **Asset optimization** and compression

## 📝 Content Management

### Adding Blog Posts

Create new posts in the `_posts/` directory with the naming convention:
```
YYYY-MM-DD-title-of-post.markdown
```

### Updating Pages

Main pages are located in the root directory:
- `about.html` - About page
- `cv.html` - Curriculum Vitae
- `projects.html` - Projects showcase

### Images and Assets

- Place images in the `img/` directory
- Use the `data/` directory for data files and documents
- CSS and JavaScript are built from `less/` and `js/` directories

## 🔧 Configuration

Main configuration files:

- `_config.yml` - Jekyll configuration
- `Gemfile` - Ruby dependencies
- `package.json` - Node.js dependencies and scripts
- `eslint.config.js` - JavaScript linting rules
- `.prettierrc` - Code formatting rules

## 🧪 Testing

Run comprehensive tests:

```bash
npm run validate
```

This will:
- Build the site
- Validate HTML
- Check for broken links
- Test responsive design

## 📊 Performance

The site is optimized for performance:

- **Compressed CSS and JavaScript**
- **Optimized images**
- **Modern web standards**
- **Fast Jekyll build times**
- **CDN-friendly static assets**

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `npm run validate`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏆 Acknowledgments

- Built with [Jekyll](https://jekyllrb.com/)
- Hosted on [GitHub Pages](https://pages.github.com/)

---

**Note**: This website has been modernized with current dependencies and best practices. For legacy support or questions about the migration from the old Grunt-based setup, please refer to the git history or contact the maintainer.
