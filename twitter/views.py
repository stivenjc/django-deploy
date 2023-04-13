from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from twitter.forms import PostForm, UserUpdateForm, ProfileUpdateForm
from twitter.models import Post


@login_required
def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = PostForm(request.POST)

            if form.is_valid():
                create_post = Post.objects.create(
                    content=form.cleaned_data.get('content'),
                    user=request.user
                )
                create_post.save()
                return redirect('twitter:home')

    else:
        form = PostForm()

    context = {'posts': posts, 'form': form}
    return render(request, 'twitter/newsfeed.html', context)


class PostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'social/post.html'
    success_url = reverse_lazy('twitter:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('twitter:home')


def profile(request, username):
    user = User.objects.get(username=username)
    posts = user.posts.all()
    context = {'user': user, 'posts': posts}
    return render(request, 'twitter/profile.html', context)


def edit_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('twitter:home')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm()
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'twitter/editar.html', context)
