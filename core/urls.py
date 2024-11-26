from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='Home'),
     path('fashion',views.fashion,name='Fashion'),
      path('food',views.food,name='Food'),
      path('lifestyle',views.lifestyle,name='Lifestyle'),
      path('travel',views.travel,name='Travel'),
      path('vlog',views.vlog,name='Vlog'),
      path('health',views.health,name='Health'),
      path('single',views.single,name='Single'),
      path('blog-author',views.blogAuthor,name='BlogAuthor'),
      path('page_contact',views.page_contact,name='Page_contact'),
]


