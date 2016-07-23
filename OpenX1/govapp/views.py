from django.shortcuts import render_to_response, render, get_object_or_404
from django.http.response import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from components.models import Category, SubCategory , CustomerIssue, GovTable, GovOfficialTable, BroadcastMessage, Suggestion
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from govapp.forms import BroadcastForm, AddOfficialForm, AddDeptHeadForm
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from datetime import date
import datetime
# Create your views here.
def user_is_staff(user):
  if User.objects.get(username = user).is_staff:
    return True
  else:
    return False
def user_gov_check(user):
   if GovTable.objects.get(username = user).is_superofficial:
       return True
   else:
       return False

def user_depthead_check(user):
   if GovTable.objects.get(username = user).is_deptHead:
       return True
   else:
       return False

def user_govofficial_check(user):      
   if not GovTable.objects.get(username = user).is_deptHead and not GovTable.objects.get(username = user).is_superofficial:
       return True
   else:
       return False

@login_required
@user_passes_test(user_is_staff)
def gov_feed_view(request):
  list_issues = CustomerIssue.objects.all().order_by('-issue_date')
  list_suggestions = Suggestion.objects.all().order_by('-suggestion_date')   
  hot_issues = CustomerIssue.objects.all().order_by('-issue_vote')[:6]
  top_ideas = Suggestion.objects.all().order_by('-suggestion_vote')[:6]

  users = User.objects.all()
  voted_issues_count=0
  voted_suggestions_count = 0
  for user in users:
    if not user.is_staff and not user.is_superuser:
      voted_issues_count += user.voted_issues.all().count()
      voted_suggestions_count +=  user.voted_suggestions.all().count()
  
  context = {'list_issues':list_issues, 
         'list_suggestions':list_suggestions,
         'hot_issues':hot_issues,
         'top_ideas':top_ideas,
       
       }
  return render(request, 'govapp/gov_feed.html', context)

@login_required
@user_passes_test(user_gov_check)
def gov_super_view(request):
    try:
    	broadcast = BroadcastMessage.objects.all().order_by('-broadcast_date')[0]
    	broadcast_msg = broadcast.broadcast_msg
    except IndexError:
	    broadcast_msg = ''
    total_issues_count = CustomerIssue.objects.all().count()
    issues = GovTable.objects.filter(issues_resolved__gt = 0)
    resolved_issues = 0
    for issue in issues:
      resolved_issues += issue.issues_resolved
    unresolved_issues = total_issues_count - resolved_issues 
    hot_issues = CustomerIssue.objects.all().order_by('-issue_vote')[:6]
    context = {'total_issues_count' : total_issues_count, 
          'resolved_issues' : resolved_issues,
          'unresolved_issues' : unresolved_issues,
          'hot_issues' : hot_issues,
          'broadcast_msg' : broadcast_msg
    }
    return render(request, 'govapp/gov_home.html',context)

@login_required
@user_passes_test(user_gov_check)
def addDeptHead_view(request):
  if request.method == "POST":
     form = AddDeptHeadForm(request.POST)
     if form.is_valid():
       email = form.cleaned_data['email']
       depthead_category = form.cleaned_data['depthead_category']
       try:
           user = User.objects.get(email = email)
           try:
             deptHead = GovTable.objects.get(username=user)
             messages.success(request, 'Official already exists')
           except ObjectDoesNotExist:
             user.is_staff = True
             user.save()
             GovTable.objects.create(username = user, 
               is_superofficial = False, 
               is_deptHead = True, 
               category = Category.objects.get(category_name = depthead_category),
               subcategory = SubCategory.objects.get(pk = 1)
             )
             messages.success(request, 'Deptartment Head added') 
       except ObjectDoesNotExist:
           messages.success(request, 'User does not exist')
           return HttpResponseRedirect('/gov/add-head')

       return HttpResponseRedirect('/gov/add-head')
     
  else:
    hot_issues = CustomerIssue.objects.all().order_by('-issue_vote')[:6]
    args ={}
    args.update(csrf(request))   
    args['form'] = AddDeptHeadForm()
    args['hot_issues'] = hot_issues
    return render(request, 'govapp/add-depthead.html',args)

