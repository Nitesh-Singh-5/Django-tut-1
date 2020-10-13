from django.urls import path,register_converter
from . import views, converters

register_converter(converters.fourdigityear,'yyyy')


urlpatterns = [
    path('',views.detail, name='home'),
    path('student/<my_id>',views.showdata, name='detail'),
    path('student/<int:my_id>/<int:my_subid>/',views.showsubdata, name='subdetail'),

    path('session/<yyyy:year>/',views.show_details,name='hero')
]
