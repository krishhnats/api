"""
URL configuration for recipemanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views
from rest_framework.authtoken import views as rviews
from recipe.views import Createrev, Detailrev

router = DefaultRouter()
router.register('Recipe',views.RecipeViewSet)
# router.register('Review',views.ReviewViewSet)
router.register('user',views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', rviews.obtain_auth_token),
    path('user_logout', views.user_logout.as_view()),
    path('createreview/', views.Createrev.as_view(), name='create_review'),
    path('detailreview/<int:pk>/', views.Detailrev.as_view(), name='detail_review'),
    path('cuisine_filter/', views.CuisineFilter.as_view(), name='cuisine_filter'),
    path('meal_filter/', views.MealFilter.as_view(), name='meal_filter'),
    path('ingredients_filter/', views.IngreditesFilter.as_view(), name='ingredients_filter'),
]
