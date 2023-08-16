from django.shortcuts import render
from .models import Topic,Webpage,AccessRecord,User
from . import forms


# Create your views here.

def index(request):

    my_dict = {"insert_me" : "Hello I am coming from views.py"}

    return render(request, "first_app/index.html", my_dict)
    
def help(request):

    my_dict = {"second_text": "I'm here to help"}

    return render(request, "first_app/help.html", my_dict)

def image(request):

    return render(request, "first_app/image.html")

def webpages(request):
    
    # Gets Data from the DB.
    webpages_list = AccessRecord.objects.order_by('date')

    # Puts the data in a dictionary
    webpages_dict = { "webpages": webpages_list }

    # Pass the dictionary to the template
    return render(request,'first_app/webpages.html', webpages_dict) 

def users(request):

    users_list = User.objects.order_by('last_name')

    users_dict = { "users" : users_list }

    return render(request, 'first_app/users.html', users_dict)

def form_name(request):

    form = forms.FormName()
    
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Success")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])
            form = forms.FormName()
       

    return render(request, 'first_app/form_page.html', { 'form':form })

def new_user_form(request):
    form = forms.NewUserForm();
    
    if request.method == "POST":
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("User saved!")
            return users(request)
        else: 
            print('Invalid form')

    return render(request,'first_app/new_user.html', {'form':form} )

def users(request):

    users_list = User.objects.order_by('last_name')

    users_dict = { "users": users_list }

    return render(request, 'first_app/users.html', users_dict)

def page_one(request):
    return render(request, "first_app/page_one.html")

def other(request):
    return render(request, 'first_app/page_two.html')

def other_three(request):
    return render(request, 'first_app/page_three.html')

def other_four(request):
    return render(request, 'first_app/page_four.html')

def new_page(request):
    return render(request, 'first_app/page_new.html')

def other_five(request):
    return render(request, 'first_app/page_five.html')


def base(request):
    return render(request, 'first_app/base.html')

def base_other(request):
    return render(request, 'first_app/other.html')

def home(request):
    return render(request, 'first_app/home.html')

def template_home(request):
    return render(request, 'first_app/template_home.html')

def template_users(request):
    return render(request, 'first_app/template_users.html')


def template_form(request):
    form = forms.NewUserForm();
    
    if request.method == "POST":
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("User saved!")
            return users(request)
        else: 
            print('Invalid form')

    return render(request,'first_app/template_form.html', {'form':form} )