from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Story, Comment
from .forms import CommentForm


# Create your views here.
class StoriesList(generic.ListView):
    queryset = Story.objects.filter(approval=1).order_by("-created_on")
    template_name = "stories/index.html"
    paginate_by = 3

class AllStoriesList(generic.ListView):
    queryset = Story.objects.filter(approval=1).order_by("-created_on")
    template_name = "stories/stories_list.html"
    paginate_by = 6

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


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Story.objects.filter(approval=1)
        story = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            rating = comment_form.save(commit=False)
            comment.story = story
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('story_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Story.objects.filter(approval=1)
    story = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'Can only delete own comments!')

    return HttpResponseRedirect(reverse('story_detail', args=[slug]))
