# Personal Website - ML Researcher Portfolio + Blog

A personal academic website built with [Quartz](https://quartz.jzhao.xyz/), featuring:

- Publications and projects portfolio
- Blog with Obsidian support (wiki-links, backlinks, callouts)
- Tufte-inspired typography
- Dark mode
- Graph view showing connections between notes
- GitHub Pages deployment

## Quick Start

### 1. Customize Your Information

Edit these files to add your content:

- `quartz.config.ts` - Site title, base URL, analytics
- `quartz.layout.ts` - Footer links (GitHub, Scholar, Twitter)
- `content/index.md` - Homepage
- `content/about.md` - About/CV page
- `content/publications/index.md` - Publications list
- `content/projects/index.md` - Projects overview
- `content/blog/*.md` - Blog posts

### 2. Local Development

```bash
# Install dependencies
npm install

# Start development server with hot reload
npx quartz build --serve

# View at http://localhost:8080
```

### 3. Deploy to GitHub Pages

1. Create a new GitHub repository
2. Update `baseUrl` in `quartz.config.ts` to `yourusername.github.io`
3. Push your code:
   ```bash
   git remote set-url origin https://github.com/yourusername/yourusername.github.io.git
   git push -u origin main
   ```
4. In GitHub repo settings, enable Pages with "GitHub Actions" as source
5. Your site will deploy automatically on every push

## Content Structure

```
content/
├── index.md              # Homepage
├── about.md              # About/CV
├── publications/
│   └── index.md          # Publications list
├── projects/
│   ├── index.md          # Projects overview
│   └── *.md              # Individual projects
├── blog/
│   └── *.md              # Blog posts
└── static/
    ├── publications.bib  # BibTeX file
    └── cv.pdf            # Your CV (add this)
```

## Obsidian Integration

This site supports full Obsidian syntax:

- **Wiki-links**: `[[page-name]]` or `[[folder/page|Display Text]]`
- **Backlinks**: Automatically shown in the right sidebar
- **Callouts**: `> [!note]`, `> [!warning]`, `> [!tip]`
- **Transclusions**: `![[other-note]]`
- **Tags**: `#tag-name`
- **Math**: `$inline$` and `$$block$$`

To edit content in Obsidian:
1. Open the `content/` folder as an Obsidian vault
2. Create/edit notes normally
3. Commit and push to deploy

## BibTeX to Markdown

Convert your publications BibTeX file to Markdown:

```bash
# Install dependency
pip install bibtexparser

# Generate publications page
python scripts/bib_to_markdown.py content/static/publications.bib

# Or write directly to file
python scripts/bib_to_markdown.py content/static/publications.bib --write
```

Edit `scripts/bib_to_markdown.py` to change:
- Author name highlighting (default: "Your Name")
- Google Scholar link
- Output format

## Customization

### Typography & Colors

Edit `quartz.config.ts` to change:
- Fonts (currently Libre Baskerville for Tufte style)
- Color scheme for light/dark modes

### Custom CSS

Add styles to `quartz/styles/custom.scss`

### Layout Components

Edit `quartz.layout.ts` to:
- Add/remove sidebar components
- Change header/footer content
- Customize page layouts

## Useful Commands

```bash
# Build site
npx quartz build

# Build with file watching
npx quartz build --serve

# Build showing bundle info
npx quartz build --bundleInfo
```

## Resources

- [Quartz Documentation](https://quartz.jzhao.xyz/)
- [Obsidian Help](https://help.obsidian.md/)
- [Tufte CSS](https://edwardtufte.github.io/tufte-css/)
