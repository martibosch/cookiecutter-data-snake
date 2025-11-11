<!-- prettier-ignore-start -->

\[!\[GitHub license\](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg)\](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/blob/main/LICENSE)

<!-- prettier-ignore-end -->

# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Requirements

The only requirement is to [install pixi](https://pixi.sh/latest/installation), then you can follow the steps described in the "Instructions" section below

## Instructions

1. Create a git repository:

```bash
git init
```

2. Activate pre-commit for the git repository:

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

3. Create the first commit:

```bash
git add .
git commit -m "feat: initial commit"
```

4. Enjoy! :rocket:

_Optional_: if you are using GitHub, you can set up [pre-commit.ci](https://pre-commit.ci) as a continuous integration service for pre-commit.

## Acknowledgments

- Based on the [cookiecutter-data-snake :snake:](https://github.com/martibosch/cookiecutter-data-snake) template for reproducible data science.
