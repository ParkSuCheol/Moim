from django.conf.urls import url
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter(trailing_slash=False)
router.register("stores", views.StoreViewSet, basename="stores")

urlpatterns = router.urls

app_name = 'api'

urlpatterns = [
    path('store/<store_id>', views.storedetail, name='storedetail'),
    path('store/reviews/<store_id>', views.storereview, name='storereview'),
    path('store/reviews/test/<store_id>', views.testreview, name='testreview'),
    
    path('store/review2/create', views.reviewcreate, name='reviewcreate'),
    path('store/firstrecommend/<store_id>', views.storerecommend, name='storerecommend'),
    path('store/storerecommend/<str:choice>', views.searchrecommend, name='searchrecommend'),
]