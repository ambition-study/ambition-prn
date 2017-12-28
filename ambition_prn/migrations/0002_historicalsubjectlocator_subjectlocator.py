# Generated by Django 2.0 on 2017-12-27 08:39

import _socket
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_crypto_fields.fields.encrypted_char_field
import django_crypto_fields.fields.encrypted_text_field
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.model_validators.phone
import edc_base.utils


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ambition_prn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalSubjectLocator',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('subject_identifier', models.CharField(db_index=True, max_length=50, verbose_name='Subject Identifier')),
                ('action_identifier', models.CharField(max_length=25, null=True)),
                ('consent_version', models.CharField(default='?', editable=False, max_length=10)),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow)),
                ('mail_address', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=500, null=True, verbose_name='Mailing address ')),
                ('physical_address', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=500, null=True, verbose_name='Physical address with detailed description')),
                ('may_follow_up', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Has the participant given his/her permission for study staff to call him/her for follow-up purposes during the study?')),
                ('may_sms_follow_up', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='Has the participant given his/her permission for study staff to SMS him/her for follow-up purposes during the study?')),
                ('subject_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number')),
                ('subject_cell_alt', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number (alternate)')),
                ('subject_phone', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone')),
                ('subject_phone_alt', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone (alternate)')),
                ('may_call_work', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Doesnt_work', "Doesn't work")], max_length=25, verbose_name='Has the participant given his/her permission for study staff to contact him/her at work for follow up purposes during the study?')),
                ('subject_work_place', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=250, null=True, verbose_name='Name and location of work place')),
                ('subject_work_phone', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Work contact number ')),
                ('may_contact_someone', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text='For example a partner, spouse, family member, neighbour ...', max_length=25, verbose_name='Has the participant given his/her permission for study staff to contact anyone else for follow-up purposes during the study?')),
                ('contact_name', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Full names of the contact person')),
                ('contact_rel', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Relationship to participant')),
                ('contact_physical_address', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=500, null=True, verbose_name='Full physical address ')),
                ('contact_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number')),
                ('contact_phone', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone number')),
                ('home_visit_permission', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Has the participant given his/her permission for studystaff to make home visits for follow-up purposes?')),
                ('alt_contact_cell_number', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number (alternate)')),
                ('has_alt_contact', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If we are unable to contact the person indicated above, is there another individual (including next of kin) with whom the study team can get in contact with?')),
                ('alt_contact_name', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text='include first name and surname (Encryption: RSA local)', max_length=71, null=True, verbose_name='Full Name of the responsible person')),
                ('alt_contact_rel', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Relationship to participant')),
                ('alt_contact_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number')),
                ('other_alt_contact_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number (alternate)')),
                ('alt_contact_tel', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone number')),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(primary_key=True, serialize=False)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical ',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='SubjectLocator',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=50, unique=True, verbose_name='Subject Identifier')),
                ('action_identifier', models.CharField(max_length=25, null=True)),
                ('consent_version', models.CharField(default='?', editable=False, max_length=10)),
                ('report_datetime', models.DateTimeField(default=edc_base.utils.get_utcnow)),
                ('mail_address', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=500, null=True, verbose_name='Mailing address ')),
                ('physical_address', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=500, null=True, verbose_name='Physical address with detailed description')),
                ('may_follow_up', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Has the participant given his/her permission for study staff to call him/her for follow-up purposes during the study?')),
                ('may_sms_follow_up', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True, verbose_name='Has the participant given his/her permission for study staff to SMS him/her for follow-up purposes during the study?')),
                ('subject_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number')),
                ('subject_cell_alt', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number (alternate)')),
                ('subject_phone', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone')),
                ('subject_phone_alt', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone (alternate)')),
                ('may_call_work', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Doesnt_work', "Doesn't work")], max_length=25, verbose_name='Has the participant given his/her permission for study staff to contact him/her at work for follow up purposes during the study?')),
                ('subject_work_place', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=250, null=True, verbose_name='Name and location of work place')),
                ('subject_work_phone', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Work contact number ')),
                ('may_contact_someone', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], help_text='For example a partner, spouse, family member, neighbour ...', max_length=25, verbose_name='Has the participant given his/her permission for study staff to contact anyone else for follow-up purposes during the study?')),
                ('contact_name', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Full names of the contact person')),
                ('contact_rel', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Relationship to participant')),
                ('contact_physical_address', django_crypto_fields.fields.encrypted_text_field.EncryptedTextField(blank=True, help_text=' (Encryption: AES local)', max_length=500, null=True, verbose_name='Full physical address ')),
                ('contact_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number')),
                ('contact_phone', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone number')),
                ('home_visit_permission', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, verbose_name='Has the participant given his/her permission for studystaff to make home visits for follow-up purposes?')),
                ('alt_contact_cell_number', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number (alternate)')),
                ('has_alt_contact', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If we are unable to contact the person indicated above, is there another individual (including next of kin) with whom the study team can get in contact with?')),
                ('alt_contact_name', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text='include first name and surname (Encryption: RSA local)', max_length=71, null=True, verbose_name='Full Name of the responsible person')),
                ('alt_contact_rel', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, verbose_name='Relationship to participant')),
                ('alt_contact_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number')),
                ('other_alt_contact_cell', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.CellNumber], verbose_name='Cell number (alternate)')),
                ('alt_contact_tel', django_crypto_fields.fields.encrypted_char_field.EncryptedCharField(blank=True, help_text=' (Encryption: RSA local)', max_length=71, null=True, validators=[edc_base.model_validators.phone.TelephoneNumber], verbose_name='Telephone number')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
