from blog.sitemaps import PostSitemap
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path


sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    # Adding the blog app urls to the main project
    path('blog/', include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name="django.contrib.sitemaps.views.sitemap"),
]
