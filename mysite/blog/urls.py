from django.urls import path

from . import views

# Like a namespace for the views inside of this app
app_name = 'blog'

# association of url patters to views, naming them
urlpatterns = [
    path('', views.post_list, name='post_list'),
    # The brackets use a pattern of datatype:fieldname. If none, everything is a string
    path('<int:id>/', views.post_detail, name='post_detail')
]
