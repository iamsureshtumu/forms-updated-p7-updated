from django.urls import path
from myapp import views
app_name="myapp"
urlpatterns=[
    path('topics/',views.topic,name="topic"),
    path('records/',views.records,name="records"),
    path('page5/',views.page5,name='forms'),
    path('display/',views.display,name="display"),
]