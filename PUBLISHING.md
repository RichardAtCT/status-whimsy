# Publishing Instructions

## Prerequisites

1. Create accounts:
   - GitHub account (if you don't have one)
   - PyPI account: https://pypi.org/account/register/
   - TestPyPI account: https://test.pypi.org/account/register/

2. Generate API tokens:
   - PyPI: Account settings → API tokens → Add API token
   - TestPyPI: Account settings → API tokens → Add API token

## GitHub Setup

1. Create a new repository on GitHub:
   - Go to https://github.com/new
   - Name: `status-whimsy`
   - Description: "A lightweight library for generating whimsical status updates using Claude Haiku 3"
   - Public repository
   - Do NOT initialize with README, .gitignore, or license

2. Push your code:
   ```bash
   cd /Users/richardatkinson/projects/status_whimsy
   git init
   git add .
   git commit -m "Initial commit: status_whimsy library"
   git branch -M main
   git remote add origin https://github.com/richardatkinson/status-whimsy.git
   git push -u origin main
   ```

3. Add secrets to GitHub repository:
   - Go to Settings → Secrets and variables → Actions
   - Add new repository secret: `PYPI_API_TOKEN` (your PyPI token)
   - Add new repository secret: `TEST_PYPI_API_TOKEN` (your TestPyPI token)

## Local Testing

1. Install in development mode:
   ```bash
   pip install -e ".[dev]"
   ```

2. Run tests:
   ```bash
   pytest
   ```

3. Check code quality:
   ```bash
   black status_whimsy tests
   isort status_whimsy tests
   flake8 status_whimsy tests
   mypy status_whimsy
   ```

## Build and Test Upload

1. Install build tools:
   ```bash
   pip install build twine
   ```

2. Build the package:
   ```bash
   python -m build
   ```

3. Check the build:
   ```bash
   twine check dist/*
   ```

4. Upload to TestPyPI first:
   ```bash
   twine upload --repository testpypi dist/*
   ```

5. Test installation from TestPyPI:
   ```bash
   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ status-whimsy
   ```

## Final PyPI Upload

1. If TestPyPI works, upload to PyPI:
   ```bash
   twine upload dist/*
   ```

2. Test installation:
   ```bash
   pip install status-whimsy
   ```

## Creating a Release on GitHub

1. Go to your repository on GitHub
2. Click on "Releases" → "Create a new release"
3. Tag version: `v0.1.0`
4. Release title: `v0.1.0 - Initial Release`
5. Description: Copy from CHANGELOG.md
6. Publish release

This will automatically trigger the GitHub Action to publish to PyPI.

## Post-Release

1. Update version in:
   - `status_whimsy/__init__.py`
   - `pyproject.toml`
   - Add new section in `CHANGELOG.md`

2. Commit version bump:
   ```bash
   git add .
   git commit -m "Bump version to 0.2.0-dev"
   git push
   ```

## Maintenance

- Monitor issues on GitHub
- Keep dependencies updated
- Follow semantic versioning
- Update documentation as needed