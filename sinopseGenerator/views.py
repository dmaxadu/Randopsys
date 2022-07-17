from django.shortcuts import render

from .forms import MovieForm

from .generating_sinopsys import convert_vectors, fill_caveirao

from .get_image import get_image_by_sinopsys

def index(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            vector1 = "["
            vector1 += str(form.cleaned_data["Action"]) + ','
            vector1 += str(form.cleaned_data["Adventure"]) + ','
            vector1 += str(form.cleaned_data["Animation"]) + ','
            vector1 += str(form.cleaned_data["Comedy"]) + ','
            vector1 += str(form.cleaned_data["Crime"]) + ','
            vector1 += str(form.cleaned_data["Documentary"]) + ','
            vector1 += str(form.cleaned_data["Drama"]) + ','
            vector1 += str(form.cleaned_data["Family"]) + ','
            vector1 += str(form.cleaned_data["Fantasy"]) + ','
            vector1 += str(form.cleaned_data["History"]) + ','
            vector1 += str(form.cleaned_data["Horror"]) + ','
            vector1 += str(form.cleaned_data["Music"]) + ','
            vector1 += str(form.cleaned_data["Mystery"]) + ','
            vector1 += str(form.cleaned_data["Romance"]) + ','
            vector1 += str(form.cleaned_data["Science_Fiction"]) + ','
            vector1 += str(form.cleaned_data["Thriller"]) + ','
            vector1 += str(form.cleaned_data["TvMovie"]) + ','
            vector1 += str(form.cleaned_data["War"]) + ','
            vector1 += "0]"
            vector = convert_vectors(vector1)
            sinopse = fill_caveirao(vector)
            if form.cleaned_data["checkbox"]:
                image = True
                href = get_image_by_sinopsys(sinopse)
            else:
                image = False
                href = ''
            return render(request, 'resposta.html', {'texto':sinopse, 'image':image, 'href':href})
        else:
            print("Form não é válido")
    else:
        form = MovieForm()
    return render(request, 'index.html', {'form':form})