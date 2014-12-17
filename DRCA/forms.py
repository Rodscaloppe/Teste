from django.forms import ModelForm
from DRCA import models as m

class formaddcur(ModelForm):
    class Meta:
        model = m.Curso