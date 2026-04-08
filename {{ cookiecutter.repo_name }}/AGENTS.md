# Agent guidance

## Running Python

This project uses [pixi](https://pixi.sh) for environment management. Always use `pixi run python` instead of `python` directly to ensure the correct environment is active.

## Jupyter notebooks

All notebooks use the `pixi-kernel-python3` kernel (`"display_name": "Python (Pixi)"`). This kernel invokes `pixi run python` automatically, so no separate environment activation is needed. Do not change the kernelspec to a named conda/venv kernel.
