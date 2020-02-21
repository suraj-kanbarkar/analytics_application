from django.core.management.base import BaseCommand
from upload_files.models import *
from django.db import connection
from collections import namedtuple


class Command(BaseCommand):
    def handle(self, *args, **options):
        c = 0
        a = 0
        # ce = CALL_ENTRY.objects.all()
        # for i in ce:
        #     matched = False
        #     for j in CDR.objects.all():
        #         if i.unique_id == j.unique_id:
        #             f = CALL_ENTRY_AND_CDR(unique_id=i.unique_id, call_date=j.call_date, cl_id=j.cl_id, src=j.src,
        #                                    dst=j.dst,
        #                                    d_context=j.d_context, channel=j.channel, dst_channel=j.dst_channel,
        #                                    last_app=j.last_app, last_data=j.last_data, cdr_duration=j.duration,
        #                                    bill_sec=j.bill_sec, amaflags=j.amaflags, disposition=j.disposition,
        #                                    account_code=j.account_code, user_field=j.user_field,
        #                                    recording_file=j.recording_file,
        #                                    c_num=j.c_num, c_nam=j.c_nam, outbound_cnum=j.outbound_cnum,
        #                                    outbound_cnam=j.outbound_cnam,
        #                                    dst_cnam=j.dst_cnam, did=j.did, id_agent=i.id_agent,
        #                                    id_queue_call_entry=i.id_queue_call_entry,
        #                                    id_contact=i.id_contact, caller_id=i.caller_id,
        #                                    datetime_init=i.datetime_init,
        #                                    datetime_end=i.datetime_end, ce_duration=i.duration,
        #                                    status=i.status,
        #                                    transfer=i.transfer, datetime_entry_queue=i.datetime_entry_queue,
        #                                    duration_wait=i.duration_wait, id_campaign=i.id_campaign)
        #             c += 1
        #             f.save()
        #             print(f)
        #             matched = True
        #     if not matched:
        #         f = CALL_ENTRY_AND_CDR_NOT_MATCHED(unique_id=i.unique_id, id_agent=i.id_agent,
        #                                            id_queue_call_entry=i.id_queue_call_entry,
        #                                            id_contact=i.id_contact, caller_id=i.caller_id,
        #                                            datetime_init=i.datetime_init,
        #                                            datetime_end=i.datetime_end, ce_duration=i.duration,
        #                                            status=i.status,
        #                                            transfer=i.transfer, datetime_entry_queue=i.datetime_entry_queue,
        #                                            duration_wait=i.duration_wait, id_campaign=i.id_campaign)
        #         c += 1
        #         f.save()
        #         print(f)
        #
        # s = 0
        # for e in CDR.objects.all():
        #     c_matched = False
        #     for f in CALL_ENTRY.objects.all():
        #         if e.unique_id == f.unique_id:
        #             c_matched = True
        #             break
        #     if not c_matched:
        #         f = CDR_AND_CALL_ENTRY_NOT_MATCHED(unique_id=e.unique_id, call_date=e.call_date, cl_id=e.cl_id,
        #                                            src=e.src,
        #                                            dst=e.dst, d_context=e.d_context, channel=e.channel,
        #                                            dst_channel=e.dst_channel,
        #                                            last_app=e.last_app, last_data=e.last_data, cdr_duration=e.duration,
        #                                            bill_sec=e.bill_sec, amaflags=e.amaflags, disposition=e.disposition,
        #                                            account_code=e.account_code, user_field=e.user_field,
        #                                            recording_file=e.recording_file,
        #                                            c_num=e.c_num, c_nam=e.c_nam, outbound_cnum=e.outbound_cnum,
        #                                            outbound_cnam=e.outbound_cnam, dst_cnam=e.dst_cnam, did=e.did)
        #         s += 1
        #         f.save()
        #         print(f)
        # print(s)

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
            cursor.execute("UPDATE `upload_files_call_entry` SET `ce_status` = 1 "
                           "where `upload_files_call_entry`.`unique_id`"
                           "in (SELECT `upload_files_cdr`.`unique_id` FROM `upload_files_cdr`);")
            print("'ce_status' is Successfully inserted in Call Entry")

            print("Please wait... While inserting 'cdr_status' into CDR.")
            cursor.execute("UPDATE `upload_files_cdr` SET `cdr_status` = 1 "
                           "where `upload_files_cdr`.`unique_id` "
                           "in (SELECT `upload_files_call_entry`.`unique_id` FROM `upload_files_call_entry`);")
            print("'cdr_status' is Successfully inserted in CDR")

            print("Please wait... While performing join operation on 'Call Entry And CDR'.")
            cursor.execute("SELECT * FROM `upload_files_call_entry` inner join `upload_files_cdr` "
                           "on (`upload_files_cdr`.`unique_id` = `upload_files_call_entry`.`unique_id`) "
                           "WHERE `upload_files_cdr`.`unique_id` = `upload_files_call_entry`.`unique_id`;")
            print("'Call Entry And CDR' tables are joined Successfully.")

            row = dictfetchall(cursor)
            c = 1
            print("Nwo updating the records into 'Call Entry And CDR table'.")
            for i in row:
                f = CALL_ENTRY_AND_CDR(unique_id=i['unique_id'], call_date=i['call_date'],
                                       cl_id=i['cl_id'], src=i['src'], dst=i['dst'], d_context=i['d_context'],
                                       channel=i['channel'],dst_channel=i['dst_channel'], last_app=i['last_app'],
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
            cursor.execute("INSERT INTO `upload_files_call_entry_and_cdr` (unique_id, ce_id, id_agent,"
                           "id_contact, id_queue_call_entry, caller_id, datetime_init, datetime_end,"
                           "ce_duration, status, transfer, datetime_entry_queue, duration_wait,"
                           "id_campaign)"
                           " SELECT unique_id, ce_id, id_agent, id_contact, id_queue_call_entry, caller_id,"
                           "datetime_init, datetime_end, ce_duration, status, transfer, datetime_entry_queue,"
                           "duration_wait, id_campaign "
                           "FROM `upload_files_call_entry` "
                           "WHERE ce_status = 0;")

            cursor.execute("INSERT INTO `upload_files_call_entry_and_cdr`(`unique_id`, `call_date`, `cl_id`, `src`,"
                           "`dst`, `d_context`, `channel`, `dst_channel`, `last_app`, `last_data`, `cdr_duration`,"
                           "`bill_sec`, `amaflags`, `disposition`, `account_code`, `user_field`, `recording_file`,"
                           "`c_num`, `c_nam`, `outbound_cnum`, `outbound_cnam`, `dst_cnam`,`did`) "
                           "select `unique_id`, `call_date`, `cl_id`, `src`,`dst`, `d_context`, `channel`, "
                           "`dst_channel`, `last_app`, `last_data`, `cdr_duration`, `bill_sec`, `amaflags`,"
                           "`disposition`, `account_code`, `user_field`, `recording_file`, `c_num`, `c_nam`,"
                           "`outbound_cnum`, `outbound_cnam`, `dst_cnam`,`did` "
                           "FROM `upload_files_cdr` WHERE `cdr_status` = 0;")
            print("unmatched records are successfully updated in 'Call Entry And CDR table'.")