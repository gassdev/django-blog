from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

User._meta.get_field('email')._unique = True


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # def __init__(self, *args, **kwargs):
    #     super(UserCreationForm, self).__init__(*args, **kwargs)

    #     self.fields['username'].label = "Pseudo"
    #     self.fields['username'].er
    #     self.fields['username'].help_text = "Obligatoire. 150 caractères ou moins. Lettres, chiffres et @ /. / + / - / _ uniquement."


    #     self.fields['email'].label = "Adresse e-mail"


    #     self.fields['password1'].label = "Mot de passe"
    #     self.fields['password1'].help_text = """
    #         <ul>
    #             <li>Votre mot de passe ne peut pas être trop similaire à vos autres informations personnelles.</li>
    #             <li>Votre mot de passe doit contenir au moins 8 caractères.</li>
    #             <li>Votre mot de passe ne peut pas être un mot de passe couramment utilisé.</li>
    #             <li>Votre mot de passe ne peut pas être entièrement numérique.</li>
    #         </ul>
    #     """

    #     self.fields['password2'].label = "Confirmez votre mot de passe"
    #     self.fields['password2'].help_text = "Entrez le même mot de passe que précédemment, pour vérification."

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
