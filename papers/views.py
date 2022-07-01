from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm
from .models import Topic,Entry
# Create your views here.
def hello(request):

    return HttpResponse("欢迎进入文献管理系统! ")

def papermanagermentsys(request):#主页
   #views_name = "文献管理系统"
  return  render(request,"papers/papermanagermentsys.html")#, {"name":views_name})
def topics(request):
    '''显示所有的主题'''
    topics=Topic.objects.order_by('date_added')
    context={'topics':topics}
    return render(request,'papers/topics.html',context)
def new_topic(request):
    '''添加新主题'''
    if request.method!='POST':
#未提交数据：创建给一个新表单
        form=TopicForm()
    else:
#POST提交的表单，对数据进行处理
        form=TopicForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('papers:topics'))
    context={'form':form}
    return render(request,'papers/new_topic.html',context)
