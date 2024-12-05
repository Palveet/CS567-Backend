from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('profile/', views.profile),
    path('articles/', views.articles),
    path('articles/<int:article_id>/', views.article_detail),
    path('survey/', views.submit_survey),
    path('survey/<int:article_id>/', views.survey_responses),
]
