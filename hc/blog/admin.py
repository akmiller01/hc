from django.contrib import admin
from blog.models import Post
from blog.forms import PostForm
from adminfiles.admin import FilePickerAdmin

class PostAdmin(FilePickerAdmin):
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
    adminfiles_fields = ('content',)
    form = PostForm

admin.site.register(Post,PostAdmin)