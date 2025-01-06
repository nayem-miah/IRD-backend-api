
from django.urls import path
from .views import CategoryView, SubCategoryView,DuaView,SingleSubCategoryView,SingleCategoryView,SingleDuaView

urlpatterns = [

       path('',CategoryView.as_view(), name='category-list'),
       path('single-category/<int:id>/',SingleCategoryView.as_view(), name='single-category'),
       path('sub-category/',SubCategoryView.as_view(), name='sub-category-list'),
       path('single-sub-category/<int:id>/',SingleSubCategoryView.as_view(), name='single-sub-category'),
       path('dua/',DuaView.as_view(), name='dua-list'),
       path('single-dua/<int:id>/',SingleDuaView.as_view(), name='single-dua'),
]
