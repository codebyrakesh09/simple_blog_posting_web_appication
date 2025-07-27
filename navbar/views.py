from django.shortcuts import render, get_object_or_404, redirect
from .models import Post  # imported Post model
from .forms import PostForm, ContactForm  # reuse the same form used for creating
from django.contrib import messages


def home(request): 
    posts = Post.objects.all().order_by('-published_at')
    return render(request, 'navbar/home.html', {'posts': posts})


def about(request):
    return render(request, 'navbar/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # Redirect to the contact page after successful form submission
        else:
            messages.error(request, "There was an error with your submission. Please try again.")
    else:
        form = ContactForm()

    return render(request, 'navbar/contact.html', {'form': form})


def blog_page(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'navbar/blog_page.html', {'post': post})


def add_post(request):  # when you click on submit request = POST
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'navbar/add_post.html', {'form': form})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            # return redirect('post_detail', post_id=post.id)  # don't have post detail page.
            return redirect('home')
    else:
        form = PostForm(instance=post)

    return render(request, 'navbar/edit_post.html', {'form': form, 'post': post})

# Editing and Deleting Posts in Django
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'navbar/delete_post.html', {'post': post})




