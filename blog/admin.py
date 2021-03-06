# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db.models import TextField
from blog.models import Blog
from file_picker.wymeditor.widgets import WYMeditorWidget 

class BlogAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'time')
	formfield_overrides = { TextField: { 'widget': WYMeditorWidget({})}}
	class Media:
		js = ('http://cdn.jquerytools.org/1.2.5/full/jquery.tools.min.js',)
			

admin.site.register(Blog, BlogAdmin)