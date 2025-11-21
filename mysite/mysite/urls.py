from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Adding the blog app urls to the main project
    path('blog/', include('blog.urls', namespace='blog'))
]
