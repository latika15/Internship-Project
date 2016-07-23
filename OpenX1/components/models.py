from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import default
from PIL import Image
from django.core.files.storage import FileSystemStorage
from test.test_imageop import MAX_LEN

fs = FileSystemStorage(location='/media/images')

            
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.category_name
    
class SubCategory(models.Model):   
    subcategory_name = models.CharField(max_length=50)
    subcategory_description = models.TextField(max_length=400,default='')
    category = models.ForeignKey(Category)
    def __unicode__(self):
        return self.subcategory_name  
    
class CustomerIssue(models.Model):
    username = models.ForeignKey(User)
    issue_title = models.CharField(max_length=100, default='')
    issue_subcategory = models.CharField(max_length=50)
    issue_description = models.TextField(max_length=500)
    issue_date = models.DateTimeField(auto_now_add = True)
    issue_vote = models.IntegerField(default = '0')
    voters = models.ManyToManyField(User, related_name='voted_issues')
    is_assigned = models.BooleanField(default = False)
    is_seen = models.BooleanField(default = False)
    is_resolved = models.BooleanField(default = False )
    issue_img = models.ImageField(upload_to = 'images/', blank = True)
    issue_location = models.CharField(max_length = 50, default='')
    issue_followers = models.IntegerField(default = 0)
    def __unicode__(self):
        return self.issue_title
    
class Suggestion(models.Model):
    username = models.ForeignKey(User)    
    suggestion_title = models.CharField(max_length=100)
    suggestion_category = models.ForeignKey(Category)
    suggestion_description = models.TextField(max_length=500, help_text = 'This is required field')
    suggestion_date = models.DateTimeField(auto_now_add = True)
    suggestion_vote = models.IntegerField(default = '0')
    voters = models.ManyToManyField(User, related_name='voted_suggestions')
    is_accepted = models.BooleanField(default = False)
    def __unicode__(self):
        return self.suggestion_title


class GovTable(models.Model):
    username = models.ForeignKey(User)
    is_superofficial = models.BooleanField(default = False)
    is_deptHead = models.BooleanField(default = False )
    category = models.ForeignKey(Category)
    subcategory = models.ForeignKey(SubCategory)
    issues_assigned = models.IntegerField(default = '0')
    issues_resolved = models.IntegerField(default = '0')
    def __unicode__(self):
        return ''
    
    
class GovOfficialTable(models.Model):
    username = models.ForeignKey(GovTable)
    issue = models.ForeignKey(CustomerIssue)
    assigned_date = models.DateField(auto_now_add = True)
    resolved_date = models.DateField(auto_now = True)
    flag = models.BooleanField(default = False)
    def __unicode__(self):
        return ''
    
    
class BroadcastMessage(models.Model):
    broadcast_msg = models.CharField(max_length=1000, default= '')
    broadcast_date = models.DateTimeField(auto_now_add = True)
    def __unicode__(self):
        return self.broadcast_msg
    
    
class Follow(models.Model):
   username = models.ForeignKey(User, unique = True)  
   issue_following = models.ManyToManyField(CustomerIssue)
   def __unicode__(self):
       return self.username
    