# ensure-venv Ensure Virtualenv

This is a pre-commit-hook to check that you are inside the right virtualenv
Otherwise, you should not run the rest of the hooks.

## Testing

```shell
pipenv shell
python -m ensurevenv.main
exit
python -m ensurevenv.main
```


## Usage
```yaml
repos:
-   repo: https://github.com/hectorcanto/myhooks/ensurevenv
    rev: 0.1.0
    hooks:
      - id: ensurevenv
        entry: ensurevenv
```

TODO make repo public or use
