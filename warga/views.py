from django.shortcuts import render
from django.views.generic import ListView, DetailView   # ✅ tambahkan DetailView
from .models import Warga, Pengaduan


class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga_list'

class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'

class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'pengaduan/pengaduan_list.html'
    context_object_name = 'pengaduan_list'

    