from django.contrib import admin

from  custom_commands.models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =(
        "name",
        "slug",
    )



@admin.register(UserAccount)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "is_staff",
        "email",
        "is_active",

    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display= (
        #"author",
        "title",
        "published",
        "date",
    )
   
    list_editable = ("published", )
    search_fields = ("title",)
    list_filter = ("published",)
    #autocomplete_fields = ("author",)