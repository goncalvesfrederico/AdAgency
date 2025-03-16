from django.urls import path
from .views import get_branchs, create_branch, branch_detail

urlpatterns = [
    path('branchs/', get_branchs, name="get_branchs"),
    path('branchs/create/', create_branch, name="create_branch"),
    path('branchs/<int:pk>', branch_detail, name="branch_detail"),
]
