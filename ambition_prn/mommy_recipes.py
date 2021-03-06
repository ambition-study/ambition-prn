from edc_constants.constants import YES
from faker import Faker
from model_mommy.recipe import Recipe, related

from .models import DeathReport, StudyTerminationConclusion, StudyTerminationConclusionW10
from .models import ProtocolDeviationViolation, DeathReportTmg

fake = Faker()

deathreport = Recipe(
    DeathReport,
    study_day=1,
    death_as_inpatient=YES,
    cause_of_death='art_toxicity',
    cause_of_death_other=None,
    action_identifier=None,
    tracking_identifier=None,
    tb_site='meningitis',
    narrative=(
        'adverse event resulted in death due to cryptococcal meningitis'))

studyterminationconclusion = Recipe(
    StudyTerminationConclusion,
    action_identifier=None,
    tracking_identifier=None)

studyterminationconclusionw10 = Recipe(
    StudyTerminationConclusionW10,
    action_identifier=None,
    tracking_identifier=None)


protocoldeviationviolation = Recipe(
    ProtocolDeviationViolation,
    action_identifier=None,
    tracking_identifier=None)

deathreporttmg = Recipe(
    DeathReportTmg,
    action_identifier=None,
    tracking_identifier=None)
