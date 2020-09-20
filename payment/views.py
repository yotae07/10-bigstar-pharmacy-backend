import json

from django.views import View
from django.http import JsonResponse

from .models import Payment
from product.models import Product
from user.models import User
from cart.models import Cart
from user.utils import LoginConfirm

class PaymentView(View):
    @LoginConfirm
    def get(self, request):
        personal_info = User.objects.get(id=request.user.id)
        name          = personal_info.name
        contact       = personal_info.mobile_number
        email         = personal_info.email
        return JsonResponse({'name':name,
                             'phone_number':contact,
                             'email':email})

class PaymentTogo(View):
    @LoginConfirm
    def post(self, request):
        data          = json.loads(request.body)
        personal_info = User.objects.get(id = request.user.id)
        cart_info     = Cart.objects.filter(user_id = request.user.id)
        item          = [data['products'][i]['name'] for i in range(len(cart_info))]
        items         = ','.join(item)
        rgb           = [data['products'][i]['backgroundColor'] for i in range(len(cart_info))]
        rgbs          = '-'.join(rgb)
        img           = [data['products'][i]['imgUrl'] for i in range(len(cart_info))]
        imgs          = ','.join(img)
        count         = [data['products'][i]['ea'] for i in range(len(cart_info))]
        counts        = ','.join(count)
        price         = [data['products'][i]['price'] for i in range(len(cart_info))]
        prices        = '-'.join(price)
        try:
            if data['card_kakao']=='credit':
                Payment(
                    name             = data['name'],
                    contact          = data['contact'],
                    post_number      = data['post_number'],
                    address_street   = data['address_street'],
                    address_detail   = data['address_detail'],
                    customer_request = data['customer_request'],
                    card_number      = data['card_number'],
                    expired_month    = data['expired_month'],
                    expired_year     = data['expired_year'],
                    birth            = data['birth'],
                    card_password    = data['card_password'],
                    user_id          = personal_info.id,
                    purchased_item   = items,
                    price            = prices,
                    count            = counts,
                    total_price      = data['totalPrice'],
                    points           = 0,
                    back_image       = rgbs,
                    pill_image       = imgs,
                    card_kakao       = data['card_kakao']
                ).save()
                
            elif data['card_kakao']=='kakao':
                Payment(
                    name     = data['name'],
                    contact          = data['contact'],
                    post_number      = data['post_number'],
                    address_street   = data['address_street'],
                    address_detail   = data['address_detail'],
                    customer_request = data['customer_request'],
                    card_number      = data['card_number'],
                    expired_month    = data['expired_month'],
                    expired_year     = data['expired_year'],
                    birth            = data['birth'],
                    card_password    = data['card_password'],
                    user_id          = personal_info.id,
                    purchased_item   = items,
                    price            = prices,
                    count            = counts,
                    total_price      = data['totalPrice'],
                    points           = 0,
                    back_image       = rgbs,
                    pill_image       = imgs,
                    card_kakao       = data['card_kakao']
                ).save()

            cart_info.delete()
            return JsonResponse({'message':'Thanks for giving us great opportunity to share pilly life. Be healty!'})
        
        except Exception as e:
            return JsonResponse({"message":f"{e}"})

class MyPillyView(View):
    @LoginConfirm
    def get(self, request):
        payment_info = Payment.objects.filter(user_id = request.user.id).select_related('user')
        data_set = []
        pilly_set = []
        for i in range(len(payment_info)):
            result = Payment.objects.get(id=payment_info[i].id)

            items          = result.purchased_item.split(',')
            counts         = result.count.split(',')
            prices         = result.price.split('-')
            back_img       = result.back_image.split('-')
            img            = result.pill_image.split(',')
            total_price    = result.total_price
            user_name      = result.name
            address_street = result.address_street
            address_detail = result.address_detail
            card_number    = result.card_number
            method_payment = result.cardnkakao

            if request.method == 'GET':
                for i in range(len(items)):
                    mypilly = ({'name' : items[i],
                    'price'            : prices[i],
                    'count'            : counts[i],
                    'back_image'       : back_img[0],
                    'pill_image'       : img[i],
                                })
                    data_set.append(mypilly)

                pilly= ({f'order_info' : data_set,
                'user_name'            : user_name,
                'total_price'          : total_price,
                'address_street'       : address_street,
                'address_detail'       : address_detail,
                'card_number'          : card_number,
                'method_payment'       : method_payment})
                data_set=[]
                pilly_set.append(pilly)

        return JsonResponse({'item_info':pilly_set,
                             'user_name':request.user.name,
                             'email'    :request.user.email,
                             'contact'  :request.user.mobile_number})

