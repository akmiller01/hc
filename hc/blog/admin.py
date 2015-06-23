from django.contrib import admin
from blog.models import Post
from adminfiles.admin import FilePickerAdmin
from markitup.widgets import AdminMarkItUpWidget

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
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            kwargs['widget'] = AdminMarkItUpWidget()
        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Post,PostAdmin)