# AI & Data Engineering Portfolio - Master Blueprint

## 🎯 The Core Objective
**The Goal:** Build a high-performance, containerized "Hybrid" portfolio that highlights expertise as an established **Data & AI Engineer at BASF**. 
**The Narrative:** Focus on enterprise-scale data architecture, robust AI/Deep Learning model deployment, and measurable business impact. The site must guide visitors from "Professional Identity" to "Technical Proof" and "Continuous Growth."

## 🏗️ Technical Infrastructure ("Infrastructure-First" Approach)
* **Backend:** Django 5 (Python).
* **Frontend:** Tailwind CSS, DaisyUI (for rapid, accessible component design).
* **Database:** SQLite (current development) migrating to PostgreSQL (production).
* **Containerization:** Fully Dockerized using `docker-compose`.
    * `web` service: Django server (Port 8000) with volume mounts for hot-reloading.
    * `tailwind` service: Node.js watcher for real-time CSS compilation.
* **Asset Management:** Django static files for CSS/JS, and dynamic media serving for user-uploaded content (profile pictures, architecture diagrams, certificates).

## 🗺️ Site Architecture & Final Feature Requirements

### 1. The Homepage (`/`) - "The Executive Summary"
* **Hero Section:** * Strong identity statement focusing on enterprise AI and Data Engineering (e.g., "Data & AI Engineer @ BASF | Building scalable ML pipelines and enterprise intelligence").
  * Professional profile image and immediate calls-to-action (GitHub, LinkedIn, Resume PDF download).
* **Dynamic Skills Matrix:** * A highly visual grid grouping the tech stack (e.g., Data Engineering, Machine Learning, MLOps, Cloud Infrastructure). 
  * Sourced dynamically from the `resume.Skill` model.
* **Featured Case Studies (Projects):** * A visually distinct 3-column card grid highlighting top-tier projects.
  * Driven by `is_featured=True` in the `projects.Project` model.
* **Experience Snapshot:** * Clean, scannable timeline or list showing current and recent roles (focusing on BASF).

### 2. The Project Detail (`/projects/<slug>/`) - "The Technical Deep Dive"
* **Dynamic Routing:** SEO-friendly slug-based URLs.
* **Hero Header:** High-res architecture diagram or cover image, project date, role, and source code/live links.
* **The Narrative Flow:** Structured content sections: "The Problem -> The Architecture -> The Solution -> The Impact."
* **Hard Metrics Dashboard:** * A distinct UI element (like DaisyUI stats components) displaying quantified results (e.g., "Reduced pipeline latency by 40%", "Model F1-Score of 0.92"). 
  * Pulled from a dedicated `ProjectMetric` relational model.
* **Tech Stack Tags:** Clickable tags linking to all projects using a specific technology (e.g., filtering all projects that use "PyTorch" or "Databricks").

### 3. The Growth Timeline (`/resume/`) - "The Continuous Context"
* **Parallel Node Timeline:** A custom vertical UI component.
  * **Left Track (Outputs):** Professional roles, promotions, and major shipped projects.
  * **Right Track (Inputs):** Continuous learning, certifications, degrees, and masterclasses happening concurrently.
* **Downloadable Asset:** A clean button to download a static ATS-friendly PDF resume.

### 4. Admin & Backend Features (The "CMS")
* **Extensible Django Admin:** Fully configured admin panels using `TabularInline` to manage `ProjectMetrics`, `ProjectLinks`, and `Skills` directly from the parent `Project` or `Profile` pages.
* **No Hardcoding:** Absolutely all user-facing content (text, skills, images, metrics) must be manageable via the database. The templates should act strictly as presentation layers.

### 5. UI/UX & Non-Functional Requirements
* **Responsive Design:** Flawless degradation from large desktop displays (multi-column) to mobile devices (stacked single-column layouts).
* **Brute-Force Image Safety:** Template-level inline style fallbacks for specific uploaded media (like SVGs or varying dimension certs) to prevent container explosions or layout shifts.
* **Dark Mode:** Built-in DaisyUI theme toggling (or a strictly enforced elegant dark-themed default suited for developers).