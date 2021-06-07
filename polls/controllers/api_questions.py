from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from polls.dtos.question import QuestionOutputDTO, QuestionInputDTO
from polls.models import Question


def detail(request, id: int):
    try:
        question = Question.objects.get(pk=id)

        data = QuestionOutputDTO(question).dump()

        return JsonResponse(data)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()


@csrf_exempt
def add(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()

    question_input = QuestionInputDTO.loads(request.body.decode('utf-8'))
    question = Question(
        question_text=question_input.questionText,
        author=question_input.author,
        status=question_input.status,
        pub_date=question_input.publishTime
    )
    question.save()

    output = {'id': question.id}

    return JsonResponse(output)
