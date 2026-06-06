from django.contrib import admin
from djblog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published', 'date')
    list_filter = ('published', 'date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'
    ordering = ('-date',)
    actions = ["publish"]

    @admin.action(description="Publish/Unpublish posts")
    def publish(self, request, queryset):
        for post in queryset:
            post.published = not post.published
            post.save()

admin.site.register(Post, PostAdmin)
# Register your models here.
