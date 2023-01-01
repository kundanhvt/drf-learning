from django.urls import path
from . import views
urlpatterns = [
    path('studinfo/<int:pk>',views.studen_details),
    path('studinfo/',views.student_list),
    path('stucreate/',views.student_create)
]
