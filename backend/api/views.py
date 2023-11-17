# from django.shortcuts import render
# from django.http import JsonResponse
# import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer

# def apiHome(request, *args, **kwargs):    #^ for general learning purpose....
#     body = request.body
#     # print(body)    #bytes string
#     # print(type(body))       #<class 'bytes'>
#     data = {}
#     try:
#         data = json.loads(body)    #string of Json data(bytes string) --> python dictionary
#     except:
#         pass
    
#     # print(type(data))     #<class 'dict>
#     # print(data)
#     # data['Anything'] = "Anything i want!! I can add this key in json response!!"
#     # print(request.GET)             #<QueryDict: {'abc': ['123']}>
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)


# def apiHome(request, *args, **kwargs):            #^ product view with the help of pure django
#     model_data = Product.objects.all().order_by('?').first()
#     data = {}
#     if model_data:
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.title
        
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#     return JsonResponse(data)


@api_view(["GET"])
def apiHome(request, *args, **kwargs):     #* api view with the help of django rest framework
    '''
    Django Rest Framework Api View
    '''
    
    # instance = Product.objects.all().order_by('?').first()
    instance = Product.objects.all()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=['id', 'title', 'price'])
        data = ProductSerializer(instance, many=True).data
    return Response(data)



# @api_view(["POST"])
# def apiHome(request, *args, **kwargs):
    
#     serializer = ProductSerializer(data = request.data)
#     if serializer.is_valid(raise_exception=True):
#         # instance = serializer.save()
#         # print(instance)
#         return Response(serializer.data)
#     else:
#         return Response({"invalid": "Not good data!"}, status=400)


