from django.contrib import admin
from .models import Project, ProjectMetric, ProjectLink

class MetricInline(admin.TabularInline):
    model = ProjectMetric
    extra = 1  # Provides 1 empty row by default

class LinkInline(admin.TabularInline):
    model = ProjectLink
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'is_featured')
    search_fields = ('title', 'technologies')
    prepopulated_fields = {'slug': ('title',)}  # Auto-fills slug as you type title!
    inlines = [MetricInline, LinkInline]        # Adds the sub-tables inside Project