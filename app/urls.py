from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('howitworks/', views.howitworks, name="howitworks"),
    path('search/', views.search, name="search"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('othercampaign/', views.othercampaign, name="campaign"),
    path('donation_future_purpose/', views.future_purpose, name="future_purpose"),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('gallery/', views.gallery, name="gallery"),

    path('othercampaign/create', views.CampaignCreateView.as_view(), name="create"),
    path('othercampaign/update/<int:pk>', views.CampaignUpdateView.as_view(), name="update"),
    path('othercampaign/delete/<int:pk>', views.CampaignDeleteView.as_view(), name="delete"),

    path('khalti-request/<int:id>/', views.khaltirequest, name='khaltirequest'),
    path('khaltiverify/<int:id>/', views.khaltiverify, name='khaltiverify'),
    path('khaltiverify_future_purpose/', views.khaltiverify_future, name='khaltiverify_future'),
    path('khaltirequest_future_purpose/', views.future_khalti, name='future_khalti')
]