from django.template.defaulttags import url
from django.urls import path
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
    path('', index, name=''),
    path('about/', about, name='about'),
    path('treningi/', treningi, name='treningi'),
    path('blog/', blog, name='blog'),
    path('show_blog/<int:blog_id>', show_blog, name='show_blog')
]