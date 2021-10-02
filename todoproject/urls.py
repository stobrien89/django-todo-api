from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todos.views import TodoViewSet

# create a new router
router = routers.DefaultRouter()
# register viewsets
router.register(r'todos', TodoViewSet)  # register "/todos" route

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
