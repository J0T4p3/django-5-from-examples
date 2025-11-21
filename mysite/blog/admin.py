from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # The fields displayed on the class list
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    # The filter options at the right hand of the page
    list_filter = ['status', 'created', 'publish', 'author']
    # Searcheable fields
    search_fields = ['title', 'body']
    # Fields that use input data from other fields
    prepopulated_fields = {'slug': ('title', )}
    # Fields that use the id from a fk
    raw_id_fields = ['author']
    # Date to filter the showed data
    date_hierarchy = 'publish'
    # Default ordering
    ordering = ['status', 'publish']

    # Little counter on the filters indicating the total obj count
    show_facets = admin.ShowFacets.ALWAYS
