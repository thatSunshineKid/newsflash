from django.shortcuts import render
from django.views import generic

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Author, Post

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_posts=Post.objects.all()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_posts':num_posts,'num_authors':num_authors},
    )


class PostListView(generic.ListView):
    model = Post
    paginate_by = 10


class PostDetailView(generic.DetailView):
    model = Post

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author



class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/flash'

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    success_url = '/flash'

class PostUpdate(UpdateView):
    model = Post
    fields = ['title','author','url']

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
