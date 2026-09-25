# Markets & Mandates

An educational, turn-based nation simulation about markets, economic planning, and the institutions in between.

**[Read the design spec](https://ghostsysoutnull.github.io/markets-and-mandates/)** · **[Give feedback](https://github.com/ghostsysoutnull/markets-and-mandates/issues/new?template=design-feedback.md)**

The project is preparing development specifications. There is no playable game yet. Draft 0.4 adds researched requirements, OO TypeScript architecture, simulation/data contracts, phone interaction, saves, verification and a workflow across sessions. Phones only, delivery through a phone-browser web link, and modular TypeScript source are accepted. PWA installation and offline play remain separate proposals.

## Development documentation

Start with [Development specification](docs/development.md). It links [requirements](docs/requirements.md), [architecture](docs/architecture.md), [simulation](docs/simulation.md), [data/content](docs/data-content.md), [phone interface](docs/interface.md), [delivery](docs/delivery.md), [verification](docs/verification.md), [research](docs/development-research.md), and [session workflow](docs/workflow.md).

## Concept documentation

- [Session handover](HANDOVER.md) and [backlog](docs/backlog.md)
- [Overview](docs/index.md)
- [The game](docs/game.md)
- [The executive, lawmakers, and courts](docs/government.md)
- [Economic systems](docs/systems.md)
- [Interest rates and monetary choices](docs/interest-rates.md)
- [Corporations, banks, and other actors](docs/actors.md)
- [Regulation and enforcement](docs/regulation.md)
- [Trade and the international economy](docs/trade.md)
- [Worked examples](docs/scenarios.md)
- [Nations and history](docs/nations.md)
- [Learning through play](docs/learning.md)
- [Decisions and feedback](docs/decisions.md)
- [Sources](docs/sources.md)

## Design collaboration

Conclude each review handoff with concrete next-step options and explicitly mark the preferred option. Record accepted design changes in the spec; keep unselected alternatives and unresolved mechanics clearly identified.

For a new session, start with [AGENTS.md](AGENTS.md), [HANDOVER.md](HANDOVER.md), and the [backlog](docs/backlog.md). The user selected a fresh session to settle the first nation/year and continue focused baseline research. The interactive walkthrough was aborted. Preserve settled decisions; UK/2010 remains a recommendation, not a selection.

## Publishing

GitHub Pages builds the Markdown in `docs/` using Jekyll. The publishing source is the `main` branch, `/docs` folder. Changes pushed there publish automatically; check the repository's Actions tab and Settings → Pages for build status.

Content lives in Markdown; the shared layout is `docs/_layouts/default.html`, and styling is `docs/assets/style.css`. Navigation is defined in `docs/_config.yml`. Keep internal links compatible with the project's `/markets-and-mandates` base path.

The future game targets phones, with a normal TypeScript project containing multiple source files and object-oriented design. The previous single-file delivery constraint is superseded. Keep the documentation deployment intact when selecting the game's distribution pipeline.

See [GitHub's publishing documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
