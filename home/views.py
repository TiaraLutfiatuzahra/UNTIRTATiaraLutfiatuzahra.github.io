from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    judul = "MISI :"
    S1 = ("Meningkatkan kualitas, relevansi dan daya saing pendidikan serta lulusan yang unggul, berkarakter dan berdaya saing di kawasan ASEAN.", 
    "Meningkatkan kualitas dan kuantitas penelitian dan pengabdian kepada masyarakat yang inovatif berbasis kebutuhan nyata sesuai perkembangan zaman.", 
    "Meningkatkan daya dukung tatakelola perguruan tinggi yang baik sebagai implementasi dari Integrated Smart and Green (It’S Green) University.")

    konteks = {
        'title' : judul,
        'S1' : S1,
    }
    return render(request, 'indexhome.html', konteks)