# Contributing to MailPicker (mpkr)

Thank you for your interest in contributing to MailPicker. The project is currently in **early development (Phase 0)** and is primarily a skeleton for the future C++ implementation. While functional contributions are not yet applicable, we welcome ideas, feedback, and preparatory contributions that do not alter the core skeleton.

---

## Current Status

* Project provides initial tooling, pre-commit hooks, and project structure.
* No functional features are implemented yet.

**Do not submit pull requests for usage features at this stage.** Focus on documentation, architecture suggestions, or preparatory work that supports the skeleton.

---

## How to Contribute (Future Phases)

Once development progresses, contributions will be organized around the following areas:

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

Be descriptive, include examples where applicable, and label your issue appropriately.

---

## Code Style and Guidelines

* Follow **C++20 standards**.  
* Adhere to `.clang-format` and `.clang-tidy` rules.  
* Include minimal MIT license headers in all new code.  
* Respect the modular structure; avoid unnecessary coupling between components.

---

## License

By contributing, you agree that your contributions will be licensed under the **MIT License**. See `LICENSE` for details.

---

## Notes

* This project is **under active development**.  
* Contributions may be reorganized as the architecture evolves.  
* Contributions beyond Phase 0 are welcome once functionality begins.
