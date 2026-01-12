# Python actions playground

Repo for prototyping / testing github actions workflows for python projects.

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install ruff pytest
ruff check
ruff format --check
python3 -m pytest
```
