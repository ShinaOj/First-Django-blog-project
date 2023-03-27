

# Create your views here.
from django.shortcuts import render, redirect
from .models import Post, Category,Tag, Author,Comment
from django.contrib import messages
from .forms import Tagform, AuthForm, PostForm, CommentForm


# Create your views here.


def home_page_view(request):
    posts = Post.objects.all()
    category= Category.objects.all()
    tag = Tag.objects.all()
    context = {
        "posts_object" : posts,
        "category_obj" : category,
        "tagg" : tag,
        
    }
    return render(request, 'mainapp/index.html', context)

def post_detail_page(request, post_id):
    post_detail = Post.objects.get(id=post_id)
    num_visits= request.sessions.get('visit_count', 0)
    request.session['visit_count']=num_visits +1
    form=CommentForm(request.POST or None)
    if request.method== 'POST':
        if form.is_valid():
            Comment.objects.create(
                post=post_detail,
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                comment=form.cleaned_data['comment']
            )
            return redirect('detail', post_id=post_detail.id)

    category = Category.objects.all()
    tag = Tag.objects.all()
    context={
        "post" : post_detail,
        "category" : category,
        "num_visitor": num_visits,
        "comment_list":Comment.objects.filter(post__id=post_id),
        "tagg" : tag
    }
    return render(request, 'mainapp/single.html', context)

def post_create_page(request):
    context={}
    post_form=PostForm()
    context['post_form']=post_form
    if request.method == "POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            author_name=form.cleaned_data['author']
            author=Author.objects.get_or_create(name=author_name)
            post.author=author
            post.save()
            messages.success(request, "new post added")
            return redirect('home')
        messages.error(request, 'mainapp/post.html', context)
    return render(request, 'mainapp/post.html', context)


def form_create_view(request):
    tag_form=Tagform()
    author_form=AuthForm()
    context ={
        "tag_form":tag_form,
        "auth_form":author_form
    }
    if request.method =='POST':
        category=request.POST.get('category')
        print(category)
        Category.objects.create(name=category)
        messages.success(request, "category created succesfully")
    return render (request, "mainapp/formtest.html", context)


def handle_tag_form(request):
    if request.method == "POST":
        form=Tagform(request.POST)
        if form.is_valid():
            tagname=form.cleaned_data['name']
            Tag.objects.create(name=tagname)
            messages.success(request, f"{tagname} was added successfully")
            return redirect('form-create')
    return render(request, "mainapp/formtest.html")

def handle_author_form(request):
    if request.method =='POST':
        form=AuthForm(request.POST)
        if form.is_valid():
            auth_name=form.cleaned_data['name']
            form.save()
            messages.success(request, f"{auth_name} created successfully")
            return redirect ('form-create')
    return render(request, "mainapp/formtest,html")
            
