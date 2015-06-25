from django.contrib import admin
from blog.models import Post
from blog.models import Tag

class PostAdmin(admin.ModelAdmin):
    #fields display on change list
    list_display = ['title','description']
    #fields to filter the change list with
    list_filter = ['published','created']
    #fields to search in change list
    search_fields = ['title','description','content']
    #enable the date drill down on change list
    date_hierarchy = 'created'
    #enable the save buttons on top of change form
    save_on_top = True
    #prepopulate the slug from the title
    prepopulated_fields = {"slug":("title",)}
    
class TagAdmin(admin.ModelAdmin):
    #enable the save buttons on top of change form
    save_on_top = True
    #prepopulate the slug from the title
    prepopulated_fields = {"slug":("name",)}

admin.site.register(Post,PostAdmin)

admin.site.register(Tag,TagAdmin)