from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
	posts = Post.objects.order_by('created_date')
	return render(request, 'my_app/post_list.html', {'posts': posts})
"""def post_new(request):
	form = PostForm()
	return render(request, 'my_app/post_new.html', {'form': form})"""
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			"""post.created_date=timezone.now()"""
			post.save()
			return redirect('post_list')
	else:
		form = PostForm()
	return render(request, 'my_app/post_new.html', {'form': form})



# Create your views here.

# Create your views here.
