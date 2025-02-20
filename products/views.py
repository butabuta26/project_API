from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin

from rest_framework.permissions import IsAuthenticated

from .models import Cart, ProductTag, FavoriteProduct, Product, Review, ProductImage
from .serializers import (CartSerializer, ProductTagSerializer,
                          FavoriteProductSerializer, ProductSerializer, ReviewSerializer, ProductImageSerializer)

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
    
class ReviewViewSet(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(product_id=self.kwargs['product_id'])
    
    # def get(self, request, pk=None, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def get(self, request, pk=None, *args, **kwargs):
    #     if pk:
    #         return self.retrieve(request, *args, **kwargs)
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    
    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
    
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
    
    
class FavoriteProductViewSet(ModelViewSet):
    serializer_class = FavoriteProductSerializer
    queryset = FavoriteProduct.objects.all()
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']
    
    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset
    
class CartViewSet(CreateModelMixin, ListModelMixin, GenericAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class ProductTagListViewSet(ListAPIView):
    serializer_class = ProductTagSerializer
    queryset = ProductTag.objects.all()
    permission_classes = [IsAuthenticated]
    
class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return self.queryset.filter(product__id=self.kwargs.get('product_id'))