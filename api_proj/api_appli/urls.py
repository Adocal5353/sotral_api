from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api_appli import views
from .views import credit_account, debit_account

urlpatterns = [
    path('buss/',views.BusList.as_view()),
    path('buss/<int:pk>/', views.BusDetail.as_view()),

    path('lignes/',views.LigneList.as_view()),
    path('lignes/<int:pk>/', views.LigneDetail.as_view()),

    path('sections/',views.SectionList.as_view()),
    path('sections/<int:pk>/', views.SectionDetail.as_view()),

    path('utilisateurs/',views.UtilisateurList.as_view()),
    path('utilisateurs/<int:pk>/', views.UtilisateurDetail.as_view()),

    path('voyagers/',views.VoyageList.as_view()),
    path('voyagers/<int:pk>/', views.VoyageDetail.as_view()),

    path('credit/', credit_account, name='credit_account'),
    path('debit/', debit_account, name='debit_account'),

    path('tarifs/',views.TarifList.as_view()),
    path('tarifs/<int:pk>/', views.TarifDetail.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)
