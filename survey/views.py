import json

from django.views import View
from django.http  import JsonResponse

from .models      import Question, Answer, UserQuestion, Result
from user.utils   import LoginConfirm

def CheckResult(find_drug):
    result = {
        '프로바이오틱스' : {1,2,3,4,5},
        '칼슘마그네슘비타민D' : {1,2,3,4,6},
        '비타민B' : {1,2,3,4,7},
        '비타민C' : {1,2,3,4,8},
        '루테인' : {1,2,3,4,9},
        '밀크씨슬' : {1,2,3,4,10},
        '오메가3' : {1,2,3,4,11}
    }
    for key, value in result.items():
        if value == find_drug:
            show_result = Result.objects.get(name = key)
            return JsonResponse(
                {
                    'user' : request.user.name,
                    'name' : show_result.name,
                    'result' : show_result.user_result
                }, status=200)
        return JsonResponse({'message' : 'NOT_MATCH'}, status=401)

class SurveyView(View):
    @LoginConfirm
    def post(self, request):
        try:
            data = json.loads(request.body)
            if data['next'] and data['answer'] != "None":
                next_answer = []
                for i in data['next']:
                    user_answer  = Answer.objects.get(answer = i)
                    user_answer1 = Answer.objects.get(answer = data['answer'])
                    UserQuestion(
                        user        = request.user,
                        question    = user_answer.question_id,
                        user_answer = user_answer1.id
                    ).save()
                    next_answer.append(user_answer.answer_tag)
                    next_answer = set(next_answer)
                next_answer     = list(next_answer)
                next_question   = Question.objects.get(id = int(next_answer[0]))
                question        = next_question.question
                sub_question    = next_question.sub_question
                answer_all      = Question.objects.filter(id = int(next_answer[0])).prefetch_related('answer_set')
                answer_box      = []
                answer_type_box = []
                for j in answer_all[0].answer_set.all():
                    answer_box.append(j.answer)
                    answer_type_box.append(j.answer_type)
                return JsonResponse(
                    {
                        'question' : question,
                        'sub_question' : sub_question,
                        'answer' : answer_box,
                        'answer_type' : answer_type_box
                    }, status=200)
            elif data['next'] and data['answer'] == "None":
                next_answer = []
                for i in data['next']:
                    if i == "0":
                        show_question     = Question.objects.get(id = 1)
                        show_sub_question = show_question.sub_question
                        show_answer       = Answer.objects.get(id=1)
                        return JsonResponse(
                            {
                                'question' : show_question.question,
                                'sub_question' : show_sub_question,
                                'answer' : show_answer.answer,
                                'answer_type' : show_answer.answer_type
                            }, status=200)
                    user_answer = Answer.objects.get(answer = i)
                    UserQuestion(
                        user        = request.user,
                        question    = user_answer.question_id,
                        user_answer = user_answer.id
                    ).save()
                    next_answer.append(user_answer.answer_tag)
                    next_answer = set(next_answer)
                next_answer     = list(next_answer)
                next_question   = Question.objects.get(id = int(next_answer[0]))
                question        = next_question.question
                answer_all      = Question.objects.filter(id = int(next_answer[0])).prefetch_related('answer_set')
                answer_box      = []
                answer_type_box = []
                for j in answer_all[0].answer_set.all():
                    answer_box.append(j.answer)
                    answer_type_box.append(j.answer_type)
                return JsonResponse(
                            {
                                'question' : question,
                                'answer' : answer_box,
                                'answer_type' : answer_type_box
                            }, status=200)
            else:
                return JsonResponse({'message' : 'INVALID_REQUEST'}, status=401)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=401)

class SurveyResultView(View):
    @LoginConfirm
    def get(slef, request):
        data = json.loads(request.body)
        try:
            if data['result']:
                user             = request.user
                user             = UserQuestion.objects.filter(user = user.id)
                user_select_list = []
                for i in user:
                    user_select_answer = i.user_answer
                    user_select_list.append(user_select_answer)
                user_select_list = set(user_select_list)
                CheckResult(user_select_list)
            return JsonResponse({'message' : 'INVALID_RESULT'}, status=401)
        except KeyError:
            JsonResponse({'message' : 'KEY_ERROR'}, status=401)
