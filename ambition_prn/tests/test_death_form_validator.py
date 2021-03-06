from ambition_rando.tests import AmbitionTestCaseMixin
from dateutil.relativedelta import relativedelta
from django import forms
from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import OTHER
from edc_registration.models import RegisteredSubject

from ..form_validators import DeathReportFormValidator
from ..constants import TUBERCULOSIS


class TestDeathFormValidations(AmbitionTestCaseMixin, TestCase):

    def test_tb_site_missing(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': None}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('tb_site', form_validator._errors)

    def test_tb_site_ok(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': 'meningitis'}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cause_of_death_other_missing(self):
        cleaned_data = {
            'cause_of_death': OTHER,
            'cause_of_death_other': None}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cause_of_death_other', form_validator._errors)

    def test_cause_of_death_other_ok(self):
        cleaned_data = {
            'cause_of_death': OTHER,
            'cause_of_death_other': 'blah'}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cause_of_death_study_doc_opinion_other_none(self):
        cleaned_data = {
            'cause_of_death': OTHER,
            'cause_of_death_other': None}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('cause_of_death_other', form_validator._errors)

    def test_cause_of_death_study_doctor_tb_no_site_specified_invalid(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': None}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('tb_site', form_validator._errors)

    def test_cause_of_death_study_doc_opinion_no(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': 'meningitis'}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cause_of_death_study_tmg1_tb_no_site_specified_invalid(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': None}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('tb_site', form_validator._errors)

    def test_cause_of_death_study_tmg1_tb_site_specified_valid(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': 'meningitis'}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_cause_of_death_study_tmg2_tb_no_site_specified_invalid(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': None}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('tb_site', form_validator._errors)

    def test_cause_of_death_study_tmg2_tb_site_specified_valid(self):
        cleaned_data = {
            'cause_of_death': TUBERCULOSIS,
            'tb_site': 'meningitis'}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

    def test_study_day_of_death(self):

        RegisteredSubject.objects.create(
            subject_identifier='12345',
            randomization_datetime=get_utcnow() - relativedelta(days=3))
        cleaned_data = {
            'subject_identifier': '12345',
            'death_datetime': get_utcnow(),
            'study_day': 4}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')

        cleaned_data = {
            'subject_identifier': '12345',
            'death_datetime': get_utcnow(),
            'study_day': 3}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('study_day', form_validator._errors)

        cleaned_data = {
            'subject_identifier': '12345',
            'death_datetime': get_utcnow() - relativedelta(hours=1),
            'study_day': 3}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, form_validator.validate)
        self.assertIn('study_day', form_validator._errors)

        cleaned_data = {
            'subject_identifier': '12345',
            'death_datetime': get_utcnow() - relativedelta(hours=1),
            'study_day': 4}
        form_validator = DeathReportFormValidator(cleaned_data=cleaned_data)
        try:
            form_validator.validate()
        except forms.ValidationError as e:
            self.fail(f'ValidationError unexpectedly raised. Got{e}')
