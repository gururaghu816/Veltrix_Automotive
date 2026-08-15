from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('models/', views.models_page, name='models'),
    path('compare/', views.compare_page, name='compare'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact_page, name='contact'),

    path('v8-phantom/', views.v8_phantom, name='v8_phantom'),
    path('x9-dominator/', views.x9_dominator, name='x9_dominator'),
    path('verna/', views.hyundai_verna, name='hyundai_verna'),
    path('land-rover-defender/', views.land_rover_defender, name='land_rover_defender'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('cars/', views.get_cars),
    path('book/', views.book_test_drive, name='book_test_drive'),
    path('success/<int:booking_id>/sign/', views.save_signature, name='save_signature'),

    path(
        'recommend/',
        views.recommend_car,
        name='recommend_car'
    ),
]