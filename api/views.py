from django.db.models import Max
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Category, Service, Salun, Auto, Warehouse, Condition, Buyer, Airport, Person, Super
from .serializers import CategorySerializer, ServiceSerializer, SalunSerializer, AutoSerializer, WarehouseSerializer, \
    ConditionSerializer, BuyerSerializer, AirPortSerializer, PersonSerializer, SuperSerializer


@api_view()
def get_categoryes(request):
    categoryes = Category.objects.all()
    serializers = CategorySerializer(categoryes, many = True)
    return Response(serializers.data)

@api_view()
def get_services(request):
    services = Service.objects.all()
    serializers = ServiceSerializer(services , many=True, read_only=True)
    print(serializers.data)
    return Response(serializers.data)

@api_view()
def get_services_for_title(request, title):
    service = get_object_or_404(Service, title=title)
    serializer = ServiceSerializer(service)
    return Response(serializer.data)

@api_view()
def get_salons(request):
    saluns = Salun.objects.all()
    serializers = SalunSerializer(many=True)
    return Response(serializers.data)

@api_view(["GET"])
def get_json_autos(request):
    autos = Auto.objects.all()
    serializer = AutoSerializer(autos, many=True)
    # print(serializer.data[0]['brand'])
    return Response(serializer.data)
    # d_for_json = {}
    # d = autos[0].__dict__
    # d_for_json['id']= d['id']
    # d_for_json['brand']= d['brand']
    # d_for_json['model']= d['model']
    # d_for_json['price']= float(d['price'])
    # return Response({'status':autos[0].__dict__})
    # return Response(d_for_json)

@api_view()
def get_json_warehouse(request):
    warehouses = Warehouse.objects.all().annotate(max_price=Max('autos__price'))
    serializer = WarehouseSerializer(warehouses, many=True)
    print(warehouses)
    return Response(serializer.data)


@api_view()
def get_json_condition(request):
    condition = Condition.objects.all()
    serializer = ConditionSerializer(condition, many=True)
    return Response(serializer.data)


@api_view()
def get_json_buyer(request):
    """Doc String"""
    buyer = Buyer.objects.all()
    serializer = BuyerSerializer(buyer, many=True)
    return Response(serializer.data)


class ServicesApiView(APIView):
    def get(self, request):
        queryset = Service.objects.all()
        serializer = ServiceSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = ServiceSerializer(data=request.data)
        print(request.data)
        if data.is_valid():
            new_service = Service(category=Category)
            service_instance = Service()
            service_instance.objects.create(service)
            return Response(service.data)
        else:
            print(data.errors)

        return Response('данные не корректы')

class MadDiesel(APIView):
    def get(self, request):
        queryset = Auto.objects.all()
        serializer = AutoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request):
        info = AutoSerializer(data=request.data)
        if info.is_valid(raise_exception=True):
            auto = Auto(
                model = info.data.get("model"),
                brand = info.data.get("brand"),
                engine = info.data.get("engine"),
                price = info.data.get("price"),
            )
            print(auto.__dict__)
            auto.save()
            print('ok')
        else:
            print('error')
        return Response({'static': 'valid'})


class WarehouseViewSet(viewsets.ViewSet):
    def list(self, request):
        query = Warehouse.objects.all()
        serializer = WarehouseSerializer(query, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        stores = Warehouse.objects.all()
        store = get_object_or_404(stores, pk=pk)
        serializer = WarehouseSerializer(store)
        return Response(serializer.data)

    def destroy(self,request, pk=None):
        store = Warehouse.objects.get(pk=pk)
        store.delete()
        return Response(status=202)


'''air'''


class AirPortViewSet(viewsets.ViewSet):
    def list(self, request):
        port = Airport.objects.all()
        serializer = AirPortSerializer(port, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        angar = Airport.objects.get(pk=pk)
        serializer = AirPortSerializer(instance=angar ,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

''''''
# @api_view(['GET','POST'])
# def get_person(request, pk=None):
#     list = get_object_or_404(Person, pk=pk)
#     serializer = PersonSerializer(list, many=True)
#
#     if request.method == 'POST':
#         pers = PersonSerializer(data=request.data)
#         print (pers.is_valid())
#         if pers.is_valid():
#             pers_instance = Person.objects.get(pk=pk)
#             print(pers_instance.__dict__)
#     return Response(serializer.data)

@api_view(['GET','POST'])
def get_person(request, pk=None):
    query = Person.objects.all()
    person = get_object_or_404(query ,pk=pk)
    serializer = PersonSerializer(person, many=True)
    return Response(serializer.data)

''''''

def get_com(request)
    pass
class Super(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format = None):
        queryset = Super.objects.all()
        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data)


def get_page(request):
    summ.delay(100,200)
    return render(request, "index.html")

