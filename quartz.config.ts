import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "John Peter Flynn",
    pageTitleSuffix: " | ML Researcher",
    enableSPA: true,
    enablePopovers: true,
    analytics: { provider: "google", tagId: "G-RL5H9S52NF" },
    locale: "en-US",
    baseUrl: "johnpeterflynn.github.io",
    ignorePatterns: ["private", "templates", ".obsidian", "blog", "projects"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        // Headers: Libre Baskerville (serif), Body: Inter (sans-serif)
        header: "Libre Baskerville",
        body: "Inter",
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#fffff8",        // Tufte cream background
          lightgray: "#e0e0dc",
          gray: "#999999",
          darkgray: "#444444",
          dark: "#111111",
          secondary: "#a00000",    // Tufte red for links
          tertiary: "#666666",
          highlight: "rgba(160, 0, 0, 0.08)",
          textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#1a1a1a",
          lightgray: "#2d2d2d",
          gray: "#666666",
          darkgray: "#cccccc",
          dark: "#e8e8e8",
          secondary: "#ff6b6b",    // Softer red for dark mode
          tertiary: "#999999",
          highlight: "rgba(255, 107, 107, 0.12)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
