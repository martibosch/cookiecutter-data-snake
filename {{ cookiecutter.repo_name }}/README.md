[![GitHub license](https://img.shields.io/github/license/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/blob/master/LICENSE)

# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Instructions

1. Create a conda environment

```
make create_environment
```

2. Activate it

```
conda activate {{cookiecutter.repo_name}}
```

3. Register the IPython kernel for Jupyter

```
make register_ipykernel
```

## Acknowledgments

* Project based on [Henk Griffioen's version](https://github.com/hgrif/cookiecutter-ds-python) of the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science). #cookiecutterdatascience
