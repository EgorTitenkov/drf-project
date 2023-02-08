from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from . import validators
from .models import Product


class ProductInLineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    email = serializers.EmailField(write_only=True)

    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])
    body = serializers.CharField(source='content')

    class Meta:
        model = Product
        fields = [
            'owner',
            'email',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'public',
            'path',
        ]

    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username
        }

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get('request')

        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
