---
title: Configuration
---

# ⚙️ Configuration

[**`templates/configs/config.yml`**](https://github.com/{{cookiecutter.repo_owner}}/{{cookiecutter.repo_name}}/blob/main/templates/configs/config.yml):

```yaml
{{cookiecutter.module_name}}:
  min_length: 2
  max_length: 100
  min_value: 0.0
  max_value: 1.0
  threshold: 0.5
```

## 🌎 Environment Variables

[**`.env.example`**](https://github.com/{{cookiecutter.repo_owner}}/{{cookiecutter.repo_name}}/blob/main/.env.example):

```sh
# ENV=LOCAL
# DEBUG=false
# TZ=UTC
# PYTHONDONTWRITEBYTECODE=0
```
