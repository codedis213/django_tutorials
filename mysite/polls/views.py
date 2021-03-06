from django.shortcuts import get_object_or_404, render_to_response, redirect, render
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from polls.models import Choice, Poll
from django.utils import timezone

from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'polls/login.html')



@login_required(login_url='/')
def home(request):
    return render_to_response('polls/home.html')


def logout(request):
    auth_logout(request)
    return redirect('/')



class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        # return Poll.objects.order_by('-pub_date')[:5]
        return Poll.objects.filter(
        	pub_date__lte=timezone.now()
        	).order_by('-pub_date')[:5]


# def index(request):
#     latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#     context = {'latest_poll_list': latest_poll_list}
#     return render(request, 'polls/index.html', context)




class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


# def detail(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/detail.html', {'poll': poll})



class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


# def results(request, poll_id):
#     poll = get_object_or_404(Poll, pk=poll_id)
#     return render(request, 'polls/results.html', {'poll': poll})



def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))