from registration.forms import RegistrationForm
from localflavor.us.models import PhoneNumberField

class MyRegistrationForm(RegistrationForm):
    phone = PhoneNumberField()

    class Meta:
        model = UserProfile
        widgets = {
                'phone' : forms.TextInput(attrs = {'placeholder': 'xxxxxxxxxx'}),
                }
    
    def save(self, *args, **kwargs):
        new_user = super(MyRegistrationForm, self).save(*args, **kwargs)


        #create a new profile for this user with his information
        UserProfile(user = new_user, phone = phone).save()

        #return the User model
        return new_user
