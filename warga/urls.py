from django.urls import path
from .views import WargaListView,WargaDetailView,WargaCreateView,PengaduanListView,PengaduanCreateView


urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
]
