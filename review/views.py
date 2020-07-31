import json

from django.views import View
from django.http import JsonResponse

from .models import Review

class ReviewToPage(View):
    def get(self, request):
        reviews = Review.objects.all()

        if request.method == "GET":
            data_set =[ ({'id':reviews[i].id,
                              'name':reviews[i].name,
                              'purchased_item':reviews[i].purchased_item,
                              'purchased_date':reviews[i].purchased_date,
                              'photo':reviews[i].photo,
                              'comment':reviews[i].comment
                             }) for i in range(len(reviews))]
        
        return JsonResponse({'main_data':data_set})





