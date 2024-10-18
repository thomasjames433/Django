from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .models import Feature, Match,Footballer

# Create your views here.
def index(request):
    # 1
    # name='KSI'
    # return render(request,'index.html',{'name':name})

    fx=Footballer.objects.all()


    contents={
        'name':'Kroos',
        'age': 34,
        'country': 'German'
    }
    f1=Feature()
    f1.id=1204324
    f1.name='KSIOLAJIDEBT'
    f1.details=" KSI, is an English social media influencer, professional boxer, and musician. He is a co-founding member of YouTube group The Sidemen, the CEO of Misfits Boxing, and the co-owner of Prime Hydration, XIX Vodka, Sidemen Clothing, restaurant chain Sides, and cereal brand Best Breakfasts."
    f1.valid=True

    f3=Feature()
    f3.id=1204324
    f3.name='LOGAN PAUL'
    f3.details=" KSI, is an English social media influencer, professional boxer, and musician. He is a co-founding member of YouTube group The Sidemen, the CEO of Misfits Boxing, and the co-owner of Prime Hydration, XIX Vodka, Sidemen Clothing, restaurant chain Sides, and cereal brand Best Breakfasts."
    f3.valid=True

    f4=Feature()
    f4.id=1204324
    f4.name='DEJI'
    f4.details=" KSI, is an English social media influencer, professional boxer, and musician. He is a co-founding member of YouTube group The Sidemen, the CEO of Misfits Boxing, and the co-owner of Prime Hydration, XIX Vodka, Sidemen Clothing, restaurant chain Sides, and cereal brand Best Breakfasts."
    f4.valid=False

    f5=Feature()
    f5.id=1204324
    f5.name='JAKE PAUL'
    f5.details=" KSI, is an English social media influencer, professional boxer, and musician. He is a co-founding member of YouTube group The Sidemen, the CEO of Misfits Boxing, and the co-owner of Prime Hydration, XIX Vodka, Sidemen Clothing, restaurant chain Sides, and cereal brand Best Breakfasts."
    f5.valid=False

    f2=Match
    f2.name1="LOGAN PAUL"
    f2.name2="KSI"
    f2.todo="BOOK NOW"
    

    feats=[f1,f3,f4,f5]
    # return render(request, 'index.html',contents)
    
    # return render(request, 'index.html',{'Feat': f1, 'MAT': f2})
    # return render(request, 'index.html',{'Feat': feats, 'MAT': f2, 'featind': feats[1]})
    return render(request, 'index.html',{'Feat': feats,'MAT': f2, 'featind': feats[1],'footy' : fx})

def register(request):
    if request.method== 'POST':
        username=request.POST['Username']
        email=request.POST['Email']
        password=request.POST['Password']
        checkpassword=request.POST['Re-Enter Password']

        if password== checkpassword:
            if User.objects.filter(email=email).exists(): #checks if email is alredy used
                    messages.info(request, "Email Already Used")
                    return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username Not Available")
                return redirect('register')
            else:
                 user= User.objects.create_user(username=username,email=email,password=password)
                 user.save()
                 return redirect("login")
        else:
            messages.info(request,"Passwords Do Not Match")
            return redirect('register')
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is None:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
        else:
            auth.login(request,user)
            return redirect('/')
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request,pk):
    return render(request,'post.html',{'pk':pk})

def manyposts(request):
    collections={'1','2','thomas','james','5'}
    return render(request,'manyposts.html',{'mp':collections})