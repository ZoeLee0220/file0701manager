
from django.urls import re_path
from .import views
app_name='papers'
urlpatterns=[
#主页
re_path(r'^$',views.papermanagermentsys,name='papermanagermentsys'),
re_path(r'^papermanagermentsys$',views.papermanagermentsys,name='papermanagermentsys'),
re_path(r'^topics$',views.topics,name='topics'),
re_path(r'^new_topic/$',views.new_topic,name='new_topic'),
]