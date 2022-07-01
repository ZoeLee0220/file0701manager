from django.db import models
fields = '__all__'
# Create your models here.
class papers(models.Model):
    # verbose_name属性定义汉字名称
    #关于文献的基础信息
    title = models.CharField(max_length=100, verbose_name='文献名称')
    TypeofPaper = models.TextField(verbose_name='文献类型')
    Space_ofPaper = models.TextField(verbose_name='研究邻域')
    basement_message = models.TextField(verbose_name='摘要')
    keyword = models.TextField(verbose_name='keyword')
    paper_link = models.TextField(verbose_name='DOI')
    Code_link = models.TextField(verbose_name='Github')
    publish_date = models.DateField(verbose_name='接收时间')


    # 外键，多对一关系，一定要加上on_delete属性
    # Accept文献的期刊信息
    publishing = models.ForeignKey(to='publishing', on_delete=models.CASCADE, verbose_name='期刊名称')

    # 作者信息
    author = models.ManyToManyField(to='author', verbose_name='作者')

    class Meta:
        verbose_name = '文献信息'
        verbose_name_plural = '文献信息'

    def __str__(self):
        return self.title + '--相关文献信息'


class publishing(models.Model):

    LEVEL_CHOICES = (
        (u'SCI', u'SCI'),
        (u'IE', u'IEEE'),
        (u'SCIE', u'SCI&IEEE'),
        (u'None',u'ALL NOT'),
    )

    name = models.CharField(max_length=100, verbose_name='期刊名称')
    IF_number = models.CharField(max_length=20, verbose_name='影响因子')
    SCIE_choice= models.CharField(max_length=20, choices=LEVEL_CHOICES)

    class Meta:
        verbose_name = '期刊信息'
        verbose_name_plural = '期刊信息'

    def __str__(self):
        return '社名：' + self.name


class author(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱',blank=True)


    class Meta:
      verbose_name = '作者基本情况'
      verbose_name_plural = '作者基本情况'

    def __str__(self):
        return '作者：' + self.name
class Topic(models.Model):
    objects: None = None
    text=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
class Entry(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name_plural='entries'

def __str__(self):
    if len(self.text)>50:
        return self.text[:50]+'...'
    else:
        return self.text
