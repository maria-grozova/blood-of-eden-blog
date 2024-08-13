from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Story, Comment
from .forms import CommentForm

# Create your views here.
class StoriesList(generic.ListView):
    queryset = Story.objects.all()
    template_name = "stories/index.html"
    paginate_by = 3

def story_detail(request, slug):
    """
    Display an individual :model:`stories.Story`.

    **Context**

    ``story``
        An instance of :model:`stories.Story`.

    **Template:**

    :template:`stories/story_detail.html`
    """

    queryset = Story.objects.filter(approval=1)
    story = get_object_or_404(queryset, slug=slug)
    comments = story.comments.all().order_by("-created_on")
    comment_count = story.comments.filter(approval=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            rating = comment_form.save(commit=False)
            comment.author = request.user
            comment.story = story
            comment_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
    

    comment_form = CommentForm()

    return render(
        request,
        "stories/story_detail.html",
        {
            "story": story,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )