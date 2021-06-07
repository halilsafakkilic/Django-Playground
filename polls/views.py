from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from polls.models import Question, Choice


def question_default_query_set():
    return Question.objects.filter(
        pub_date__lte=timezone.now(),
        status=1
    )


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    entity_limit = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entity_limit'] = self.entity_limit

        return context

    def get_queryset(self):
        return question_default_query_set().order_by('-pub_date')[:self.entity_limit]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return question_default_query_set()


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        return question_default_query_set()


def vote(request, question_id):
    question = None
    try:
        question = question_default_query_set().filter(id=question_id).get()

        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
