from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit

from rsvp import models


class ResponseForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ResponseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-responseForm'
        self.helper.form_method = 'post'
        self.helper.form_action = 'response-create'
        self.helper.layout = Layout(
            Field('name', placeholder="e.g. Johnny B. Goode"),
            Field('guest_count', placeholder="e.g. 2"),
            Field('accommodation_requests', rows=2, placeholder="e.g. Closer parking, wheelchair seating"),
        )
        self.helper.add_input(Submit('submit', 'Send RSVP'))

    class Meta:
        model = models.Response
        fields = ('name', 'guest_count', 'accommodation_requests')
