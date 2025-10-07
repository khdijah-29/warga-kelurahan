from django.shortcuts import render
from django.views.generic import ListView, DetailView   # ✅ tambahkan DetailView
from .models import Warga

# View untuk menampilkan daftar warga
class WargaListView(ListView):
    model = Warga
    # Django otomatis akan mencari template di warga/warga_list.html
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga_list'

class WargaDetailView(DetailView):
    model = Warga
    # Django otomatis akan mencari template di warga/warga_detail.html
    template_name = 'warga/warga_detail.html'
