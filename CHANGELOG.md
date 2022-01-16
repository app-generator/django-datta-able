# Change Log

## [1.0.4] 2022-01-16
### Improvements

- Bump Django Codebase to [v2stable.0.1](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
- Dependencies update (all packages) 
  - Django==4.0.1
- Settings update for Django 4.x
  - `New Parameter`: CSRF_TRUSTED_ORIGINS
    - [Origin header checking isn`t performed in older versions](https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-trusted-origins)  

## [1.0.3] 2021-11-07
### Improvements

- Bump Django Codebase to [v2.0.4](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
  - `assets` & `templates` moved to `apps` folder

## [1.0.2] 2021-09-09
### Improvements & Fixes

- Bump Django Codebase to [v2.0.2](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
  - Dependencies update (all packages)
    - Use Django==3.2.6 (latest stable version)
  - Better Code formatting
  - Improved Files organization
  - Optimize imports
  - Docker Scripts Update 
- Fixes: 
  - Patch 500 Error when authenticated users access `admin` path (no slash at the end)
  - Patch [#16](https://github.com/app-generator/boilerplate-code-django-dashboard/issues/16): Minor issue in Docker 

## [1.0.1] 2020-01-18
### Improvements

- Bump UI: [Jinja Datta Able](https://github.com/app-generator/jinja-datta-able/releases) v1.0.1
- UI: [Datta Able](https://github.com/codedthemes/datta-able-bootstrap-dashboard) 2021-01-01 snapshot
- Codebase: [Django Dashboard](https://github.com/app-generator/boilerplate-code-django-dashboard/releases) v1.0.4

## [1.0.0] 2020-02-07
### Initial Release
