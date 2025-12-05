# Contributing to MailPicker (mpkr)

Thank you for your interest in contributing to MailPicker. At this stage, the project is in **early development (Phase 0)** and not yet ready for functional contributions. However, we welcome ideas, feedback, and future participation once the architecture stabilizes.

---

## Current Status

* Project is a skeleton for later C++ implementation.
* Contains tooling, pre-commit hooks, and project structure.
* No functional features are implemented.

**Do not submit pull requests for usage features yet.** Contributions should focus on documentation, architecture suggestions, or preparatory work that does not affect the skeleton.

---

## How to Contribute (Future Phases)

Once development progresses, contributions will be organized around these areas:

### 1. Core Modules

* AuthManager
* IMAP Client
* DatabaseManager
* SearchInterface (fzf wrapper)
* ConfigManager

### 2. Security & Infrastructure

* OAuth2 PKCE implementation
* Secure token handling
* Pre-commit and CI enhancements
* Cross-platform build and packaging

### 3. Documentation

* Developer guides
* API documentation
* Architecture diagrams
* Tutorials

### 4. Testing

* Unit tests for modules
* Integration tests for IMAP and database
* CI/CD pipeline configuration

---

## Reporting Issues

Please use GitHub Issues for:

* Bug reports
* Feature requests
* Documentation improvements
* Security concerns

Be as descriptive as possible, include examples where applicable, and label your issue appropriately.

---

## Code Style and Guidelines

* Follow **C++20 standards**.
* Adhere to `.clang-format` and `.clang-tidy` rules.
* All new code should include minimal MIT license headers.
* Respect the modular structure; avoid coupling components unnecessarily.

---

## License

By contributing, you agree that your contributions will be licensed under the **MIT License**. See `LICENSE` for details.

---

## Notes

* This project is **under active development**.
* Contributions may be reorganized as the architecture matures.
* Contributions outside of Phase 0 are welcome once functionality begins.
