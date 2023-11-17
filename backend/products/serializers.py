from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title, unique_title_validator

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field='pk')
    title = serializers.CharField(validators=[unique_title_validator])
    class Meta:
        model = Product
        fields = [
                #   'user',
                  'url',
                  'edit_url',
                  'id',
                  'title',
                  'content',
                  'price',
                  'sale_price',
                  'my_discount',
                  ]
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name!") 
    #     return value
        
    def get_edit_url(self, obj):
        # return f"api/products/{obj.id}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={'pk':obj.id}, request=request)
        
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
