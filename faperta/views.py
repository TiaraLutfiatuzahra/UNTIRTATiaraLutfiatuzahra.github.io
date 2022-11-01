from django.shortcuts import render
from faperta.models import Dosen
from faperta.forms import FormDosen

# Create your views here.
def faperta(request):
    judul = "Akademik"
    S1 = ("Program Studi S-1", "Program Studi S-2")

    konteks = {
        'title' : judul,
        'S1' : S1,
    }
    return render(request, 'indexfaperta.html', konteks)

def tambah_dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            Pesan = "Data berhasil disimpan"

            konteks = {
                'form' : form,
                'pesan' : Pesan,
            }

            return render(request, 'tambah-dosen.html', konteks)
    else:
        form = FormDosen()

        konteks ={
            'form' : form,
        }

    return render(request, 'tambah-dosen.html', konteks)