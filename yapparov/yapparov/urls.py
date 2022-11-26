from damir import views
from django.urls import path, include

post_patterns = [
    path("",views.post),
    path("last",views.last),
    path("popular",views.popular),
    path("like",views.like),
    path("coment",views.coment),
    path("error",views.error),
]

urlpatterns = [
    path('', views.index),
    path("post/",include(post_patterns)),
    path("post/<int:id>/", include(post_patterns)),
    path("user/",views.user),
    path("about/", views.about),
    path('contacts/',views.contacts),
    path("access/<str:name>/<str:password>",views.access),
    path("access/<str:name>",views.access),
    path("json",views.json),
    path("set",views.set),
    path("get",views.get),
]
