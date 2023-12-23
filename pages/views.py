from django.views.generic import TemplateView
from .models import Vote
from django.http import HttpResponse
from django.shortcuts import redirect, render


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


def home(request):

    voted_for = None

    if request.user.is_authenticated:
        voted_for = Vote.objects.filter(user=request.user).last()
    
    vivek_votes = Vote.objects.filter(vote_for="vivek").count()
    sandeep_votes = Vote.objects.filter(vote_for="sandeep").count()

    context = {
        "voted_for": voted_for, 
        "vivek_votes": vivek_votes, 
        "sandeep_votes": sandeep_votes
    }
    return render(request, "pages/home.html", context)


def cast_vote(request, vote_for):
    """
    Casts a vote
    """
    if vote_for not in ["sandeep", "vivek"]:
        return None
    
    vote = Vote.objects.filter(user=request.user)
    
    if vote.exists():
        last_vote = vote.last()
        if last_vote.vote_for != vote_for:
            last_vote.vote_for = vote_for
            last_vote.save()

        return redirect("pages:home")

    Vote.objects.create(vote_for=vote_for, user=request.user)
    return redirect("pages:home")

