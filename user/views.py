from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import Registerform, createRecipe
from datetime import datetime
from .models import Recipe
# Create your views here.


@login_required
def user_logout(request):
    logout(request)
    return redirect('/')


@login_required
def profile(request):
    return render(request, "profile.html")


'''
def register(request):
    if request.method == "POST":
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Registerform()
    return render(request, "register/register.html", {"form": form})
'''


def register(request):
    message = ''
    if request.method == "POST":
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            email = request.POST.get('email')
            if len(password1) < 8:
                message = '密碼少於8個字元'

            elif password1 != password2:
                message = '兩次密碼不相同'
            else:
                if User.objects.filter(username=username).exists():
                    message = '帳號重複'
    else:
        form = Registerform()
    return render(request, "register/register.html", {"form": form, "message": message})


@login_required
def create(request):
    form = createRecipe()
    if request.method == "POST":
        if request.user.is_authenticated:
            form = createRecipe(request.POST, request.FILES)
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.created = datetime.now()
            recipe.save()
            return redirect('view')
    return render(request, "create.html", {"form": form})


@login_required  # 回傳登入者所有食譜畫面
def view(request):
    recipe = Recipe.objects.filter(user=request.user)
    return render(request, "view.html", {"recipe": recipe})


@login_required
def sortcreate(request):  # 排序
    recipe = Recipe.objects.filter(user=request.user)
    sort = request.COOKIES.get('sort')
    sort = '1' if not sort or sort == '0' else '0'

    if sort == '1':
        recipe = recipe.order_by('-created')

    response = render(request, "view.html", {"recipe": recipe})
    response.set_cookie('sort', sort)
    return response


def update(request, id):  # 回傳更新畫面
    myrecipe = Recipe.objects.get(id=id)
    recipe = Recipe.objects.filter(user=request.user)
    return render(request, "update.html", {"myrecipe": myrecipe, "recipe": recipe})


def updaterecord(request, id):  # 修改內容
    title = request.POST["title"]
    text = request.POST["text"]
    img = request.POST.get("image")  # 取得圖片
    myrecipe = Recipe.objects.get(id=id)
    myrecipe.image = myrecipe.image  # 圖片=原本上傳的圖片
    myrecipe.title = title
    myrecipe.text = text
    # 如果name屬性取得為空值，則保留原本的圖片
    if img == "":
        myrecipe.image = myrecipe.image
    else:
        myrecipe.image = img

    myrecipe.save()
    return redirect("view")


@login_required
def delete(request, id):
    recipe = Recipe.objects.get(id=id)
    recipe.delete()
    return redirect('view')
