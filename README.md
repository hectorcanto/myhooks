# myhooks

custom pre-commit hooks


## ensure-venv: Ensure Virtualenv

This is a pre-commit-hook to check that you are inside the right virtualenv
Otherwise, you should not run the rest of the hooks.

### Testing

```shell
pipenv shell
python -m hooks.ensure_venv
exit
python -m hooks.ensure_venv
```

### Usage
```yaml
repos:
-   repo: https://github.com/hectorcanto/myhooks
    rev: 0.1.0
    hooks:
      - id: ensure-venv
```
