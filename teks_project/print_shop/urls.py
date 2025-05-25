from django.urls import path
from . import views

app_name = 'print_shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('blog/', views.PostListView.as_view(), name='blog'),
    path('blog/<int:post_id>/', views.post_detail_by_id, name='post_detail_by_id'),
    path('blog/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('printing/', views.printing, name='printing'),
    path('mailing/', views.mailing, name='mailing'),
    path('marketing/', views.marketing, name='marketing'),
]
