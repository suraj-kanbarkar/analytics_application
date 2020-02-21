# Generated by Django 3.0.2 on 2020-02-17 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CALL_ENTRY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ce_id', models.CharField(max_length=20, null=True)),
                ('unique_id', models.CharField(max_length=20, null=True)),
                ('id_agent', models.CharField(max_length=12)),
                ('id_queue_call_entry', models.CharField(max_length=2)),
                ('id_contact', models.CharField(max_length=5)),
                ('caller_id', models.CharField(max_length=100)),
                ('datetime_init', models.CharField(max_length=30)),
                ('datetime_end', models.CharField(max_length=30)),
                ('ce_duration', models.CharField(max_length=6)),
                ('status', models.CharField(max_length=12)),
                ('transfer', models.CharField(max_length=5)),
                ('datetime_entry_queue', models.CharField(max_length=20)),
                ('duration_wait', models.CharField(max_length=5)),
                ('id_campaign', models.CharField(max_length=5)),
                ('trunk', models.CharField(max_length=20)),
                ('ce_status', models.CharField(default=0, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CALL_ENTRY_AND_CDR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=200, null=True)),
                ('call_date', models.CharField(max_length=100, null=True)),
                ('cl_id', models.CharField(max_length=1406, null=True)),
                ('src', models.CharField(max_length=15, null=True)),
                ('dst', models.CharField(max_length=100, null=True)),
                ('d_context', models.CharField(max_length=30, null=True)),
                ('channel', models.CharField(max_length=30, null=True)),
                ('dst_channel', models.CharField(max_length=30, null=True)),
                ('last_app', models.CharField(max_length=100, null=True)),
                ('last_data', models.CharField(max_length=100, null=True)),
                ('cdr_duration', models.CharField(max_length=20, null=True)),
                ('ce_duration', models.CharField(max_length=20, null=True)),
                ('bill_sec', models.CharField(max_length=20, null=True)),
                ('amaflags', models.CharField(max_length=20, null=True)),
                ('disposition', models.CharField(max_length=20, null=True)),
                ('account_code', models.CharField(max_length=100, null=True)),
                ('user_field', models.CharField(max_length=100, null=True)),
                ('recording_file', models.CharField(max_length=100, null=True)),
                ('c_num', models.CharField(blank=True, default='NULL', max_length=100, null=True)),
                ('c_nam', models.CharField(blank=True, default='NULL', max_length=1406, null=True)),
                ('outbound_cnum', models.CharField(max_length=100, null=True)),
                ('outbound_cnam', models.CharField(max_length=100, null=True)),
                ('dst_cnam', models.CharField(max_length=100, null=True)),
                ('did', models.CharField(max_length=100, null=True)),
                ('ce_id', models.CharField(max_length=20, null=True)),
                ('id_agent', models.CharField(max_length=100, null=True)),
                ('id_contact', models.CharField(max_length=100, null=True)),
                ('id_queue_call_entry', models.CharField(max_length=100, null=True)),
                ('caller_id', models.CharField(max_length=100, null=True)),
                ('datetime_init', models.CharField(max_length=100, null=True)),
                ('datetime_end', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('transfer', models.CharField(max_length=100, null=True)),
                ('datetime_entry_queue', models.CharField(max_length=100, null=True)),
                ('duration_wait', models.CharField(max_length=100, null=True)),
                ('id_campaign', models.CharField(max_length=100, null=True)),
            ],
            options={
                'ordering': ['call_date'],
            },
        ),
        migrations.CreateModel(
            name='CALL_ENTRY_AND_CDR_NOT_MATCHED',
            fields=[
                ('unique_id', models.FloatField(primary_key=True, serialize=False)),
                ('call_date', models.CharField(max_length=20)),
                ('cl_id', models.CharField(max_length=1406)),
                ('src', models.CharField(max_length=15)),
                ('dst', models.CharField(max_length=15)),
                ('d_context', models.CharField(max_length=30)),
                ('channel', models.CharField(max_length=30)),
                ('dst_channel', models.CharField(max_length=30)),
                ('last_app', models.CharField(max_length=10)),
                ('last_data', models.CharField(max_length=30)),
                ('cdr_duration', models.CharField(max_length=6)),
                ('ce_duration', models.CharField(max_length=6)),
                ('bill_sec', models.CharField(max_length=6)),
                ('amaflags', models.CharField(max_length=100)),
                ('disposition', models.CharField(max_length=12)),
                ('account_code', models.CharField(max_length=12)),
                ('user_field', models.CharField(max_length=12)),
                ('recording_file', models.CharField(max_length=100)),
                ('c_num', models.CharField(blank=True, default='NULL', max_length=20, null=True)),
                ('c_nam', models.CharField(blank=True, default='NULL', max_length=1406, null=True)),
                ('outbound_cnum', models.CharField(max_length=20)),
                ('outbound_cnam', models.CharField(max_length=20)),
                ('dst_cnam', models.CharField(max_length=20)),
                ('did', models.CharField(max_length=20)),
                ('ce_id', models.CharField(max_length=20, null=True)),
                ('id_agent', models.CharField(max_length=10)),
                ('id_contact', models.CharField(max_length=5)),
                ('id_queue_call_entry', models.CharField(max_length=2)),
                ('caller_id', models.CharField(max_length=100)),
                ('datetime_init', models.CharField(max_length=30)),
                ('datetime_end', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=12)),
                ('transfer', models.CharField(max_length=5)),
                ('datetime_entry_queue', models.CharField(max_length=20)),
                ('duration_wait', models.CharField(max_length=5)),
                ('id_campaign', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='CALL_PROGRESS',
            fields=[
                ('unique_id', models.FloatField(primary_key=True, serialize=False)),
                ('datetime_entry', models.CharField(max_length=20)),
                ('id_campaign_incoming', models.CharField(max_length=5)),
                ('id_call_incoming', models.CharField(max_length=15)),
                ('id_campaign_outgoing', models.CharField(max_length=20)),
                ('id_call_outgoing', models.CharField(max_length=20)),
                ('new_status', models.CharField(max_length=15)),
                ('retry', models.CharField(max_length=2)),
                ('trunk', models.CharField(max_length=20)),
                ('id_agent', models.CharField(max_length=5)),
                ('duration', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='CALLENTRY_TO_CDR_MATCHED',
            fields=[
                ('unique_id', models.FloatField(primary_key=True, serialize=False)),
                ('call_date', models.CharField(max_length=20)),
                ('src', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CALLENTRY_TO_CDR_UN_MATCHED',
            fields=[
                ('unique_id', models.FloatField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CDR_AND_CALL_ENTRY_NOT_MATCHED',
            fields=[
                ('unique_id', models.FloatField(primary_key=True, serialize=False)),
                ('call_date', models.CharField(max_length=20)),
                ('cl_id', models.CharField(max_length=1406)),
                ('src', models.CharField(max_length=15)),
                ('dst', models.CharField(max_length=15)),
                ('d_context', models.CharField(max_length=30)),
                ('channel', models.CharField(max_length=30)),
                ('dst_channel', models.CharField(max_length=30)),
                ('last_app', models.CharField(max_length=10)),
                ('last_data', models.CharField(max_length=30)),
                ('cdr_duration', models.CharField(max_length=6)),
                ('ce_duration', models.CharField(max_length=6)),
                ('bill_sec', models.CharField(max_length=6)),
                ('amaflags', models.CharField(max_length=100)),
                ('disposition', models.CharField(max_length=12)),
                ('account_code', models.CharField(max_length=12)),
                ('user_field', models.CharField(max_length=12)),
                ('recording_file', models.CharField(max_length=100)),
                ('c_num', models.CharField(blank=True, default='NULL', max_length=20, null=True)),
                ('c_nam', models.CharField(blank=True, default='NULL', max_length=1406, null=True)),
                ('outbound_cnum', models.CharField(max_length=20)),
                ('outbound_cnam', models.CharField(max_length=20)),
                ('dst_cnam', models.CharField(max_length=20)),
                ('did', models.CharField(max_length=20)),
                ('id_agent', models.CharField(max_length=10)),
                ('id_contact', models.CharField(max_length=5)),
                ('id_queue_call_entry', models.CharField(max_length=100)),
                ('caller_id', models.CharField(max_length=100)),
                ('datetime_init', models.CharField(max_length=30)),
                ('datetime_end', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=12)),
                ('transfer', models.CharField(max_length=5)),
                ('datetime_entry_queue', models.CharField(max_length=20)),
                ('duration_wait', models.CharField(max_length=5)),
                ('id_campaign', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='CDR_TO_CALLENTRY_MATCHED',
            fields=[
                ('unique_id', models.FloatField(primary_key=True, serialize=False)),
                ('call_date', models.CharField(max_length=20)),
                ('src', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CDR_TO_CALLENTRY_UN_MATCHED',
            fields=[
                ('unique_id', models.FloatField(primary_key=True, serialize=False)),
                ('call_date', models.CharField(max_length=20)),
                ('src', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.CharField(max_length=20, null=True)),
                ('end_date', models.CharField(max_length=20, null=True)),
                ('file', models.CharField(max_length=20, null=True)),
                ('server', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CDR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(max_length=20, null=True)),
                ('call_date', models.CharField(max_length=20)),
                ('cl_id', models.CharField(max_length=1406)),
                ('src', models.CharField(max_length=15)),
                ('dst', models.CharField(max_length=30)),
                ('d_context', models.CharField(max_length=30)),
                ('channel', models.CharField(max_length=30)),
                ('dst_channel', models.CharField(max_length=80)),
                ('last_app', models.CharField(max_length=100)),
                ('last_data', models.CharField(max_length=100)),
                ('cdr_duration', models.CharField(max_length=6)),
                ('bill_sec', models.CharField(max_length=6)),
                ('amaflags', models.CharField(max_length=2)),
                ('disposition', models.CharField(max_length=12)),
                ('account_code', models.CharField(max_length=12)),
                ('user_field', models.CharField(max_length=12)),
                ('recording_file', models.CharField(max_length=100)),
                ('c_num', models.CharField(blank=True, default='NULL', max_length=20, null=True)),
                ('c_nam', models.CharField(blank=True, default='NULL', max_length=1406, null=True)),
                ('outbound_cnum', models.CharField(max_length=20)),
                ('outbound_cnam', models.CharField(max_length=20)),
                ('dst_cnam', models.CharField(max_length=20)),
                ('did', models.CharField(max_length=20)),
                ('cdr_status', models.CharField(default=0, max_length=20)),
                ('key', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='upload_files.CALL_ENTRY', verbose_name='cdr')),
            ],
        ),
    ]