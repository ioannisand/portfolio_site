from django.db import models


class Profile(models.Model):
    # Singleton-like behavior: We generally only want one profile
    name = models.CharField(max_length=100, default="Your Name")
    title = models.CharField(max_length=100, help_text="e.g. Full-Stack AI Engineer")
    bio = models.TextField()
    profile_image = models.ImageField(upload_to="profile/", blank=True, null=True)

    # Social Links
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    contact_email = models.EmailField(blank=True)

    # Resume Download
    resume_file = models.FileField(upload_to="documents/", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Personal Profile"