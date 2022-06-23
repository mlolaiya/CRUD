
from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="all"),
    path("create/", views.PostCreateView.as_view(), name="post_create"),
    path("delete/<slug:slug>", views.PostDeleteView.as_view(), name="post_delete"),
    path("update/<slug:slug>", views.PostUpdateView.as_view(), name="post_update"),
    path("read/<slug:slug>", views.PostDetailView.as_view(), name="post_detail"),

]






""" from django.urls import path
from .views import PostListView 
from .views import PostDetailView



urlpatterns = [
    path('', PostListView.as_view(), name='article-list'),
]


urlpatterns = [
    path('', PostDetailView.as_view()),
] """