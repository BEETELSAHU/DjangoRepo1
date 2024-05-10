from django import forms
from testapp.models import Movies

class MoviesForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    movie_name = forms.CharField()
    hero_name = forms.CharField()
    heroien_name = forms.CharField()
    movie_rating = forms.FloatField()
    class Meta:
        model = Movies
        fields = '__all__'
