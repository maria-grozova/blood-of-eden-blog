from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Story

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

    queryset = Story.objects.filter(approval=0)
    story = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "stories/story_detail.html",
        {"story": story},
    )