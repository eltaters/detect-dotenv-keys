# detect-dotenv-keys
Pre-commit hook to check for sensitive keys in dotenv files.

## Installing the Hook
To install the hook on your project, set up [pre-commit](https://pre-commit.com/) and add the following 
to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/eltaters/detect-dotenv-keys
  rev: v0.1.1
  hooks:
    - id: detect-dotenv
```
