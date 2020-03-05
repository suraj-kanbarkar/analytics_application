from django.db import models


# callentry_to_cdr models
class CALLENTRY_TO_CDR_MATCHED(models.Model):
    objects = models.Manager()
    unique_id = models.FloatField(primary_key=True)
    call_date = models.CharField(max_length=20)
    src = models.CharField(max_length=20)

    def __str__(self):
        template = '{0.unique_id} {0.call_date} {0.src}'
        return template.format(self)


class CALLENTRY_TO_CDR_UN_MATCHED(models.Model):
    objects = models.Manager()
    unique_id = models.FloatField(primary_key=True)

    def __str__(self):
        template = '{0.unique_id}'
        return template.format(self)


# cdr_to_callentry models
class CDR_TO_CALLENTRY_MATCHED(models.Model):
    objects = models.Manager()
    unique_id = models.FloatField(primary_key=True)
    call_date = models.CharField(max_length=20)
    src = models.CharField(max_length=20)

    def __str__(self):
        template = '{0.unique_id} {0.call_date} {0.src}'
        return template.format(self)


class CDR_TO_CALLENTRY_UN_MATCHED(models.Model):
    objects = models.Manager()
    unique_id = models.FloatField(primary_key=True)
    call_date = models.CharField(max_length=20)
    src = models.CharField(max_length=20)

    def __str__(self):
        template = '{0.unique_id} {0.call_date} {0.src}'
        return template.format(self)


class CALL_PROGRESS(models.Model):
    objects = models.Manager()
    unique_id = models.FloatField(primary_key=True)
    datetime_entry = models.CharField(max_length=20)
    id_campaign_incoming = models.CharField(max_length=5)
    id_call_incoming = models.CharField(max_length=15)
    id_campaign_outgoing = models.CharField(max_length=20)
    id_call_outgoing = models.CharField(max_length=20)
    new_status = models.CharField(max_length=15)
    retry = models.CharField(max_length=2)
    trunk = models.CharField(max_length=20)
    id_agent = models.CharField(max_length=5)
    duration = models.CharField(max_length=6)

    # class BigintField(models.Model):
    #     def db_type(self):
    #         return 'BIGINT'

    def __str__(self):
        template = '{0.unique_id} {0.datetime_entry} {0.id_campaign_incoming} {0.id_call_incoming} {0.id_campaign_outgoing}' \
                   '{0.id_call_outgoing} {0.new_status} {0.retry} {0.trunk} {0.id_agent} {0.duration}'
        return template.format(self)


class CALL_ENTRY(models.Model):
    objects = models.Manager()
    ce_id = models.CharField(max_length=20, null=True)
    unique_id = models.CharField(max_length=20, null=True)
    id_agent = models.CharField(max_length=12)
    id_queue_call_entry = models.CharField(max_length=2)
    id_contact = models.CharField(max_length=5)
    caller_id = models.CharField(max_length=100)
    datetime_init = models.CharField(max_length=30)
    datetime_end = models.CharField(max_length=30)
    ce_duration = models.CharField(max_length=6)
    status = models.CharField(max_length=12)
    transfer = models.CharField(max_length=5)
    datetime_entry_queue = models.CharField(max_length=20)
    duration_wait = models.CharField(max_length=5)
    id_campaign = models.CharField(max_length=5)
    trunk = models.CharField(max_length=20)
    ce_status = models.CharField(max_length=20, default=0)

    def __str__(self):
        template = '{0.unique_id} {0.id_agent} {0.id_queue_call_entry} {0.id_contact} {0.caller_id} {0.datetime_init}' \
                   '{0.datetime_end} {0.ce_duration} {0.status} {0.transfer} {0.datetime_entry_queue} {0.duration_wait}' \
                   '{0.id_campaign} {0.trunk}'
        return template.format(self)


