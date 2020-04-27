from django.db import models


# call entry_to_cdr models
class CallEntryToCdrMatched(models.Model):
    objects = models.Manager()
    unique_id = models.FloatField(primary_key=True)
    call_date = models.CharField(max_length=20)
    src = models.CharField(max_length=20)

    def __str__(self):
        template = '{0.unique_id} {0.call_date} {0.src}'
        return template.format(self)


class CallEntryToCdrUnMatched(models.Model):
    objects = models.Manager()
    unique_id = models.FloatField(primary_key=True)

    def __str__(self):
        template = '{0.unique_id}'
        return template.format(self)


# cdr_to_call entry models
class CdrToCallEntryMatched(models.Model):
    objects = models.Manager()
    unique_id = models.FloatField(primary_key=True)
    call_date = models.CharField(max_length=20)
    src = models.CharField(max_length=20)

    def __str__(self):
        template = '{0.unique_id} {0.call_date} {0.src}'
        return template.format(self)


class CdrToCallEntryUnMatched(models.Model):
    objects = models.Manager()
    unique_id = models.FloatField(primary_key=True)
    call_date = models.CharField(max_length=20)
    src = models.CharField(max_length=20)

    def __str__(self):
        template = '{0.unique_id} {0.call_date} {0.src}'
        return template.format(self)


class CallProgress(models.Model):
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

    def __str__(self):
        template = '{0.unique_id} {0.datetime_entry} {0.id_campaign_incoming} {0.id_call_incoming}' \
                   '{0.id_campaign_outgoing} {0.id_call_outgoing} {0.new_status} {0.retry} {0.trunk}' \
                   ' {0.id_agent} {0.duration}'
        return template.format(self)


class CallEntry(models.Model):
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
                   '{0.datetime_end} {0.ce_duration} {0.status} {0.transfer} {0.datetime_entry_queue}' \
                   ' {0.duration_wait} {0.id_campaign} {0.trunk}'
        return template.format(self)


class Cdr(models.Model):
    objects = models.Manager()
    key = models.ForeignKey(CallEntry, on_delete=models.SET_DEFAULT, verbose_name='cdr', default=1)
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
                   '{0.last_app} {0.last_data} {0.cdr_duration} {0.bill_sec} {0.amaflags} {0.disposition}' \
                   '{0.account_code} {0.user_field} {0.recording_file} {0.c_num} {0.c_nam} {0.outbound_cnum}' \
                   '{0.outbound_cnam} {0.dst_cnam} {0.did}'
        return template.format(self)


class CallEntryAndCdr(models.Model):
    objects = models.Manager()
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
                   '{0.last_app} {0.last_data} {0.cdr_duration} {0.bill_sec} {0.amaflags} {0.disposition}' \
                   '{0.account_code} {0.user_field} {0.recording_file} {0.c_num} {0.c_nam} {0.outbound_cnum}' \
                   '{0.outbound_cnam} {0.dst_cnam} {0.did} {0.id_agent} {0.id_queue_call_entry} {0.caller_id}' \
                   '{0.datetime_init} {0.datetime_end} {0.ce_duration} {0.cdr_duration} {0.status} {0.transfer}' \
                   '{0.datetime_entry_queue} {0.duration_wait} {0.id_campaign}'
        return template.format(self)

    class Meta:
        ordering = ['call_date']


class CallEntryAndCdrNotMatched(models.Model):
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
                   '{0.last_app} {0.last_data} {0.cdr_duration} {0.bill_sec} {0.amaflags} {0.disposition}' \
                   '{0.account_code} {0.user_field} {0.recording_file} {0.c_num} {0.c_nam} {0.outbound_cnum}' \
                   '{0.outbound_cnam} {0.dst_cnam} {0.did} {0.id_agent} {0.id_queue_call_entry} {0.caller_id}' \
                   '{0.datetime_init} {0.datetime_end} {0.ce_duration} {0.cdr_duration} {0.status} {0.transfer}' \
                   '{0.datetime_entry_queue} {0.duration_wait} {0.id_campaign}'
        return template.format(self)


class CdrAndCallEntryNotMatched(models.Model):
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
                   '{0.last_app} {0.last_data} {0.cdr_duration} {0.bill_sec} {0.amaflags} {0.disposition}' \
                   '{0.account_code} {0.user_field} {0.recording_file} {0.c_num} {0.c_nam} {0.outbound_cnum}' \
                   '{0.outbound_cnam} {0.dst_cnam} {0.did} {0.id_agent} {0.id_queue_call_entry} {0.caller_id}' \
                   '{0.datetime_init} {0.datetime_end} {0.ce_duration} {0.cdr_duration} {0.status} {0.transfer}' \
                   '{0.datetime_entry_queue} {0.duration_wait} {0.id_campaign}'
        return template.format(self)


