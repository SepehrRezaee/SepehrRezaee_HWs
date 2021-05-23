from django.shortcuts import render, redirect
from . import models, forms


def post_list(request):

    my_posts = models.Post.objects.all()
    return render(
        request=request,
        context={
            'my_posts': my_posts
        },
        template_name='blog/posts.html'
    )


def create_post(request):
    form_instance = forms.PostForm()

    if request.method == 'POST':
        form_instance = forms.PostForm(data=request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('blog:post-list')

    return render(request, 'blog/create_post.html', {'form': form_instance})
