from django.contrib import admin
from edc_action_item import action_fieldset
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import ambition_prn_admin
from ..forms import ProtocolDeviationViolationForm
from ..models import ProtocolDeviationViolation
from .modeladmin_mixins import ModelAdminMixin


@admin.register(ProtocolDeviationViolation, site=ambition_prn_admin)
class ProtocolDeviationViolationAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = ProtocolDeviationViolationForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'report_datetime',
                'short_description',
                'report_type',
            )}
         ),
        ('Assessment to confirm violation/deviation', {
            'fields': (
                'safety_impact',
                'safety_impact_details',
                'study_outcomes_impact',
                'study_outcomes_impact_details')},
         ),
        ('Details of protocol violation', {
            'description': ('The following questions are only required if '
                            'this is a protocol violation.'),
            'fields': (
                'violation_datetime',
                'violation_type',
                'violation_type_other',
                'violation_description',
                'violation_reason')}
         ),
        ('Actions taken', {
            'fields': (
                'corrective_action_datetime',
                'corrective_action',
                'preventative_action_datetime',
                'preventative_action',
                'action_required',)}),
        ('Report status', {
            'fields': (
                'report_status',
                'report_closed_datetime')}),
        action_fieldset,
        audit_fieldset_tuple,
    )

    radio_fields = {
        'action_required': admin.VERTICAL,
        'report_status': admin.VERTICAL,
        'report_type': admin.VERTICAL,
        'safety_impact': admin.VERTICAL,
        'study_outcomes_impact': admin.VERTICAL,
        'violation_type': admin.VERTICAL,
    }

    list_display = ('subject_identifier', 'dashboard', 'short_description',
                    'report_datetime', 'status', 'action_required', 'report_type',
                    'tracking_identifier', 'action_identifier', 'user_created')

    list_filter = ('action_required', 'report_status',
                   'report_type')

    search_fields = ('tracking_identifier', 'short_description',
                     'subject_identifier', 'action_identifier')

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        fields = ('tracking_identifier', 'action_identifier') + fields
        if obj:
            fields = fields + ('subject_identifier', )
        return fields

    def status(self, obj=None):
        return obj.report_status.title()
