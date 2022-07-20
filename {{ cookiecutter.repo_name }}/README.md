[![GitHub license](https://img.shields.io/github/license/%7B%7Bcookiecutter.github_username%7D%7D/%7B%7Bcookiecutter.repo_name%7D%7D.svg)](https://github.com/%7B%7Bcookiecutter.github_username%7D%7D/%7B%7Bcookiecutter.repo_name%7D%7D/blob/master/LICENSE)

# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Requirements

- [mamba](https://github.com/mamba-org/mamba), which can be installed using conda or [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) (see [the official installation instructions](https://github.com/mamba-org/mamba#installation))
- [snakemake](https://snakemake.github.io), which can be installed using [conda or mamba](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html)

## Instructions

1. Create a conda environment:

```
snakemake -c1 create_environment
```

2. Activate it (if using conda, replace `mamba` for `conda`):

```
mamba activate {{cookiecutter.repo_name}}
```

3. Register the IPython kernel for Jupyter:

```
snakemake -c1 register_ipykernel
```

## Acknowledgments

- Project based on [Henk Griffioen's version](https://github.com/hgrif/cookiecutter-ds-python) of the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science). #cookiecutterdatascience
