from django.shortcuts import render

# Create your views here.
def profil(request):
    judul = "Maksud dan tujuan pndirian yayasan ini adalah :"
    S1 = ("Membantu usaha-usaha pemerintah dalam bidang pendidikan umum.", "Mendirikan sekolah-sekolah mulai dari taman kanak-kanak sampai dengan perguruan tinggi, termasuk juga sekolah-sekolah kejuruan.", "Merencanakan dan mengusahakan sarana pendidikan, serta sarana olah raga.")

    konteks = {
        'title' : judul,
        'S1' : S1,
    }
    return render(request, 'indexprofil.html', konteks)