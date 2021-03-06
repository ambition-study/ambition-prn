from django.db import models
from django.db.models.deletion import PROTECT
from edc_action_item.model_mixins import ActionModelMixin
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel, ReportStatusModelMixin
from edc_base.model_validators.date import datetime_not_future
from edc_base.sites import CurrentSiteManager, SiteModelMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_constants.constants import NOT_APPLICABLE
from edc_protocol.validators import datetime_not_before_study_start

from ..action_items import DEATH_REPORT_TMG_ACTION
from ..choices import CAUSE_OF_DEATH, TB_SITE_DEATH
from .death_report import DeathReport


class DeathReportTmgManager(models.Manager):

    def get_by_natural_key(self, subject_identifier):
        return self.get(death_report__subject_identifier=subject_identifier)


class DeathReportTmg(ActionModelMixin, ReportStatusModelMixin,
                     SiteModelMixin, BaseUuidModel):

    action_name = DEATH_REPORT_TMG_ACTION

    tracking_identifier_prefix = 'DR'

    death_report = models.ForeignKey(DeathReport, on_delete=PROTECT)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        validators=[
            datetime_not_before_study_start,
            datetime_not_future],
        default=get_utcnow)

    cause_of_death = models.CharField(
        verbose_name='Main cause of death',
        max_length=50,
        choices=CAUSE_OF_DEATH,
        blank=True,
        null=True,
        help_text='Main cause of death in the opinion of TMG member')

    cause_of_death_other = models.CharField(
        verbose_name='If "Other" above, please specify',
        max_length=100,
        blank=True,
        null=True)

    cause_of_death_agreed = models.CharField(
        verbose_name='Is the cause of death agreed between study doctor and TMG member?',
        max_length=15,
        choices=YES_NO,
        blank=True,
        null=True,
        help_text='If No, explain in the narrative below')

    tb_site = models.CharField(
        verbose_name='If cause of death is TB, specify site of TB disease',
        max_length=25,
        choices=TB_SITE_DEATH,
        default=NOT_APPLICABLE,
        blank=True)

    narrative = models.TextField(
        verbose_name='Narrative',
        blank=True,
        null=True)

    on_site = CurrentSiteManager()

    objects = DeathReportTmgManager()

    history = HistoricalRecords()

    def __str__(self):
        return str(self.death_report)

    def save(self, *args, **kwargs):
        self.subject_identifier = self.death_report.subject_identifier
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.report_datetime, ) + self.death_report.natural_key()
    natural_key.dependencies = ['ambition_prn.deathreport', 'sites.Site']

    class Meta:
        verbose_name = 'Death Report TMG'
        verbose_name_plural = 'Death Report TMG'
