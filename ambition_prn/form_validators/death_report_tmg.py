from django import forms
from edc_constants.constants import OTHER, CLOSED, NO, YES
from edc_form_validators import FormValidator

from ..constants import TUBERCULOSIS


class DeathReportTmgFormValidator(FormValidator):

    def clean(self):

        self.required_if(
            CLOSED, field='report_status',
            field_required='cause_of_death',
            inverse=False)

        self.validate_other_specify(
            field='cause_of_death',
            other_specify_field='cause_of_death_other',
            other_stored_value=OTHER)

        if self.cleaned_data.get('cause_of_death'):
            if (self.cleaned_data.get('cause_of_death_agreed') == NO
                    and self.instance.death_report.cause_of_death == self.cleaned_data.get(
                        'cause_of_death')):
                raise forms.ValidationError({
                    'cause_of_death_agreed':
                    ('Cause of death reported by the study doctor matches '
                     'your assessment.')})
            elif (self.cleaned_data.get('cause_of_death_agreed') == YES
                    and self.instance.death_report.cause_of_death != self.cleaned_data.get(
                        'cause_of_death')):
                raise forms.ValidationError({
                    'cause_of_death_agreed':
                    ('Cause of death reported by the study doctor '
                     'does not match your assessment.')})

        self.required_if(
            CLOSED, field='report_status',
            field_required='cause_of_death_agreed',
            inverse=False)

        self.required_if(
            NO, field='cause_of_death_agreed',
            field_required='narrative',
            inverse=False)

        self.applicable_if(
            TUBERCULOSIS,
            field='cause_of_death',
            field_applicable='tb_site')

        self.required_if(
            CLOSED, field='report_status',
            field_required='report_closed_datetime')