from django.urls import path , include

from .views import ProductDetail, LatestProductsList, CategoryDetail, search

urlpatterns = [
	path('latest/', LatestProductsList.as_view()),
	path('products/search/', search),
	path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
	path('products/<slug:category_slug>/', CategoryDetail.as_view()),
]

