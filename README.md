# MailPicker (mpkr)

*A modern IMAP email indexer and fuzzy-search tool, written in C++.*

## Project Status: Early Development (Phase 0)

MailPicker is currently in active early development.
At this stage, the repository contains only the foundational structure, tooling, and configuration required for long-term maintainability.

**No usable functionality is implemented yet.**

This phase focuses on establishing:

- Core project layout
- CMake modular structure
- Code style enforcement (clang-format, clang-tidy)
- Automated license headers
- Secret scanning
- Pre-commit workflow
- Initial documentation and planning

MailPicker is not yet ready for testing or installation.

## What MailPicker Will Become

When complete, MailPicker (`mpkr`) will be a cross-platform command-line tool that:

- Authenticates with Gmail and Outlook using OAuth2 + PKCE
- Connects to IMAP using secure XOAUTH2
- Indexes email metadata into a local SQLite database
- Provides fast search and filtering using fzf
- Runs fully offline after syncing
- Ships as packaged binaries for both Linux and Windows

The project is intentionally designed as a deep-dive into modern C++ and production-grade tooling.

## High-Level Roadmap

### Phase 0 — Foundations (Current)

- Set up repository structure
- Configure code-quality tools
- Add automated license header checks
- Establish pre-commit hooks
- Outline architecture and components

### Phase 1 — Core Skeleton & Modules

- Define modular CMake targets (Auth, IMAP, DB, Search, CLI)
- Integrate external dependencies (via vcpkg/Conan)

### Phase 2 — Authentication Layer

- OAuth2 Authorization Code + PKCE
- Local callback server for authorization code
- Token storage model

### Phase 3 — IMAP Indexing Pipeline

- Secure IMAP connection
- Email metadata extraction
- SQLite integration

### Phase 4 — Search Interface

- Pipe DB content into fzf
- Select/search email entries

### Phase 5 — Packaging

- Linux: Deb, RPM, AppImage
- Windows: MSI installer
- Versioning + release workflow

## License

MailPicker is released under the MIT License.
See `LICENSE` for details.

## Contributing

The project is not yet ready for contributions.
Once the architecture stabilizes in later phases, contribution guidelines will be provided.
