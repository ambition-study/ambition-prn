from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_consent.model_mixins import RequiresConsentModelMixin
from edc_visit_schedule.model_mixins import DisenrollmentModelMixin


class DisenrollmentManager(models.Manager):

    def get_by_natural_key(self, subject_identifier,
                           visit_schedule_name, schedule_name):
        return self.get(
            subject_identifier=subject_identifier,
            visit_schedule_name=visit_schedule_name,
            schedule_name=schedule_name)


class Disenrollment(DisenrollmentModelMixin, RequiresConsentModelMixin,
                    BaseUuidModel):

    ADMIN_SITE_NAME = 'ambition_prn_admin'

    objects = DisenrollmentManager()

    history = HistoricalRecords()

    class Meta(DisenrollmentModelMixin.Meta):
        visit_schedule_name = 'visit_schedule.schedule'
        consent_model = 'ambition_subject.subjectconsent'
