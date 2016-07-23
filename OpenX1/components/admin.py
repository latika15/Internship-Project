from django.contrib import admin
from .models import Category, SubCategory , CustomerIssue, GovTable, GovOfficialTable

# Register your models here.

    

class SubCategoryList(admin.TabularInline):
    model = SubCategory
    extra = 1

class CategoryList(admin.ModelAdmin):
    inlines = [SubCategoryList]
    
class IssueList(admin.ModelAdmin):
   list_display = ('issue_date', 'issue_description','issue_subcategory')

class GovList(admin.ModelAdmin):
    list_display = ('username', 'is_superofficial', 'is_deptHead', 'category', 'subcategory')    
    
admin.site.register(Category, CategoryList)
admin.site.register(CustomerIssue, IssueList)
admin.site.register(GovTable, GovList)
