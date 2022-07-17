from django import forms
from django.forms import ModelForm
from .models import Movie

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", "History", "Horror", "Music", "Mystery", "Romance", "Science_Fiction", "Thriller", "TvMovie", "War", "checkbox"]
        exclude = ["sinopse", "vector", "Western"]