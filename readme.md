AI Portfolio - Architecture & Technical Documentation
Status: Phase 2 (Homepage Content & Styling) Goal: A "Hybrid" portfolio for an Automation Engineer transitioning into AI/Deep Learning. Tech Stack: Django 5, Tailwind CSS, DaisyUI, Docker, PostgreSQL (future), SQLite (current).

1. Site Architecture (The Screens)
The application consists of three core public views designed to guide recruiters from "Identity" to "Proof of Competence."

A. The Homepage (/)
Purpose: The "Shop Window." Scannability is the priority.

Key Components:

Hero Section: Identity statement ("Automation Engineer transitioning to AI").

Skills Matrix: Grid of technologies (Python, Azure, RPA) linked to the Skill model.

Featured Projects: A curated list of top 3 projects (drawn from Project model with is_featured=True).

Experience Summary: The most recent 3 professional roles (drawn from Experience model).

Education & Certifications: A combined "Learning Journey" section showing formal education alongside self-taught certifications.

B. The Project Detail (/projects/<slug>/)
Purpose: Technical depth and "Case Studies."

Key Components:

Header: Large cover image and quick stats (Date, Role, Source Link).

The Narrative: "Problem -> Solution -> Architecture -> Challenges" structure.

Technical Tags: Dynamic links to the tools used (e.g., clicking "Python" shows all Python projects).

Metrics: Hard numbers (e.g., "Reduced manual entry by 40%") drawn from ProjectMetric model.

C. The Timeline / Resume (/resume/)
Purpose: Context and growth story.

Key Components:

Vertical Timeline: A visual line connecting distinct events.

Parallel Nodes: Displays "Output" (Jobs/Projects) on the left and "Input" (Learning/Certs) on the right to show continuous self-improvement.

2. Technical Infrastructure (Docker & Django)
This project uses an "Infrastructure First" approach, fully containerized for consistency.

Docker Setup
We use docker-compose to run two services in parallel:

web Service (Django):

Runs the Python server on port 8000.

Mounts the local directory to /app inside the container for hot-reloading.

Critical Config: Uses DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' in settings to avoid warnings.

Media Files: Configured to serve uploaded images (certs/profiles) from media/ during development.

tailwind Service (Node.js/Watcher):

Runs a separate process to compile Tailwind CSS in real-time.

Critical Fix: We enabled tty: true and stdin_open: true in docker-compose.yml to prevent this container from exiting immediately.

Configuration: The file theme/static_src/tailwind.config.js is manually configured to scan all app directories (core, resume, projects) for HTML files to generate classes.

Project Structure (File Tree)
Plaintext

ai_portfolio/
├── config/                  # Main Django settings & URL routing
│   ├── settings.py          # Configured for Tailwind & Media files
│   └── urls.py              # Includes logic to serve media in DEBUG mode
│
├── core/                    # The "Identity" App
│   ├── models.py            # Contains 'Profile' (Bio, Title, Image)
│   ├── views.py             # Renders the Homepage (aggregates data from all apps)
│   └── templates/core/      # Contains 'home.html' (The main layout)
│
├── resume/                  # The "History" App
│   ├── models.py            # Contains 'Experience', 'Education', 'Certificate', 'Skill'
│   └── admin.py             # Admin registration for these models
│
├── projects/                # The "Portfolio" App
│   ├── models.py            # Contains 'Project', 'ProjectMetric', 'ProjectLink'
│   └── admin.py             # Uses 'TabularInline' to edit metrics inside the Project page
│
├── templates/               # Global Templates
│   └── base.html            # Master layout (Navbar, Footer, CSS imports)
│
├── theme/                   # The Tailwind CSS App
│   └── static_src/          # Node.js source files for Tailwind
│
├── media/                   # User-uploaded content (Git-ignored)
│   ├── certificates/        # Certificate images
│   ├── skills/              # Tech stack logos
│   └── projects/            # Project screenshots
│
└── docker-compose.yml       # Orchestrates the Web and Tailwind services
Important "Hacks" & Fixes Applied
Image Sizing: We encountered issues with huge/exploding images (especially generic SVGs). We solved this using Brute Force Inline Styles in the template (e.g., style="width: 120px; height: 80px;") to override any CSS specificity issues.

Tailwind Watcher: If styles disappear, restart the tailwind container (docker-compose up). It needs to be running to see new classes.

Media Serving: We explicitly added static(settings.MEDIA_URL, ...) to config/urls.py so images appear during local development.