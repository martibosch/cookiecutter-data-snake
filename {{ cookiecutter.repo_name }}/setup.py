import setuptools

setuptools.setup(
    name='{{ cookiecutter.repo_name }}',
    packages=['{{ cookiecutter.python_module_name }}'],
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='GPL-3.0',
)
