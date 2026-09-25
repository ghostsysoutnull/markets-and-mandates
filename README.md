# Markets & Mandates

An educational, turn-based nation simulation about markets, economic planning, and the institutions in between.

**[Read the design spec](https://ghostsysoutnull.github.io/markets-and-mandates/)** · **[Give feedback](https://github.com/ghostsysoutnull/markets-and-mandates/issues/new?template=design-feedback.md)**

The project is in concept development. There is no playable game yet. The documentation captures the initial discussion, identifies working proposals, and keeps open decisions visible.

## Documentation

- [Overview](docs/index.md)
- [The game](docs/game.md)
- [Economic systems](docs/systems.md)
- [Nations and history](docs/nations.md)
- [Learning through play](docs/learning.md)
- [Decisions and feedback](docs/decisions.md)
- [Sources](docs/sources.md)

## Publishing

GitHub Pages builds the Markdown in `docs/` using Jekyll. The publishing source is the `main` branch, `/docs` folder. Changes pushed there publish automatically; check the repository's Actions tab and Settings → Pages for build status.

Content lives in Markdown; the shared layout is `docs/_layouts/default.html`, and styling is `docs/assets/style.css`. Navigation is defined in `docs/_config.yml`. Keep internal links compatible with the project's `/markets-and-mandates` base path.

The future game's intended delivery is a mobile-friendly single HTML and JavaScript page. That is a later implementation constraint, not a requirement to design the simulation now.

See [GitHub's publishing documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