@login_required
@user_passes_test(user_gov_check)
def resourceList_view(request):
  heads = GovTable.objects.filter(is_deptHead = True)
  head_list = {}
  head_table = []
  for head in heads:
    user = User.objects.get(username = head.username)
    head_list["username"] = User.objects.get(username = head.username)
    head_list["email"] = user.email
    head_list["category"] = head.category
    head_list["issues_handling"] = head.issues_assigned
    head_list["issues_resolved"] = head.issues_resolved
    head_table.append(head_list)
    head_list = {}
  print head_table
  for head in head_table:
    print head.issues_handling
  official_list = GovTable.objects.filter(is_superofficial = False).filter(is_deptHead = False)
  hot_issues = CustomerIssue.objects.all().order_by('-issue_vote')[:6]
  context = {'hot_issues' : hot_issues,
          'head_table' : head_table,
          'official_list' : official_list
  }
  return render(request, 'govapp/allresources.html',context)


@login_required
@user_passes_test(user_depthead_check)
def deptHead_view(request):
    deptHead_category = Category.objects.get(category_name = GovTable.objects.get(username_id = request.user.id).category)
    deptHead_issue={}
    deptHead_table = []
    for subcategory in SubCategory.objects.filter(category = deptHead_category):
        sc_name = subcategory.subcategory_name
        issue_list = CustomerIssue.objects.filter(issue_subcategory = sc_name).order_by('-issue_date')
        for issue in issue_list:
            deptHead_issue["issue_id"] = issue.id
            deptHead_issue["issue_date"] = issue.issue_date
            deptHead_issue["issue_subcategory"] = issue.issue_subcategory
            deptHead_issue["issue_description"] = issue.issue_description
            deptHead_issue["is_assigned"] = issue.is_assigned
            deptHead_issue["is_seen"] = issue.is_seen
            deptHead_issue["is_resolved"] = issue.is_resolved
            deptHead_issue["issue_location"] = issue.issue_location
            deptHead_table.append(deptHead_issue)
            deptHead_issue = {}
        
    govOfficials = GovTable.objects.filter(category = GovTable.objects.get(username_id = request.user.id).category).filter(is_superofficial = False).filter(is_deptHead = False)
    
    context = {'deptHead_table': deptHead_table,'govOfficials':govOfficials }
    return render(request,'govapp/depthead.html',context)

@login_required
@user_passes_test(user_depthead_check)
def assignIssue_view(request, issue):
   govofficial = request.POST.get('govofficial')
   assigned_issue = CustomerIssue.objects.get(pk=issue)
   if assigned_issue.is_assigned:              #reassign issue
       prev_official = GovOfficialTable.objects.get(issue = assigned_issue)
       prev_official = GovTable.objects.get(id = prev_official.username_id)
       prev_official.issues_assigned -= 1
       prev_official.save()
       assign_to = GovTable.objects.get(username = User.objects.get(username=govofficial))
       assign_to.issues_assigned += 1
       assign_to.save()
       issue = GovOfficialTable.objects.get(issue=assigned_issue)
       issue.username_id = assign_to
       issue.save() 
   else:                               #Assign issue
       assign = GovOfficialTable(username=GovTable.objects.get(username = User.objects.get(username=govofficial)), issue = assigned_issue)
       assign.save()
       assigned_issue.is_assigned = True
       assigned_issue.save()
       official = GovTable.objects.get(username = User.objects.get(username=govofficial))
       official.issues_assigned += 1
       official.save()
   return HttpResponseRedirect('/gov/dept/')


