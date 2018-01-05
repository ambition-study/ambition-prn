from django import forms
from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import YES, NOT_APPLICABLE
from edc_form_validators import FormValidator
from edc_constants.constants import DEAD

from ..constants import CONSENT_WITHDRAWAL
from django.conf import settings
from edc_base.utils import convert_php_dateformat


class StudyTerminationConclusionFormValidator(FormValidator):

    patient_history_model = 'ambition_subject.patienthistory'
    death_report_model = 'ambition_prn.deathreport'

    @property
    def death_report_model_cls(self):
        return django_apps.get_model(self.death_report_model)

    @property
    def patient_history_model_cls(self):
        return django_apps.get_model(self.patient_history_model)

    def clean(self):

        try:
            death_report = self.death_report_model_cls.objects.get(
                subject_identifier=self.cleaned_data.get('subject_identifier'))
        except ObjectDoesNotExist:
            if self.cleaned_data.get('termination_reason') == DEAD:
                raise forms.ValidationError({
                    'termination_reason':
                    'Patient is deceased, please complete death report form first.'})
        else:
            if self.cleaned_data.get('death_date'):
                try:
                    self.death_report_model_cls.objects.get(
                        subject_identifier=self.cleaned_data.get(
                            'subject_identifier'),
                        death_datetime__date=self.cleaned_data.get('death_date'))
                except ObjectDoesNotExist:
                    formatted_date = death_report.death_datetime.strftime(
                        convert_php_dateformat(settings.SHORT_DATE_FORMAT))
                    raise forms.ValidationError({
                        'death_date':
                        'Date does not match Death Report. '
                        f'Expected {formatted_date}.'})

        self.required_if(
            YES,
            field='discharged_after_initial_admission',
            field_required='initial_discharge_date')

        self.applicable_if(
            YES,
            field='discharged_after_initial_admission',
            field_applicable='readmission_after_initial_discharge')

        self.required_if(
            YES,
            field='readmission_after_initial_discharge',
            field_required='readmission_date')

        self.required_if(
            DEAD,
            field='termination_reason',
            field_required='death_date')

        self.required_if(
            CONSENT_WITHDRAWAL,
            field='termination_reason',
            field_required='consent_withdrawal_reason')

        self.applicable_if(
            CONSENT_WITHDRAWAL,
            field='termination_reason',
            field_applicable='willing_to_complete_10w')

        self.applicable_if(
            'care_transferred_to_another_institution',
            field='termination_reason',
            field_applicable='willing_to_complete_centre')

        self.required_if_true(
            condition=(
                self.cleaned_data.get('willing_to_complete_10w') == YES
                or self.cleaned_data.get('willing_to_complete_centre') == YES),
            field_required='willing_to_complete_date')

        self.applicable_if(
            'late_exclusion_criteria_met',
            field='termination_reason',
            field_applicable='protocol_exclusion_criterion')

        self.required_if(
            'included_in_error',
            field='termination_reason',
            field_required='included_in_error')

        self.required_if(
            'included_in_error',
            field='termination_reason',
            field_required='included_in_error_date')

        self.validate_other_specify(field='first_line_regimen')

        self.validate_other_specify(field='second_line_regimen')

        self.not_applicable_if(
            NOT_APPLICABLE,
            field='first_line_regimen',
            field_applicable='first_line_choice')

        try:
            patient_history = self.patient_history_model_cls.objects.get(
                subject_visit__subject_identifier=self.cleaned_data.get(
                    'subject_identifier'))
        except ObjectDoesNotExist:
            patient_history = None

        self.required_if_true(
            condition=(
                patient_history
                and (patient_history.first_arv_regimen == NOT_APPLICABLE
                     and self.cleaned_data.get('first_line_regimen') == NOT_APPLICABLE)),
            field_required='arvs_delay_reason')
