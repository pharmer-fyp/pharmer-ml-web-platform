from django.urls import path, include
from . import views 
app_name = "pages"

urlpatterns = [ 
    path('', views.home_view, name = 'home_view'),
    path('pages/home', views.home_view, name = 'home_view'),
    path('pages/cropyeild', views.cropyield_view, name = 'cropyield_view'),
    path('pages/cropvalue', views.cropvalue_view, name = 'cropvalue_view'),
    path('pages/temprf', views.temprf_view, name = 'temprf_view'),
    path('pages/predict_temp_rf', views.predict_temp_rf, name = 'predict_temp_rf'),
    path('pages/predict_crop_val', views.predict_crop_val, name = 'predict_crop_val'),
    path('pages/predict_crop_yield', views.predict_crop_yield, name = 'predict_crop_yield'),
]