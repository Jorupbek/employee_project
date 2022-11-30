from django.urls import path

from employee.views import DivisionListView

urlpatterns = [
    path('', DivisionListView.as_view(), name='division-list'),
    path('<slug:division_slug>/', DivisionListView.as_view(), name='employees-by-division'),
]