class CDR(models.Model):
    objects = models.Manager()
    key = models.ForeignKey(CALL_ENTRY, on_delete=models.SET_DEFAULT, verbose_name='cdr', default=1)
    unique_id = models.CharField(max_length=20, null=True)
    call_date = models.CharField(max_length=20)
    cl_id = models.CharField(max_length=1406)
    src = models.CharField(max_length=15)
    dst = models.CharField(max_length=30)
    d_context = models.CharField(max_length=30)
    channel = models.CharField(max_length=30)
    dst_channel = models.CharField(max_length=80)
    last_app = models.CharField(max_length=100)
    last_data = models.CharField(max_length=100)
    cdr_duration = models.CharField(max_length=6)
    bill_sec = models.CharField(max_length=6)
    amaflags = models.CharField(max_length=2)
    disposition = models.CharField(max_length=12)
    account_code = models.CharField(max_length=12)
    user_field = models.CharField(max_length=12)
    recording_file = models.CharField(max_length=100)
    c_num = models.CharField(max_length=20, null=True, blank=True, default='NULL')
    c_nam = models.CharField(max_length=1406, null=True, blank=True, default='NULL')
    outbound_cnum = models.CharField(max_length=20)
    outbound_cnam = models.CharField(max_length=20)
    dst_cnam = models.CharField(max_length=20)
    did = models.CharField(max_length=20)
    cdr_status = models.CharField(max_length=20, default=0)


    def __str__(self):
        template = '{0.unique_id} {0.call_date} {0.cl_id} {0.src} {0.dst} {0.d_context} {0.channel} {0.dst_channel}' \
                   '{0.last_app} {0.last_data} {0.cdr_duration} {0.bill_sec} {0.amaflags} {0.disposition} {0.account_code}' \
                   '{0.user_field} {0.recording_file} {0.c_num} {0.c_nam} {0.outbound_cnum} {0.outbound_cnam}' \
                   '{0.dst_cnam} {0.did}'
        return template.format(self)


class CALL_ENTRY_AND_CDR(models.Model):
    objects = models.Manager()
    # ce_cdr_fk = models.ForeignKey(CDR, on_delete=models.SET_DEFAULT, verbose_name='call_entry_and_cdr', default=1)
    unique_id = models.CharField(max_length=200, null=True)
    call_date = models.CharField(max_length=100, null=True)
    cl_id = models.CharField(max_length=1406, null=True)
    src = models.CharField(max_length=15, null=True)
    dst = models.CharField(max_length=100, null=True)
    d_context = models.CharField(max_length=30, null=True)
    channel = models.CharField(max_length=30, null=True)
    dst_channel = models.CharField(max_length=30, null=True)
    last_app = models.CharField(max_length=100, null=True)
    last_data = models.CharField(max_length=100, null=True)
    cdr_duration = models.CharField(max_length=20, null=True)
    ce_duration = models.CharField(max_length=20, null=True)
    bill_sec = models.CharField(max_length=20, null=True)
    amaflags = models.CharField(max_length=20, null=True)
    disposition = models.CharField(max_length=20, null=True)
    account_code = models.CharField(max_length=100, null=True)
    user_field = models.CharField(max_length=100, null=True)
    recording_file = models.CharField(max_length=100, null=True)
    c_num = models.CharField(max_length=100, null=True, blank=True, default='NULL')
    c_nam = models.CharField(max_length=1406, null=True, blank=True, default='NULL')
    outbound_cnum = models.CharField(max_length=100, null=True)
    outbound_cnam = models.CharField(max_length=100, null=True)
    dst_cnam = models.CharField(max_length=100, null=True)
    did = models.CharField(max_length=100, null=True)
    ce_id = models.CharField(max_length=20, null=True)
    id_agent = models.CharField(max_length=100, null=True)
    id_contact = models.CharField(max_length=100, null=True)
    id_queue_call_entry = models.CharField(max_length=100, null=True)
    caller_id = models.CharField(max_length=100, null=True)
    datetime_init = models.CharField(max_length=100, null=True)
    datetime_end = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=100, null=True)
    transfer = models.CharField(max_length=100, null=True)
    datetime_entry_queue = models.CharField(max_length=100, null=True)
    duration_wait = models.CharField(max_length=100, null=True)
    id_campaign = models.CharField(max_length=100, null=True)

    def __str__(self):
        template = '{0.unique_id} {0.call_date} {0.cl_id} {0.src} {0.dst} {0.d_context} {0.channel} {0.dst_channel}' \
                   '{0.last_app} {0.last_data} {0.cdr_duration} {0.bill_sec} {0.amaflags} {0.disposition} {0.account_code}' \
                   '{0.user_field} {0.recording_file} {0.c_num} {0.c_nam} {0.outbound_cnum} {0.outbound_cnam}' \
                   '{0.dst_cnam} {0.did} {0.id_agent} {0.id_queue_call_entry} {0.caller_id} {0.datetime_init} ' \
                   '{0.datetime_end} {0.ce_duration} {0.cdr_duration} {0.status} {0.transfer} {0.datetime_entry_queue}' \
                   '{0.duration_wait} {0.id_campaign}'
        return template.format(self)

    class Meta:
        ordering = ['call_date']


