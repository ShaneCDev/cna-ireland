from django import forms
from django_recaptcha.fields import ReCaptchaField

class ContactForm(forms.Form):

    class Meta:
        fields = '__all__'

    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    captcha = ReCaptchaField()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            print(type(field_name))
            if field_name != 'captcha':
                field.widget.attrs['class'] = 'border-dark rounded-0'
