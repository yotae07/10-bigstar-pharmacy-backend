import json

from django.views import View
from django.http  import JsonResponse

from user.utils   import LoginConfirm
from .models      import (
    Question,
    Answer,
    UserQuestion,
    Result
)

def CheckResult(find_drug):
    result = {
        '프로바이오틱스' : [1,2,3,4,5],
        '칼슘마그네슘비타민D' : [1,2,3,4,6],
        '비타민B' : [1,2,3,4,7],
        '비타민C' : [1,2,3,4,8],
        '루테인' : [1,2,3,4,9],
        '밀크씨슬' : [1,2,3,4,10],
        '오메가3' : [1,2,3,4,11]
    }
    for key in result.keys():
        if find_drug == result[key]:
            return Result.objects.get(name = key)
    return Result.objects.get(name = '칼슘마그네슘비타민D')

class SurveyView(View):
    @LoginConfirm
    def post(self, request):
        try:
            data = json.loads(request.body)
            if data['next'] and data['answer'][0] != "None":
                for j in data['answer']:
                    recode_answer = Answer.objects.select_related('question').get(answer = j)
                    UserQuestion(
                        user        = request.user,
                        question    = recode_answer.question,
                        user_answer = recode_answer.id
                        ).save()
                list_next_answer = list(set([Answer.objects.get(answer = i).answer_tag for i in data['next']]))
                answer_all       = Question.objects.filter(id = int(list_next_answer[0])).prefetch_related('answer_set')
                answer_box       = [j.answer_type for j in answer_all[0].answer_set.all()]
                answer_type      = list(set([j.answer_type for j in answer_all[0].answer_set.all()]))
                if answer_all[0].sub_quesion:
                    sub_question = answer_all[0].sub_quesion
                else:
                    sub_question = "None"
                return JsonResponse(
                    {
                        'question_id': answer_all[0].id,
                        'question' : answer_all[0].question,
                        'sub_question' : sub_question,
                        'answer' : answer_box,
                        'answer_type' : answer_type[0]
                    }, status=200)
            elif data['next'] and data['answer'][0] == "None":
                if data['next'] == ["100"]:
                    return JsonResponse({'message': 'finish'}, status=200)
                next_answer = []
                for i in data['next']:
                    if i == "0":
                        UserQuestion.objects.filter(user = request.user).delete()
                        show_question = Question.objects.get(id = 1)
                        show_answer   = Answer.objects.get(id=1)
                        return JsonResponse(
                            {
                                'question_id': show_question.id,
                                'question' : show_question.question,
                                'answer' : show_answer.answer,
                                'answer_type' : show_answer.answer_type
                            }, status=200)
                    recode_answer = Answer.objects.get(answer = i)
                    UserQuestion(
                        user        = request.user,
                        question    = recode_answer.question,
                        user_answer = recode_answer.id
                    ).save()
                    next_answer.append(Answer.objects.get(answer = i).answer_tag)
                list_next_answer = list(set(next_answer))
                answer_all       = Question.objects.filter(id = int(list_next_answer[0])).prefetch_related('answer_set')
                answer_box       = [j.answer_type for j in answer_all[0].answer_set.all()]
                answer_type      = list(set([j.answer_type for j in answer_all[0].answer_set.all()]))
                if answer_all[0].sub_quesion:
                    sub_question = answer_all[0].sub_quesion
                else:
                    sub_question = "None"
                return JsonResponse(
                            {
                                'question_id': answer_all[0].id,
                                'question' : answer_all[0].question,
                                'sub_question' : sub_question,
                                'answer' : answer_box,
                                'answer_type' : answer_type[0]
                            }, status=200)
            else:
                return JsonResponse({'message' : 'INVALID_REQUEST'}, status=401)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=401)

class SurveyResultView(View):
    @LoginConfirm
    def post(self, request):
        data = json.loads(request.body)
        try:
            if data['result']:
                user             = User.objects.filter(user = request.user)
                user_select_list = [i.user_answer for i in user]
                result           = CheckResult(user_select_list)
                return JsonResponse(
                    {
                        'name': result.name,
                        'result': result.user_result
                    }, status=200)
        except KeyError:
            JsonResponse({'message' : 'KEY_ERROR'}, status=401)