class CALL_ENTRY_AND_CDR_NOT_MATCHED(models.Model):
    objects = models.Manager()
    unique_id = models.FloatField(primary_key=True)
    call_date = models.CharField(max_length=20)
    cl_id = models.CharField(max_length=1406)
    src = models.CharField(max_length=15)
    dst = models.CharField(max_length=15)
    d_context = models.CharField(max_length=30)
    channel = models.CharField(max_length=30)
    dst_channel = models.CharField(max_length=30)
    last_app = models.CharField(max_length=10)
    last_data = models.CharField(max_length=30)
    cdr_duration = models.CharField(max_length=6)
    ce_duration = models.CharField(max_length=6)
    bill_sec = models.CharField(max_length=6)
    amaflags = models.CharField(max_length=100)
    disposition = models.CharField(max_length=12)
    account_code = models.CharField(max_length=12)
    user_field = models.CharField(max_length=12)
    recording_file = models.CharField(max_length=100)
    c_num = models.CharField(max_length=20, null=True, blank=True, default='NULL')
    c_nam = models.CharField(max_length=1406, null=True, blank=True, default='NULL')
    outbound_cnum = models.CharField(max_length=20)
    outbound_cnam = models.CharField(max_length=20)
    dst_cnam = models.CharField(max_length=20)
    did = models.CharField(max_length=20)
    ce_id = models.CharField(max_length=20, null=True)
    id_agent = models.CharField(max_length=10)
    id_contact = models.CharField(max_length=5)
    id_queue_call_entry = models.CharField(max_length=2)
    caller_id = models.CharField(max_length=100)
    datetime_init = models.CharField(max_length=30)
    datetime_end = models.CharField(max_length=20)
    status = models.CharField(max_length=12)
    transfer = models.CharField(max_length=5)
    datetime_entry_queue = models.CharField(max_length=20)
    duration_wait = models.CharField(max_length=5)
    id_campaign = models.CharField(max_length=5)

    def __str__(self):
        template = '{0.unique_id} {0.call_date} {0.cl_id} {0.src} {0.dst} {0.d_context} {0.channel} {0.dst_channel}' \
                   '{0.last_app} {0.last_data} {0.cdr_duration} {0.bill_sec} {0.amaflags} {0.disposition} {0.account_code}' \
                   '{0.user_field} {0.recording_file} {0.c_num} {0.c_nam} {0.outbound_cnum} {0.outbound_cnam}' \
                   '{0.dst_cnam} {0.did} {0.id_agent} {0.id_queue_call_entry} {0.caller_id} {0.datetime_init} ' \
                   '{0.datetime_end} {0.ce_duration} {0.cdr_duration} {0.status} {0.transfer} {0.datetime_entry_queue}' \
                   '{0.duration_wait} {0.id_campaign}'
        return template.format(self)