@login_required
@user_passes_test(user_depthead_check) 
def addOfficial_view(request):
   if request.method == "POST":
     form = AddOfficialForm(request.user, request.POST)
     if form.is_valid():
       email = form.cleaned_data['email']
       official_subcategory = form.cleaned_data['official_subcategory']
       depthead = GovTable.objects.get(username = request.user)
       try:
           official = User.objects.get(email = email)
           try:
             govofficial = GovTable.objects.get(username=official)
             messages.success(request, 'Official already exists')
           except ObjectDoesNotExist:
             official.is_staff = True
             official.save()
             GovTable.objects.create(username = official, 
               is_superofficial = False, 
               is_deptHead = False, 
               category = Category.objects.get(category_name = depthead.category),
               subcategory = SubCategory.objects.get(subcategory_name = official_subcategory)
             )
             messages.success(request, 'Official added') 
       except ObjectDoesNotExist:
           messages.success(request, 'User does not exist')
           return HttpResponseRedirect('/gov/dept/add-official')

       return HttpResponseRedirect('/gov/dept/')
   
   else:
      
     args ={}
     args.update(csrf(request))   
     args['form'] = AddOfficialForm(request.user)
     return render(request, 'govapp/addofficial.html',args)

@login_required
@user_passes_test(user_depthead_check)
def dept_suggestions_view(request):
  suggestions = Suggestion.objects.filter(suggestion_category = GovTable.objects.get(username = request.user).category).order_by('-suggestion_date')
  context = {'suggestions':suggestions}
  return render(request, 'govapp/dept-suggestions.html', context)


@login_required
@user_passes_test(user_depthead_check)
def suggestionAccept_view(request,suggestion):
  
  suggestion = Suggestion.objects.get(id = suggestion)
  suggestion.is_accepted = True
  suggestion.save()
  return HttpResponseRedirect('/gov/dept/dept-suggestions')

@login_required
@user_passes_test(user_govofficial_check) 
def govOfficial_view(request):
    govofficial_issues = GovOfficialTable.objects.filter(username_id = GovTable.objects.get(username_id = request.user.id)).order_by('-assigned_date')
    customer_issues = []
    for issue in govofficial_issues:
        customer_issues.append(CustomerIssue.objects.get(pk = issue.issue_id))
    zip_list = zip(govofficial_issues,customer_issues)
    context = {'zip_list':zip_list}
    return render(request, 'govapp/govofficial.html',context)

@login_required
@user_passes_test(user_govofficial_check)    
def is_seen_view(request, issue):  
   issue = CustomerIssue.objects.get(pk=issue)
   issue.is_seen = True
   issue.save()
   return HttpResponseRedirect('/gov/official/')

@login_required  
@user_passes_test(user_govofficial_check)  
def is_resolved_view(request, issue):  
   issue = CustomerIssue.objects.get(pk=issue)
   issue.is_resolved = True
   issue.save()
   
   gov_issue = GovOfficialTable.objects.get(issue = issue)
   gov_issue.resolved_date = datetime.datetime.now()
   print datetime.datetime.now()
   gov_issue.save()

   govofficial = GovTable.objects.get(username = request.user)
   govofficial.issues_resolved += 1
   govofficial.save()
   return HttpResponseRedirect('/gov/official/')


def broadcastPage(request):
    if request.method == 'POST':
        form = BroadcastForm(request.POST)    
        if form.is_valid():
                send_msg = form.save(commit=False)
                broadcast_msg = request.POST.get('broadcast_msg')
                send_msg.broadcast_msg = broadcast_msg
                send_msg.save()
                messages.success(request,  broadcast_msg )
                return HttpResponseRedirect('/gov/')   
               
    else:
        form = BroadcastForm({'broadcast_msg':broadcast_msg})  
        context = {'form':form,'broadcast_msg' : broadcast_msg}
        return render(request,'govapp/gov_home.html',context)
      
@login_required
@user_passes_test(user_govofficial_check)
def flag_view(request):
   
   issue = get_object_or_404(GovOfficialTable, issue=request.POST.get('issue'))
   issue.flag = True
   issue.save()
  

   return HttpResponse()   

@login_required
@user_passes_test(user_govofficial_check)
def unflag_view(request):
   
   issue = get_object_or_404(GovOfficialTable, issue=request.POST.get('issue'))
   issue.flag = False
   issue.save()

   return HttpResponse()            