from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Service, Super, Airboard


class SalunSerializer(serializers.Serializer):
    name = serializers.CharField()
    slug = serializers.SlugField()


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    slug =serializers.SlugField()


class ServiceSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    price = serializers.DecimalField(max_digits=20, decimal_places=2)
    saluns = SalunSerializer(many=True)
    category = CategorySerializer()

    # def save(self):
    #     title = self.validated_data['title']
    #     slug = self.validated_data['slug']
    #     price = self.validated_data['price']
    #     saluns = self.validated_data['saluns']
    #     category = self.validated_data['category']


'''4 tables'''


class BuyerSerializerFORWAREHOUSE(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    surname = serializers.CharField(max_length=250)
    address = serializers.CharField()


class WarehouseSerializer(serializers.Serializer):
    locate = serializers.CharField(max_length=250)
    type_warehouse = serializers.CharField(max_length=250)
    buyer_set = BuyerSerializerFORWAREHOUSE(many=True)


class BuyerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    surname = serializers.CharField(max_length=250)
    address = serializers.CharField()
    warehouse = WarehouseSerializer()


class ConditionSerializerAuto(serializers.Serializer):
    status = serializers.CharField(max_length=250)


class AutoSerializer(serializers.Serializer):
    brand = serializers.CharField(max_length=250)
    model = serializers.CharField(max_length=250)
    engine = serializers.CharField(max_length=250)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    warehouse = WarehouseSerializer(many=True)
    condition_set = ConditionSerializerAuto(many=True)


class ConditionSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=250)
    auto = AutoSerializer()


class ServiceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = 'all'


'''air'''


class AirBoardSerializer(serializers.Serializer):
    brand = serializers.CharField(max_length=255)
    model = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=5)

    def update(self, instance, validated_data):
        instance.brand = validated_data.get('brand', instance.brand)
        instance.model = validated_data.get('model', instance.model)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance
# class AirBoardSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Airboard
#         fields = "__all__"



class AirPortSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    airboard = AirBoardSerializer(many=True)


''''''


class PersonSerializerForHouse(serializers.Serializer):
    address = serializers.CharField(max_length=255)


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    rate = serializers.DecimalField(max_digits=10, decimal_places=2)
    # address = PersonSerializerForHouse(many=True)


class HouseSerializer(serializers.Serializer):
    address = serializers.CharField(max_length=255)


''''''


class SuperSerializer(ModelSerializer):
    class Meta:
        model = Super
        fields = '__all__'