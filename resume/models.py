from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = (
        ('language', 'Programming Language'),
        ('framework', 'Framework/Library'),
        ('tool', 'Tool/Platform'),  # Docker, Azure, Git
        ('concept', 'Concept'),  # Linear Algebra, CI/CD
    )

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    icon = models.ImageField(upload_to="skills/", blank=True, null=True, help_text="Small SVG or PNG logo")
    is_featured = models.BooleanField(default=False, help_text="Show in the 'About Me' tech stack matrix?")

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave empty for 'Present'")
    is_current = models.BooleanField(default=False)
    description = models.TextField(help_text="Markdown supported")

    # New: Link experience to skills used (e.g., Used Python at Company X)
    related_skills = models.ManyToManyField(Skill, blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.role} at {self.company}"


class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Certificate(models.Model):
    name = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    date_issued = models.DateField()
    url = models.URLField(blank=True)
    image = models.ImageField(upload_to="certificates/", blank=True, null=True)

    # New: Link certificate to a skill (e.g., Azure Cert -> Azure Skill)
    related_skills = models.ManyToManyField(Skill, blank=True)

    class Meta:
        ordering = ['-date_issued']

    def __str__(self):
        return self.name