from django.shortcuts import redirect, render
from .models import Article
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def archive(request):
    posts = Article.objects.all()
    return render(request, 'archive.html', {"posts": posts})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=article.id) 
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not (username and password):
            return render(request, 'login.html', {'errors': 'Введите имя пользователя и пароль.'})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('archive')
        else:
            return render(request, 'login.html', {'errors': 'Неверное имя пользователя или пароль.'})
    else:
        return render(request, 'login.html', {})

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if not (username and email and password and password2):
            return render(request, 'register.html', {'errors': 'Все поля обязательны для заполнения.'})

        if password != password2:
            return render(request, 'register.html', {'errors': 'Пароли не совпадают.'})

        try:
            User.objects.get(username=username)
            return render(request, 'register.html', {'errors': 'Пользователь с таким именем уже существует.'})
        except User.DoesNotExist:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('archive')

    else:
        return render(request, 'register.html', {})