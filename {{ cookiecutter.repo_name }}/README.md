<!-- prettier-ignore-start -->
[![GitHub license](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/blob/main/LICENSE)
<!-- prettier-ignore-end -->

# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Requirements

- [mamba](https://github.com/mamba-org/mamba), which can be installed using conda or [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) (see [the official installation instructions](https://github.com/mamba-org/mamba#installation))
- [snakemake](https://snakemake.github.io), which can be installed using [conda or mamba](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html)

## Instructions

1. Create a conda environment:

```bash
snakemake -c1 create_environment
```

2. Activate it (if using conda, replace `mamba` for `conda`):

```bash
mamba activate {{cookiecutter.repo_name}}
```

3. Register the IPython kernel for Jupyter:

```bash
snakemake -c1 register_ipykernel
```

4. Create a git repository:

```bash
git init
```

5. Activate pre-commit for the git repository:

```bash
pre-commit install
pre-commit install --hook-type commit-msg
```

6. Create the first commit:

```bash
git add .
git commit -m "feat: initial commit"
```

7. Enjoy! :rocket:

_Optional_: if you are using GitHub, you can set up [pre-commit.ci](https://pre-commit.ci) as a continuous integration service for pre-commit.

## Acknowledgments

- Based on the [cookiecutter-data-snake :snake:](https://github.com/martibosch/cookiecutter-data-snake) template for reproducible data science.
