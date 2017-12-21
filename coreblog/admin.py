from django.contrib import admin
from .models import *

# Re gister your models here.

class UserMod(admin.ModelAdmin):
	list_display = ["Username","First_N"]
	list_display_links = ["Username"]
	search_fields = ['User', 'First_N', 'Last_N']

	 
	class Meta:
		model = User

class PostMod(admin.ModelAdmin):
	list_display = ["Title","Updated","Author"]
	list_display_links = ["Title"]
	search_fields = ['Title', 'Author', 'Category','Timestamp']
	filter_horizontal = ('Category',)
	 
	class Meta:
		model = Post
class CategoryMod(admin.ModelAdmin):
	list_display = ["Name",]
	list_display_links = ["Name"]
	search_fields = ['Name',]

	 
	class Meta:
		model = Category

admin.site.register(User, UserMod)
admin.site.register(Post, PostMod)
admin.site.register(Category, CategoryMod)