class CDR_AND_CALL_ENTRY_NOT_MATCHED(models.Model):
    objects = models.Manager()
    unique_id = models.FloatField(primary_key=True)
    call_date = models.CharField(max_length=20)
    cl_id = models.CharField(max_length=1406)
    src = models.CharField(max_length=15)
    dst = models.CharField(max_length=15)
    d_context = models.CharField(max_length=30)
    channel = models.CharField(max_length=30)
    dst_channel = models.CharField(max_length=30)
    last_app = models.CharField(max_length=10)
    last_data = models.CharField(max_length=30)
    cdr_duration = models.CharField(max_length=6)
    ce_duration = models.CharField(max_length=6)
    bill_sec = models.CharField(max_length=6)
    amaflags = models.CharField(max_length=100)
    disposition = models.CharField(max_length=12)
    account_code = models.CharField(max_length=12)
    user_field = models.CharField(max_length=12)
    recording_file = models.CharField(max_length=100)
    c_num = models.CharField(max_length=20, null=True, blank=True, default='NULL')
    c_nam = models.CharField(max_length=1406, null=True, blank=True, default='NULL')
    outbound_cnum = models.CharField(max_length=20)
    outbound_cnam = models.CharField(max_length=20)
    dst_cnam = models.CharField(max_length=20)
    did = models.CharField(max_length=20)
    id_agent = models.CharField(max_length=10)
    id_contact = models.CharField(max_length=5)
    id_queue_call_entry = models.CharField(max_length=100)
    caller_id = models.CharField(max_length=100)
    datetime_init = models.CharField(max_length=30)
    datetime_end = models.CharField(max_length=20)
    status = models.CharField(max_length=12)
    transfer = models.CharField(max_length=5)
    datetime_entry_queue = models.CharField(max_length=20)
    duration_wait = models.CharField(max_length=5)
    id_campaign = models.CharField(max_length=5)

    def __str__(self):
        template = '{0.unique_id} {0.call_date} {0.cl_id} {0.src} {0.dst} {0.d_context} {0.channel} {0.dst_channel}' \
                   '{0.last_app} {0.last_data} {0.cdr_duration} {0.bill_sec} {0.amaflags} {0.disposition} {0.account_code}' \
                   '{0.user_field} {0.recording_file} {0.c_num} {0.c_nam} {0.outbound_cnum} {0.outbound_cnam}' \
                   '{0.dst_cnam} {0.did} {0.id_agent} {0.id_queue_call_entry} {0.caller_id} {0.datetime_init} ' \
                   '{0.datetime_end} {0.ce_duration} {0.cdr_duration} {0.status} {0.transfer} {0.datetime_entry_queue}' \
                   '{0.duration_wait} {0.id_campaign}'
        return template.format(self)


class Logs(models.Model):
    objects = models.Manager()
    start_date = models.CharField(max_length=20, null=True)
    end_date = models.CharField(max_length=20, null=True)
    file = models.CharField(max_length=20, null=True)
    server = models.CharField(max_length=20, null=True)


class CDR_LIFESTYLE(models.Model):
    objects = models.Manager()
    S_No = models.CharField(max_length=50, null=True)
    TFN = models.CharField(max_length=50, null=True)
    Campaign = models.CharField(max_length=50, null=True)
    PBX_Entry_Time = models.CharField(max_length=50, null=True)
    Queue_Entry_Time = models.CharField(max_length=100, default='0000-00-00 00:0-:00')
    Call_Start_Time = models.CharField(max_length=50, null=True)
    Call_End_Time = models.CharField(max_length=50, null=True)
    Source = models.CharField(max_length=50, null=True)
    Destination = models.CharField(max_length=50, null=True)
    IVR_Time = models.CharField(max_length=50, null=True)
    Talk_Time = models.CharField(max_length=50, null=True)
    Queue_Wait_Time = models.CharField(max_length=50, null=True)
    Status = models.CharField(max_length=50, null=True)
    Transfer_Number = models.CharField(max_length=50, null=True)
    PBX_Unqiue_ID = models.CharField(max_length=50, null=True)

    def __str__(self):
        template = '{0.S_No} {0.TFN} {0.Campaign} {0.PBX_Entry_Time} {0.Queue_Entry_Time} {0.Call_Start_Time}' \
                   ' {0.Call_End_Time} {0.Source} {0.Destination} {0.IVR_Time} {0.Talk_Time} {0.Queue_Wait_Time}' \
                   ' {0.Status} {0.Transfer_Number} {0.PBX_Unqiue_ID}'
        return template.format(self)