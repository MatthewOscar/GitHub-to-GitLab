# GitHub-to-GitLab

Sample project to practice setting up mirroring from GitHub to GitLab.

## Overview

This repository demonstrates how to mirror a GitHub repository to GitLab so that your GitLab copy stays in sync automatically whenever you push changes to GitHub.

There are two main approaches:

1. **GitLab Pull Mirroring** — GitLab periodically pulls from GitHub (GitLab Premium/Ultimate or self-managed with the feature enabled).
2. **GitHub Actions Push Mirroring** — A GitHub Actions workflow pushes to GitLab on every push (works on any plan).

---

## Option 1: GitLab Pull Mirroring

GitLab can be configured to automatically pull changes from a remote repository (like GitHub).

### Steps

1. Create an empty project on GitLab.
2. Go to **Settings → Repository → Mirroring repositories**.
3. Set **Git repository URL** to your GitHub repo URL, e.g.:
   ```
   https://github.com/<username>/<repo>.git
   ```
4. Set **Mirror direction** to **Pull**.
5. If the GitHub repository is private, provide a GitHub Personal Access Token as the password.
6. Click **Mirror repository**.

GitLab will now pull changes from GitHub on a schedule (roughly every 5 minutes).

---

## Option 2: GitHub Actions Push Mirroring

This repository includes a ready-to-use GitHub Actions workflow (`.github/workflows/mirror-to-gitlab.yml`) that mirrors every push to a GitLab repository.

### Prerequisites

- A GitLab repository (can be empty).
- A GitLab Personal Access Token with **write_repository** scope.

### Setup

1. **Fork or clone this repository** to your own GitHub account.

2. **Create a GitLab Personal Access Token**:
   - In GitLab, go to **User Settings → Access Tokens**.
   - Create a token with the `write_repository` scope.
   - Copy the token value.

3. **Add the token as a GitHub Secret**:
   - In your GitHub repository, go to **Settings → Secrets and variables → Actions**.
   - Click **New repository secret**.
   - Name: `GITLAB_TOKEN`
   - Value: your GitLab Personal Access Token.

4. **Set the GitLab repository URL secret**:
   - Add another secret named `GITLAB_REPO_URL` with the value:
     ```
     https://gitlab.com/<username>/<repo>.git
     ```

5. Push any change to the `main` branch — the workflow will automatically mirror the repository to GitLab.

---

## Repository Structure

```
GitHub-to-GitLab/
├── .github/
│   └── workflows/
│       └── mirror-to-gitlab.yml   # GitHub Actions mirroring workflow
├── src/
│   └── hello.py                   # Sample source file
├── tests/
│   └── test_hello.py              # Unit tests for sample source file
├── _config.yml                    # Jekyll configuration for GitHub Pages
├── index.md                       # Sample Jekyll homepage
├── CONTRIBUTING.md                # Contribution guidelines
├── LICENSE                        # MIT License
└── README.md                      # This file
```

## Running the Tests

```bash
python -m unittest discover tests/
```

---

## License

[MIT](LICENSE)
