from django.db import models
from resume.models import Skill

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="URL friendly name (e.g. pneumonia-detection)")
    summary = models.CharField(max_length=255, help_text="Short tagline for the card view")
    description = models.TextField(help_text="Full case study. Markdown supported.")
    cover_image = models.ImageField(upload_to="projects/")

    # Tech Stack (Simple text for now, could be ManyToMany later)
    skills = models.ManyToManyField(Skill, related_name="projects", blank=True)
    date_created = models.DateField(auto_now_add=True)
    is_featured = models.BooleanField(default=False, help_text="Show on Homepage Hero?")

    def __str__(self):
        return self.title


class ProjectMetric(models.Model):
    """
    Stores specific model performance numbers.
    e.g. Metric: 'F1 Score', Value: '0.91'
    """
    project = models.ForeignKey(Project, related_name="metrics", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, help_text="e.g. Accuracy, F1-Score, Latency")
    value = models.CharField(max_length=50, help_text="e.g. 91%, 20ms, 0.85")

    def __str__(self):
        return f"{self.project.title} - {self.name}: {self.value}"


class ProjectLink(models.Model):
    """
    Stores related links (GitHub, Swagger, Live Demo, Paper)
    """
    LINK_TYPES = (
        ('github', 'GitHub Repo'),
        ('kaggle', 'Kaggle Notebook'),
        ('swagger', 'Swagger API'),
        ('demo', 'Live Demo'),
        ('paper', 'Research Paper'),
    )

    project = models.ForeignKey(Project, related_name="links", on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=LINK_TYPES)
    url = models.URLField()
    label = models.CharField(max_length=50, blank=True, help_text="Override button text (optional)")

    def __str__(self):
        return f"{self.project.title} - {self.type}"