from django.shortcuts import render_to_response, render, get_object_or_404
from django.http.response import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from components.models import Category, SubCategory , CustomerIssue, Suggestion , BroadcastMessage, Follow, GovOfficialTable, GovTable
from django.template import RequestContext
from customerapp.forms import ReportIssueForm, SuggestionForm 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def message():
    try:
    	broadcast = BroadcastMessage.objects.all().order_by('-broadcast_date')[0]
    	broadcast_msg = broadcast.broadcast_msg
    except:
	broadcast_msg = ''    
    return broadcast_msg

def user_citizen_check(user):
   if not user.is_superuser and not user.is_staff:
       return True
   else:
       return False
   
# Create your views here.  
@login_required
@user_passes_test(user_citizen_check) 
def feedPage(request):
    broadcast_msg = message()
    list_issues = CustomerIssue.objects.all().order_by('-issue_date')
    list_suggestions = Suggestion.objects.all().order_by('-suggestion_date')
    try:
        curr_user = Follow.objects.get(username_id = request.user.id)
        list_following = curr_user.issue_following.all()
    except ObjectDoesNotExist:
        list_following = {}    
    list_myissues = CustomerIssue.objects.filter(username=request.user)
    hot_issues = CustomerIssue.objects.all().order_by('-issue_vote')[:6]
    top_ideas = Suggestion.objects.all().order_by('-suggestion_vote')[:6]
    voted_issues = request.user.voted_issues.filter(id__in=[issue.id for issue in list_issues])   
    voted_suggestions = request.user.voted_suggestions.filter(id__in=[suggestion.id for suggestion in list_suggestions]) 
    context = {'list_issues':list_issues, 
           'list_suggestions':list_suggestions,
           'list_following':list_following,
           'voted_issues':voted_issues,
           'voted_suggestions':voted_suggestions,
           'list_myissues':list_myissues,
           'hot_issues':hot_issues,
           'top_ideas':top_ideas,
	       'broadcast_msg':broadcast_msg
   }
   
    return render(request,'index_cust.html', context)

@login_required 
@user_passes_test(user_citizen_check)
def customerHome(request):
    broadcast_msg = message()
    issue_category = Category.objects.all()
    special_categories = {}         #create a dictionay which stores 'category_name' and 'subcategory_name'
    all_categories = []             #list which stores all the names from category and subcategory 
    for issue in issue_category:
        tmp_list = []
        for i in SubCategory.objects.filter(category_id = issue):
            tmp_list.append(i.subcategory_name)
        special_categories["category_name"] = issue.category_name
        #special_categories["category_icon"]  = issue.category_icon.url
        special_categories["subcategory_name"] = tmp_list
        all_categories.append(special_categories)
        special_categories ={}
    hot_issues = CustomerIssue.objects.all().order_by('-issue_vote')[:6]
    top_ideas = Suggestion.objects.all().order_by('-suggestion_vote')[:6]
    context = {'all_cateogries': all_categories, 'broadcast_msg':broadcast_msg, 'hot_issues':hot_issues, 'top_ideas':top_ideas}
    return render(request,'customerapp/customer_home.html',context)


@login_required
@user_passes_test(user_citizen_check)
def subcategoryPage(request, subcategoryID):
    broadcast_msg = message()
    sc_list = []
    for subcat in SubCategory.objects.all():
        sc_list.append(subcat.subcategory_name)  
    list_issues = CustomerIssue.objects.filter(issue_subcategory=subcategoryID).order_by('-issue_date')
    try:
        curr_user = Follow.objects.get(id = request.user.id)
        list_following = curr_user.issue_following.all()
    except ObjectDoesNotExist:
        list_following = {}
    hot_issues = CustomerIssue.objects.filter(id__in=[issue.id for issue in list_issues]).order_by('-issue_vote')[:6]
    top_ideas = Suggestion.objects.all().order_by('-suggestion_vote')[:6]
    context = {'list_issues':list_issues,'subcategoryID' : subcategoryID, 
               'broadcast_msg':broadcast_msg,
               'list_following':list_following, 
               'hot_issues':hot_issues,
               'top_ideas':top_ideas
    }   
    if subcategoryID in sc_list:
        return render(request, 'customerapp/subcategoryPage.html',context)
    
    #else:
        #return render_to_response('error.html')

