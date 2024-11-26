from django.shortcuts import render
from .models import ContactedUser
from django.core.mail import send_mail

# Create your views here.

def home(request):
    context = {
        'title':'Home'
    }
    return render(request,'index.html',context)
def fashion(request):
    context = {
        'title':'Fashion'
    }
    return render(request,'blog-category-01.html',context)
def food(request):
    context = {
        'title':'Food'
    }
    return render(request,'blog-category-02.html',context)
def lifestyle(request):
    context = {
        'title':'Life-style'
    }
    return render(request,'blog-category-03.html',context)
def travel(request):
    context = {
        'title':'Travel'
    }
    return render(request,'blog-category-04.html',context)
def vlog(request):
    context = {
        'title':'Vlog'
    }
    return render(request,'blog-category-05.html',context)
def health(request):
    context = {
        'title':'Health'
    }
    return render(request,'blog-category-06.html',context)
def single(request):
    context = {
        'title':'Single-Page'
    }
    return render(request,'single.html',context)
def blogAuthor(request):
    context = {
        'title':'Blog Author-Page'
    }
    return render(request,'blog-author.html',context)
def page_contact(request):

    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        message=request.POST.get('message')
        subject=request.POST.get('subject')

        new_user_contacted = ContactedUser(
            name=name,
            email=email,
            number=number,
            message=message,
            subject=subject
        )
        new_user_contacted.save()

        email_subject = f"{subject}"
        email_message = f"The user contacted's detail are : - \nName - {name}\nEmail - {email}\nPhone Number - {number}\nMessage - {message}"
        from_email = 'shivampandey839@gmail.com'
        to_email = ['shivam839pandey@gmail.com']

        send_mail(email_subject,email_message,from_email,to_email)


    context = {
        'title':'Contact-Page'
    }
    return render(request,'page-contact.html',context)