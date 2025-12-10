from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Post


from .models import Post, Status 
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    UserPassesTestMixin
)
class PostListView(ListView):
    template_name = "posts/list.html"
   # model = Post
    context_object_name = "post_list"
    status = Status.objects.get(name="published")
    queryset = Post.objects.filter(status=status).order_by("created_on").reverse()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    
    
class PostDraftListView(LoginRequiredMixin, ListView):
    template_name = "posts/draft_list.html"
    context_object_name = "drafts"
    status = Status.objects.get(name="draft")
    queryset = Post.objects.filter(status=status).order_by("created_on").reverse()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_posts = context['drafts'].filter(author=self.request.user)
        context['drafts'] = draft_posts
        return context
    
class PostArchivedListView(LoginRequiredMixin, ListView):
        template_name = "posts/archived_list.html"
        context_object_name = "archived"
        status = Status.objects.get(name="archived")
        queryset = Post.objects.filter(status=status).order_by("created_on").reverse()
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            archived_posts = context['archived'].filter(author=self.request.user)
            context['archived'] = archived_posts
            return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ['title', 'subtitle','body', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('posts:list')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ['title', 'subtitle', 'body' ,'status']