@login_required
@user_passes_test(user_citizen_check)
def reportIssuePage(request, subcategoryID):
    broadcast_msg = message()
    if request.method == 'POST':
        form = ReportIssueForm(request.POST , request.FILES)    
        if form.is_valid():
                report_issue = form.save(commit=False)
                report_issue.username = User.objects.get(username=request.user.username)
                issue_subcategory = form.cleaned_data['issue_subcategory']
                issue_description = form.cleaned_data['issue_description']
                report_issue.issue_img = request.FILES.get('issue_img')
                issue_location = request.POST.get('issue_location')
                report_issue.issue_location = issue_location
                print report_issue.issue_img
                report_issue.save()
                messages.success(request, 'Thank you for posting an issue.')
                link = '/customer/categories/%s/'
                return HttpResponseRedirect(link % subcategoryID)   
               
    else:
        form = ReportIssueForm({'issue_subcategory':subcategoryID}) 
        list_issues = CustomerIssue.objects.filter(issue_subcategory=subcategoryID).order_by('-issue_date')
        hot_issues = CustomerIssue.objects.filter(id__in=[issue.id for issue in list_issues]).order_by('-issue_vote')[:6] 
        top_ideas = Suggestion.objects.all().order_by('-suggestion_vote')[:6]
        context = {'form':form,'subcategoryID' : subcategoryID, 'broadcast_msg':broadcast_msg, 'hot_issues':hot_issues,'top_ideas':top_ideas}
        return render(request,'customerapp/report_issue.html',context)
    
    
@login_required 
@user_passes_test(user_citizen_check)   
def suggestionPage(request):
    broadcast_msg = message()
    form = SuggestionForm(request.POST or None)
    username = request.user.username
    print username
    if form.is_valid():
        username = User.objects.get(username=username)
        suggestion_title = form.cleaned_data['suggestion_title']
        suggestion_category = Category.objects.get(category_name = form.cleaned_data['suggestion_category'])
        suggestion_description = form.cleaned_data['suggestion_description']
        Suggestion.objects.create(
              username = username,
              suggestion_title = suggestion_title,
              suggestion_category = suggestion_category,
              suggestion_description = suggestion_description
          )
        messages.success(request, 'Thank you for posting an idea.')
        return HttpResponseRedirect('/customer/mysuggestions')
    else:
        form = SuggestionForm
        top_ideas = Suggestion.objects.all().order_by('-suggestion_vote')[:6]
        context = {'form': form, 'broadcast_msg':broadcast_msg,'top_ideas':top_ideas}
        return render(request,'customerapp/suggestionform.html',context)
    

@login_required
@user_passes_test(user_citizen_check)
def myprofilePage(request):
    broadcast_msg = message()
    user = User.objects.get(username=request.user.username)
    myissues = CustomerIssue.objects.filter(username=user).order_by('-issue_date')
    try:
        curr_user = Follow.objects.get(username_id = request.user.id)
        list_following = curr_user.issue_following.all()
    except ObjectDoesNotExist:
        list_following = {}
    hot_issues = CustomerIssue.objects.all().order_by('-issue_vote')[:6]  
    top_ideas = Suggestion.objects.all().order_by('-suggestion_vote')[:6]
    context = {'myissues': myissues, 'broadcast_msg':broadcast_msg, 'list_following':list_following, 'hot_issues':hot_issues,'top_ideas':top_ideas}
    return render(request, 'customerapp/myprofile.html',context)

@login_required
@user_passes_test(user_citizen_check)
def mysuggestionsPage(request):
    broadcast_msg = message()
    user = User.objects.get(username=request.user.username)   
    my_suggestions = Suggestion.objects.filter(username=user).values().order_by('-suggestion_date')
    top_ideas = Suggestion.objects.all().order_by('-suggestion_vote')[:6]
    context = {'mysuggestions': my_suggestions, 'broadcast_msg':broadcast_msg,'top_ideas':top_ideas}
    return render(request, 'customerapp/mysuggestions.html',context)

