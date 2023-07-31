from django.urls import path

from . import views

app_name = "Home"

urlpatterns = [
    path("", views.home, name='HOME'),
    path("test", views.test_page, name='TEST'),
    path("contact", views.contact_us, name='CONTACT_US'),
    path("about", views.about, name='ABOUT_US'),
    # path("blogs", views.blog, name='BLOGS'),
    # path("test", views.test, name='TEST'),
    # path("mutualfunds", views.mutualfunds, name='SERVICE_MUTUALFUNDS'),
    # path("lumpsum", views.lumpsum, name='SERVICE_LUMPSUM'),
    # path("mediclaim", views.mediclaim, name='SERVICE_MEDICLAIM'),
    # path("terminsurance", views.insurance, name='SERVICE_INSURANCE'),
    # path("videos", views.showvideos, name='videos'),
    # path("blogs/<str:slug>", views.blogpost, name='SERVICE_BLOG'),

]
