from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.db import models

def arabic_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str


class Category(models.Model):
    title = models.CharField(max_length=1000,verbose_name='اسم المسلسل/البرنامج')
    content = models.TextField(null=True,blank=True,help_text='قم بادخال قصة المسلسل او معلومات البرنامج',verbose_name='وصف المسلسل/البرنامج')
    image = models.ImageField(upload_to='categories',help_text='قم برفع صوره من جهازك',verbose_name='صوره')
    slug = models.SlugField(null=True,blank=True,unique=True,allow_unicode=True,help_text='يجب تركه كما هو')
    post_update = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return f'/category/{self.slug}'


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(Category,self).save(*args, **kwargs)
    class Meta:
        verbose_name = ('مسلسل/برنامج جديد')
        verbose_name_plural = ('المسلسلات/البرامج')

class Post(models.Model):
    title = models.CharField(max_length=1000,verbose_name='عنوان الحلقه')
    content = models.TextField(null=True,blank=True,help_text='قم بادخال وصف للحلقه ',verbose_name='وصف الحلقه')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,help_text='قم باختيار المسلسل او البرنامج الذي تنتمي له الحلقه',blank=True,null=True,related_name='posts',verbose_name='مسلسل/برنامج')
    episode = models.IntegerField(default=1,help_text='قم بادخال رقم الحلقه',verbose_name='رقم الحلقه')
    image = models.ImageField(upload_to='posts',help_text='قم برفع صوره من جهازك',verbose_name='صوره')
    video = models.FileField(null=True,blank=True,help_text='يمكنك رفع فيديو الحلقه من جهازك ولكن يفضل وضع رابط تضمين ',verbose_name='رفع فيديو من جهازك')
    embed = models.URLField(null=True,blank=True,help_text='قم باضافة رابط التضمين الخاص بفيديو الحلقه',verbose_name='اضافة رابط تضمين لفيديو')
    slug = models.SlugField(null=True,blank=True,unique=True,allow_unicode=True,help_text='يجب تركه كما هو')
    post_update = models.DateTimeField(auto_now=True)
    post_date = models.DateTimeField(default=timezone.now,help_text='يفضل تركه كما هو ',verbose_name='تاريخ الحلقه')
    active = models.BooleanField(default=True,help_text='يفضل تركه مفعلا كما هو فعند الغاء التفعيل لن تظهر الحلقه في الموقع',verbose_name='تفعيل')
    views = models.IntegerField(default=0,help_text='يجب تركها كما هي لضمان دقة نتائج الموقع',verbose_name='المشاهدات')

    def get_absolute_url(self):
        return f'/detail/{self.slug}'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)
        super(Post,self).save(*args, **kwargs)



    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def FileURL(self):
        try:
            urll = self.video.url
        except:
            urll = ''
        return urll

    class Meta:
        ordering = ('-episode',)
        verbose_name = ('حلقه جديده')
        verbose_name_plural = ('الحلقات')



