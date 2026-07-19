from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('models/', views.models_page),
    path('compare/', views.compare_page),
    path('about/', views.about_page),
    path('contact/', views.contact_page),

    path('v8-phantom/', views.v8_phantom, name='v8_phantom'),
    path('x9-dominator/', views.x9_dominator, name='x9_dominator'),
    path('verna/', views.hyundai_verna, name='hyundai_verna'),
    path('land-rover-defender/', views.land_rover_defender, name='land_rover_defender'),

    path('login/', views.login_view),
    path('logout/', views.logout_view),

    path('cars/', views.get_cars),
    path('book/', views.book_test_drive, name='book_test_drive'),

    # VELTRIX AI RECOMMENDATION
    path(
        'recommend/',
        views.recommend_car,
        name='recommend_car'
    ),
]