class Logs(models.Model):
    objects = models.Manager()
    start_date = models.CharField(max_length=20, null=True)
    end_date = models.CharField(max_length=20, null=True)
    file = models.CharField(max_length=20, null=True)
    server = models.CharField(max_length=20, null=True)


class CdrLifestyle(models.Model):
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


class BreakReport(models.Model):
    objects = models.Manager()
    date = models.DateTimeField(null=True, blank=True)
    no_agent = models.IntegerField(blank=True)
    agent_name = models.IntegerField(blank=True)
    hold = models.TimeField(blank=True)
    tea_break = models.TimeField(blank=True)
    lunch_break = models.TimeField(blank=True)
    manual_dial_break = models.TimeField(blank=True)
    auxillary_break = models.TimeField(blank=True)
    total = models.TimeField(blank=True)

    def __str__(self):
        template = '{0.no_agent} {0.agent_name} {0.hold} {0.tea_break} {0.lunch_break} {0.manual_dial_break}' \
                   ' {0.auxillary_break} {0.total}'
        return template.format(self)


class LoginLogout(models.Model):
    objects = models.Manager()
    agent = models.CharField(max_length=20, null=True)
    date_init = models.DateTimeField(blank=True)
    date_end = models.DateTimeField(blank=True)
    total_login = models.TimeField(blank=True)
    incoming_calls = models.TimeField(blank=True)
    outgoing_calls = models.TimeField(blank=True)
    time_of_calls = models.TimeField(blank=True)
    service_percentage = models.FloatField(blank=True)
    status = models.CharField(max_length=50, null=True)

    def __str__(self):
        template = '{0.agent} {0.date_init} {0.date_end} {0.total_login} {0.incoming_calls} {0.outgoing_calls}' \
                   ' {0.time_of_calls} {0.service_percentage} {0.status}'
        return template.format(self)


class CdrReport(models.Model):
    objects = models.Manager()
    date = models.DateTimeField(blank=True)
    source = models.CharField(max_length=50, null=True)
    ring_group = models.CharField(max_length=50, null=True)
    destination = models.CharField(max_length=50, null=True)
    src_channel = models.CharField(max_length=100, null=True)
    account_code = models.CharField(max_length=50, null=True)
    dst_channel = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=50, null=True)
    duration = models.CharField(max_length=50, null=True)

    def __str__(self):
        template = '{0.date} {0.source} {0.ring_group} {0.destination} {0.src_channel} {0.account_code}' \
                   ' {0.dst_channel} {0.status} {0.duration}'
        return template.format(self)


class AgentId(models.Model):
    objects = models.Manager()
    agent_name = models.CharField(max_length=20, blank=True)
    agent_id = models.CharField(max_length=20, blank=True)

    def __str__(self):
        template = '{0.agent_name} {0.agent_id}'
        return template.format(self)


# class CueMath(models.Model):
#     objects = models.Manager()
#     date = models.DateTimeField()
#     agent_no = models.CharField(max_length=20, blank=True)
#     agent_name = models.CharField(max_length=20, blank=True)
#     login_time = models.TimeField(blank=True)
#     logout_time = models.TimeField(blank=True)
#     total_log_hrs = models.TimeField(blank=True)
#     no_of_times_logged = models.IntegerField(blank=True)
#     tea_break = models.TimeField(blank=True)
#     lunch_break = models.TimeField(blank=True)
#     auxillary_break = models.TimeField(blank=True)
#     total_break_hrs_per_day = models.TimeField(blank=True)
#     outgoing_short_calls = models.IntegerField(blank=True)
#     incoming_short_calls = models.IntegerField(blank=True)
#     og_answered = models.IntegerField(blank=True)
#     og_no_answered = models.IntegerField(blank=True)
#     og_busy = models.IntegerField(blank=True)
#     og_failed = models.IntegerField(blank=True)
#     ic_answered = models.IntegerField(blank=True)
#     outgoing_call_time = models.TimeField(blank=True)
#     incoming_call_time = models.TimeField(blank=True)
#     talk_time = models.TimeField(blank=True)
#     total_production_hrs = models.TimeField(blank=True)
#
#     def __str__(self):
#         template = '{0.date} {0.agent_no} {0.agent_name} {0.login_time} {0.logout_time} {0.total_log_hrs}' \
#                    '{0.no_of_times_logged} {0.tea_break} {0.lunch_break} {0.auxillary_break} ' \
#                    '{0.total_break_hrs_per_day}' \
#                    '{0.outgoing_short_calls} {0.incoming_short_calls} {0.og_answered} {0.og_no_answered} {0.og_busy} ' \
#                    '{0.og_failed} {0.ic_answered} {0.outgoing_call_time} {0.incoming_call_time} {0.talk_time} ' \
#                    '{0.total_production_hrs}'
#         return template.format(self)
#
#     class Meta:
#         ordering = ['date']
