from django.urls import path
from .views import HomePage, AboutPage, MySkills, AboutDetailsPage
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('details/<int:pk>/', AboutDetailsPage.as_view(), name='details'),
    path('about/', AboutPage.as_view(), name='about'),
    path('skills/', MySkills.as_view(), name='skills'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)