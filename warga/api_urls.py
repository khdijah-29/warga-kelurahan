from django.urls import path
from .views import WargaListAPIView,WargaDetailAPIView,PengaduanListlAPIView

urlpatterns = [
    path('warga/', WargaListAPIView.as_view(), name='api-warga-list'),
    path('warga/<int:pk>/', WargaDetailAPIView.as_view(), name='api-warga-detail'),
    path ('pengaduan/',PengaduanListlAPIView.as_view(), name='api-pengaduan-list'),

]
