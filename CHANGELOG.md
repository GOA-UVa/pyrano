# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

[//]: # "## [unreleased] - yyyy-mm-dd"

## [0.0.3] - 2025-10-29

### Added
- API key authentication between client and server (`X-API-Key` header) defined in `config.yml` and `serverconf.yml`.

## [0.0.2] - 2025-10-29

### Fixed
- When a file measurement contains a nan radiation value, it is ignored instead of failing to upload all the data.

## [0.0.1] - 2025-06-02

Initial version that serves as the baseline for tracking changes in the change log.


[unreleased]: https://github.com/goa-uva/pyrano/compare/v0.0.3...HEAD
[0.0.3]: https://github.com/goa-uva/pyrano/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/goa-uva/pyrano/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/goa-uva/pyrano/releases/tag/v0.0.1
