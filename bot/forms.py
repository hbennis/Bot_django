from django import forms


class StartForm(forms.Form):
    texte=forms.CharField(label="",widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(StartForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
        self.fields['texte'].widget.attrs['style'] = 'width:400px; height:20px;'

    def clean_texte(self):
        texte = self.cleaned_data['texte']
        if texte.lower()!="bonjour":
            raise forms.ValidationError("Vous devez dire Bonjour!")

        return texte

class DiscussionForm(forms.Form):
    texte=forms.CharField(label="",widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(DiscussionForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
        self.fields['texte'].widget.attrs['style'] = 'width:400px; height:20px;'


    #def clean(self):
        #cleaned_data = super(DiscussionForm, self).clean()
        #texte = cleaned_data.get('texte')

        #if texte:  # Est-ce que sujet et message sont valides ?
            #if texte.lower()!="bonjour":
                #raise forms.ValidationError("Dire Bonjour")

        #return cleaned_data