@login_required
@user_passes_test(user_citizen_check)
#def change_pwdPage(request):
    #return render(request, 'customerapp/change_pwd.html')

def notificationsPage(request):
    broadcast_msg = message()
    user = User.objects.get(username=request.user.username)
    customer_issues = CustomerIssue.objects.filter(username=user).order_by('-issue_date')
    gov_issues = GovOfficialTable.objects.filter(issue__in=[issue.id for issue in customer_issues])
    zip_list = zip(gov_issues,customer_issues)
    hot_issues = CustomerIssue.objects.all().order_by('-issue_vote')[:6]   
    top_ideas = Suggestion.objects.all().order_by('-suggestion_vote')[:6]
    context = {'broadcast_msg':broadcast_msg, 'zip_list':zip_list, 'hot_issues':hot_issues,'top_ideas':top_ideas}
    return render(request, 'customerapp/notifications.html', context)

@login_required
@user_passes_test(user_citizen_check)
def followPage(request, subcategoryID, issue):
   issue = CustomerIssue.objects.get(id=issue)
   #check if already following some issues 
   if Follow.objects.filter(username=request.user.id).count() > 0:         
       curr_user = Follow.objects.get(username_id = request.user.id)
       list_following = curr_user.issue_following.all()
       if issue not in list_following:
           print 'issue not following'
           curr_user.issue_following.add(issue)
           issue.issue_followers += 1
           curr_user.save()
           issue.save()
   else:
       #if this is users first following issue create new entry
       Follow.objects.create(username=request.user)                    
       curr_user = Follow.objects.get(username = request.user.id)
       curr_user.issue_following.add(issue)
       issue.issue_followers += 1
       curr_user.save()
       issue.save()
   #get list of issues which a particular user is following
   list_following = curr_user.issue_following.all()
   #context = {'issue':issue,'list_following':list_following} 
   return HttpResponseRedirect('/customer/feed')

def rate(request):
    if request.is_ajax():
        if request.method == 'GET':
            message = "fail"
        elif request.method == 'POST':
            user = request.POST.get('user')
            rating = request.POST.get('rating')
            this_id = request.POST.get('id')
            message = str(user) + " "+ str(rating) + " " +str(id)
    else:
        message = "No XHR"
    # do something
    return HttpResponse(message)


@login_required
@user_passes_test(user_citizen_check)
def vote(request):
   issue = get_object_or_404(CustomerIssue, id=request.POST.get('issue'))
   issue.issue_vote += 1
   issue.save()
   user = request.user
   user.voted_issues.add(issue)
   user.save()

   return HttpResponse()

@login_required
@user_passes_test(user_citizen_check)
def voteSuggestion(request):
   suggestion = get_object_or_404(Suggestion, id=request.POST.get('suggestion'))
   suggestion.suggestion_vote += 1
   suggestion.save()
   user = request.user
   user.voted_suggestions.add(suggestion)
   user.save()

   return HttpResponse()

@login_required
@user_passes_test(user_citizen_check)
def issuePage(request, issueId):
   issue = get_object_or_404(CustomerIssue, pk=issueId)
   hot_issues = CustomerIssue.objects.all().order_by('-issue_vote')[:6]
   top_ideas = Suggestion.objects.all().order_by('-suggestion_vote')[:6]
   context = {'issue':issue, 'hot_issues':hot_issues,'top_ideas':top_ideas}
   return render(request, 'customerapp/issuepage.html',context)


@login_required
@user_passes_test(user_citizen_check)
def ideaPage(request, ideaId):
   suggestion = get_object_or_404(Suggestion, pk=ideaId)
   hot_issues = CustomerIssue.objects.all().order_by('-issue_vote')[:6]
   top_ideas = Suggestion.objects.all().order_by('-suggestion_vote')[:6]
   context = {'suggestion': suggestion,'hot_issues':hot_issues,'top_ideas':top_ideas}
   return render(request, 'customerapp/ideapage.html',context)




