from django import forms


class TweetForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'row': 3, 'cols': 50}), max_length=160)
    tweet_file = forms.FileField(required=False)
    image = forms.ImageField(required=False)


class SearchForm(forms.Form):
    search = forms.TextInput()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=3)
    password = forms.CharField(min_length=6, max_length=16)
