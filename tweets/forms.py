from django import forms


class TweetForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'row': 3, 'cols': 50}), max_length=160)
    tweet_file = forms.FileField(required=False)


class SearchForm(forms.Form):
    search = forms.TextInput()
