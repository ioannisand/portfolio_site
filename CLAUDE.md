# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run the development server
python manage.py runserver

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Run tests
python manage.py test

# Run tests for a single app
python manage.py test core
python manage.py test resume
python manage.py test projects

# Create a superuser (to access /admin)
python manage.py createsuperuser

# Tailwind CSS — must run in parallel with the dev server
python manage.py tailwind start    # dev (watches for changes)
python manage.py tailwind build    # production minified build
python manage.py tailwind install  # install npm deps (first time)
```

> **Note:** `NPM_BIN_PATH` in `settings.py` is currently set to `/usr/bin/npm`. On Windows this must point to the actual npm executable (e.g. `C:/Program Files/nodejs/npm.cmd`). Inside Docker the path is correct as-is.

## Docker

The preferred way to run the app is via Docker Compose, which handles both the Django dev server and the Tailwind CSS watcher as separate services sharing a bind-mounted volume.

```bash
# Build images and start all services (web + tailwind)
docker compose up --build

# Start without rebuilding
docker compose up

# Run a management command inside the running web container
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
docker compose exec web python manage.py test

# Stop all services
docker compose down
```

The site is available at `http://localhost:8000`.

### How Docker is structured

- **Single image** (`python:3.11-slim` + Node 20) is built from `Dockerfile` and reused by both services.
- **`web` service** — runs `python manage.py runserver 0.0.0.0:8000`, port 8000 exposed.
- **`tailwind` service** — runs `python manage.py tailwind start` (CSS watcher); no exposed port, writes compiled CSS into the shared volume so the `web` service picks it up immediately.
- The project directory is bind-mounted to `/app` in both containers, so code changes on the host are reflected instantly without rebuilding.

## Architecture

This is a **Django 6 personal portfolio site** with Tailwind CSS for styling.

### App structure

| App | Responsibility                                                                                          |
|---|---------------------------------------------------------------------------------------------------------|
| `config/` | Django project settings, rootp URLconf, WSGI/ASGI                                                       |
| `core/` | Homepage view; holds the `Profile` singleton model (name, bio, social links, resume file)               |
| `resume/` | `Skill`, `Experience`, `Education`, `Certificate` models (no views yet — data rendered on homepage)     |
| `projects/` | `Project`, `ProjectMetric`, `ProjectLink` models (no views yet — featured projects rendered on homepage) |
| `theme/` | django-tailwind app; compiled CSS output goes to `theme/static/css/dist/styles.css`                     |

### Data flow

All page data currently flows through a single view: `core/views.py:home`. It queries:
- `Profile.objects.first()` — the singleton profile
- `Project.objects.filter(is_featured=True)` — up to 3 featured projects
- `Skill.objects.filter(is_featured=True)` — tech stack icons
- `Experience`, `Education`, `Certificate` — resume data

### Templates

- `templates/base.html` — project-level base (takes precedence in template loading)
- `theme/templates/base.html` — theme-level base (fallback)
- `core/templates/core/home.html` — homepage, extends `base.html`

### Media files

Uploaded files (profile images, skill icons, certificates, project covers) are stored under `media/` and served via Django in DEBUG mode. `MEDIA_ROOT` maps to the project root `media/` directory.

### Key relationships

- `Project` → `Skill` (ManyToMany via `resume.Skill`)
- `Experience` → `Skill` (ManyToMany)
- `Certificate` → `Skill` (ManyToMany)
- `Skill.is_featured` controls which skills appear in the homepage tech stack matrix
- `Project.is_featured` controls which projects appear in the homepage hero section
