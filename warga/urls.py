from django.urls import path
from .views import WargaListView,WargaDetailView,WargaCreateView,PengaduanListView,PengaduanCreateView,WargaListView, WargaDetailView, WargaCreateView, WargaUpdateView,WargaDeleteView
from . import views


urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('<int:pk>/edit/', WargaUpdateView.as_view(), name='warga-edit'),
    path('<int:pk>/hapus/', WargaDeleteView.as_view(), name='warga-hapus'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),
    path('pengaduan/tambah/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    path('pengaduan/<int:pk>/edit/', views.PengaduanUpdateView.as_view(), name='pengaduan_edit'),
    path('pengaduan/<int:pk>/delete/', views.PengaduanDeleteView.as_view(), name='pengaduan_delete'),
]
