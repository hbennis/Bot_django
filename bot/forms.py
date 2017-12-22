from django import forms


class DiscussionForm(forms.Form):
    texte=forms.CharField(label="",widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(DiscussionForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
        self.fields['texte'].widget.attrs['style'] = 'width:400px; height:20px;'
