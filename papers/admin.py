from django.contrib import admin

# Register your models here.
from . models import papers,publishing,author
from papers.models import Topic
admin.site.register(papers)
admin.site.register(publishing)
admin.site.register(author)

admin.site.register(Topic)
