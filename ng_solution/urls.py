"""ng_solution URL Configuration
"""
from django.conf.urls import url
from django.contrib import admin
from ng_solution import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movies/$',views.MoviesList.as_view(),name='movies'),
    url(r'^comments/$',views.CommentsList.as_view(),name='comments'),
]
