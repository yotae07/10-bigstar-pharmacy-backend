import json

from django.views import View
from django.http import JsonResponse

from user.utils import LoginConfirm
from .models import Cart
from task.models import Product
from user.models import User

class CartAdd(View):
    @LoginConfirm
    def post(self, request):
        data = json.loads(request.body)
        try:
            p_id = Product.objects.get(item=data['item']).id
            if Cart.objects.filter(item=data['item'], user_id=request.user.id).exists():
                return JsonResponse({'message':'이미 담겼어요'})
            
            Cart(item      = data['item'],
                count      = data['count'],
                product_id = p_id,
                user_id    = request.user.id
            ).save()

            return JsonResponse({'message':'Added'})
        
        except:
            return JsonResponse({'message':'품목이 잘못되었어요'})

class Count(View):
    @LoginConfirm
    def post(self, request):
        data = json.loads(request.body)
        try:
            info       = Cart.objects.get(item=data['item'], user_id=request.user.id)
            info.count = data['count']
            info.save()
        
            return JsonResponse({'count':info.count})

        except:
            return JsonResponse({'message':'없는데 어케 더해?'})

class CartView(View):
    @LoginConfirm
    def get(self, request):
        cart_in  = Cart.objects.filter(user_id=request.user.id)
        if not cart_in:
            return JsonResponse({'message':'장바구니에 추가된 제품이 없습니다. 몇가지 건강 설문을 통해 나만을 위한 영양성분을 찾아보세요.'})
        data_set = [({
            'name' :cart_in[i].item,
            'count':cart_in[i].count,
            'id'   :cart_in[i].product_id,
            'image':Product.objects.get(id=cart_in[i].product_id).image_product,
            'price':Product.objects.get(id=cart_in[i].product_id).pricenum,
            'colors':Product.objects.get(id=cart_in[i].product_id).colors}) for i in range(len(cart_in))]

        return JsonResponse({'order':data_set})

class DeleteItem(View):
    @LoginConfirm
    def post(self, request):
        data = json.loads(request.body)
        
        if data['delete'] == 'delete':
            Cart.objects.filter(user_id=request.user.id).delete()
            return JsonResponse({'message':'텅텅'})
        
        return JsonResponse({'message':'delete을 입력해서 보내주세요'})    



