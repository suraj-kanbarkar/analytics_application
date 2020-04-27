from django.core.management.base import BaseCommand
from upload_files.models import *
from django.db import connection
from collections import namedtuple


class Command(BaseCommand):
    def handle(self, *args, **options):
        def namedtuplefetchall(cursor):
            """Return all rows from a cursor as a namedtuple"""
            desc = cursor.description
            nt_result = namedtuple('Result', [col[0] for col in desc])
            return [nt_result(*row) for row in cursor.fetchall()]

        def dictfetchall(cursor):
            "Return all rows from a cursor as a dict"
            columns = [col[0] for col in cursor.description]
            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        with connection.cursor() as cursor:
            print("Please wait... While inserting 'ce_status' into Call Entry.")
            cursor.execute("UPDATE `upload_files_callentry` SET `ce_status` = 1 "
                           "where `upload_files_callentry`.`unique_id`"
                           "in (SELECT `upload_files_cdr`.`unique_id` FROM `upload_files_cdr`);")
            print("'ce_status' is Successfully inserted in Call Entry")

            print("Please wait... While inserting 'cdr_status' into CDR.")
            cursor.execute("UPDATE `upload_files_cdr` SET `cdr_status` = 1 "
                           "where `upload_files_cdr`.`unique_id` "
                           "in (SELECT `upload_files_callentry`.`unique_id` FROM `upload_files_callentry`);")
            print("'cdr_status' is Successfully inserted in CDR")

            print("Please wait... While performing join operation on 'Call Entry And CDR'.")
            cursor.execute("SELECT * FROM `upload_files_callentry` inner join `upload_files_cdr` "
                           "on (`upload_files_cdr`.`unique_id` = `upload_files_callentry`.`unique_id`) "
                           "WHERE `upload_files_cdr`.`unique_id` = `upload_files_callentry`.`unique_id`;")
            print("'Call Entry And CDR' tables are joined Successfully.")

            row = dictfetchall(cursor)
            c = 1
            print("Nwo updating the records into 'Call Entry And CDR table'.")
            for i in row:
                f = CallEntryAndCdr(unique_id=i['unique_id'], call_date=i['call_date'],
                                    cl_id=i['cl_id'], src=i['src'], dst=i['dst'], d_context=i['d_context'],
                                    channel=i['channel'], dst_channel=i['dst_channel'], last_app=i['last_app'],
                                    last_data=i['last_data'], ce_duration=i['ce_duration'],
                                    cdr_duration=i['cdr_duration'], bill_sec=i['bill_sec'],
                                    amaflags=i['amaflags'], disposition=i['disposition'],
                                    account_code=i['account_code'], user_field=i['user_field'],
                                    recording_file=i['recording_file'], c_num=i['c_num'], c_nam=i['c_nam'],
                                    outbound_cnum=i['outbound_cnum'], outbound_cnam=i['outbound_cnam'],
                                    dst_cnam=i['dst_cnam'], did=i['did'], ce_id=i['ce_id'], id_agent=i['id_agent'],
                                    id_queue_call_entry=i['id_queue_call_entry'], id_contact=i['id_contact'],
                                    caller_id=i['caller_id'], datetime_init=i['datetime_init'],
                                    datetime_end=i['datetime_end'], status=i['status'], transfer=i['transfer'],
                                    datetime_entry_queue=i['datetime_entry_queue'], duration_wait=i['duration_wait'],
                                    id_campaign=i['id_campaign'])

                f.save()
                c += 1
                print(f)
            print("Joined records are successfully updated in 'Call Entry And CDR table'.")

            print("Please wait... while inserting unmatched records into 'Call Entry And CDR table'.")
            cursor.execute("INSERT INTO `upload_files_callentryandcdr` (unique_id, ce_id, id_agent,"
                           "id_contact, id_queue_call_entry, caller_id, datetime_init, datetime_end,"
                           "ce_duration, status, transfer, datetime_entry_queue, duration_wait,"
                           "id_campaign)"
                           " SELECT unique_id, ce_id, id_agent, id_contact, id_queue_call_entry, caller_id,"
                           "datetime_init, datetime_end, ce_duration, status, transfer, datetime_entry_queue,"
                           "duration_wait, id_campaign "
                           "FROM `upload_files_callentry` "
                           "WHERE ce_status = 0;")

            cursor.execute("INSERT INTO `upload_files_callentryandcdr`(`unique_id`, `call_date`, `cl_id`, `src`,"
                           "`dst`, `d_context`, `channel`, `dst_channel`, `last_app`, `last_data`, `cdr_duration`,"
                           "`bill_sec`, `amaflags`, `disposition`, `account_code`, `user_field`, `recording_file`,"
                           "`c_num`, `c_nam`, `outbound_cnum`, `outbound_cnam`, `dst_cnam`,`did`) "
                           "select `unique_id`, `call_date`, `cl_id`, `src`,`dst`, `d_context`, `channel`, "
                           "`dst_channel`, `last_app`, `last_data`, `cdr_duration`, `bill_sec`, `amaflags`,"
                           "`disposition`, `account_code`, `user_field`, `recording_file`, `c_num`, `c_nam`,"
                           "`outbound_cnum`, `outbound_cnam`, `dst_cnam`,`did` "
                           "FROM `upload_files_cdr` WHERE `cdr_status` = 0;")
            print("unmatched records are successfully updated in 'Call Entry And CDR table'.")
