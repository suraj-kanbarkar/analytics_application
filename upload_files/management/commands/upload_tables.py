from django.core.management.base import BaseCommand
import csv
from upload_files.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        # upload data to callentry_to_cdr_matched and callentry_to_cdr_un_matched table
        # with open('/home/appdevelopement/PycharmProjects/grassroots/upload_data/media/callentry_to_cdr_matched.csv', 'rt') as csv_file:
        #     reader = csv.DictReader(csv_file, delimiter=',')
        #     for row in reader:
        #         f = CALLENTRY_TO_CDR_MATCHED(unique_id=row['uniqueid'], call_date=row['date'], src=row['src'])
        #         print(f)
        #         f.save()
        #
        # with open('/home/appdevelopement/PycharmProjects/grassroots/upload_data/media/callentry_to_cdr_un_matched.csv', 'rt') as csv_file:
        #     reader = csv.DictReader(csv_file, delimiter=',')
        #     for row in reader:
        #         f = CALLENTRY_TO_CDR_UN_MATCHED(unique_id=row['uniqueid'])
        #         print(f)
        #         f.save()
        #
        # # # upload data to cdr_to_callentry_matched and cdr_to_callentry_un_matched table
        # with open('/home/appdevelopement/PycharmProjects/grassroots/upload_data/media/cdr_to_callentry_matched.csv', 'rt') as csv_file:
        #     reader = csv.DictReader(csv_file, delimiter=',')
        #     for row in reader:
        #         f = CDR_TO_CALLENTRY_MATCHED(unique_id=row['uniqueid'], call_date=row['date'], src=row['src'])
        #         print(f)
        #         f.save()
        #
        # with open('/home/appdevelopement/PycharmProjects/grassroots/upload_data/media/cdr_to_callentry_un_matched.csv', 'rt') as csv_file:
        #     reader = csv.DictReader(csv_file, delimiter=',')
        #     for row in reader:
        #         f = CDR_TO_CALLENTRY_UN_MATCHED(unique_id=row['uniqueid'], call_date=row['date'], src=row['src'])
        #         print(f)
        #         f.save()

        with open('/home/appdevelopement/PycharmProjects/grassroots/call_analysis/call_data/Lmark-callentry.csv', 'rt') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            for row in reader:
                f = CALL_ENTRY(unique_id=row['uniqueid'], ce_id=row['id'], id_agent=row['id_agent'],
                               id_queue_call_entry=row['id_queue_call_entry'], id_contact=row['id_contact'],
                               caller_id=row['callerid'], datetime_init=row['datetime_init'],
                               datetime_end=row['datetime_end'], ce_duration=row['duration'], status=row['status'],
                               transfer=row['transfer'], datetime_entry_queue=row['datetime_entry_queue'],
                               duration_wait=row['duration_wait'], id_campaign=row['id_campaign'], trunk=row['trunk'])
                f.save()

        # with open('/home/appdevelopement/PycharmProjects/grassroots/upload_data/media/call_progress_ctkt-22-23.csv', 'rt') as csv_file:
        #     reader = csv.DictReader(csv_file, delimiter=',')
        #     for row in reader:
        #         f = CALL_PROGRESS(unique_id=row['uniqueid'], datetime_entry=row['datetime_entry'],
        #                           id_campaign_incoming=row['id_campaign_incoming'], id_call_incoming=row['id_call_incoming'],
        #                           id_campaign_outgoing=row['id_campaign_outgoing'], id_call_outgoing=row['id_call_outgoing'],
        #                           new_status=row['new_status'], retry=row['retry'], trunk=row['trunk'],
        #                           id_agent=row['id_agent'], duration=row['duration'])
        #         print(f)
        #         f.save()

        # with open('/home/appdevelopement/PycharmProjects/grassroots/call_analysis/call_data/Lmark-CDR.csv', 'rt') as csv_file:
        #     reader = csv.DictReader(csv_file, delimiter=',')
        #     for row in reader:
        #         f = CDR(unique_id=row['uniqueid'], call_date=row['calldate'], cl_id=row['clid'], src=row['src'],
        #                 dst=row['dst'], d_context=row['dcontext'], channel=row['channel'], dst_channel=row['dstchannel'],
        #                 last_app=row['lastapp'], last_data=row['lastdata'], cdr_duration=row['duration'],
        #                 bill_sec=row['billsec'], disposition=row['disposition'], amaflags=row['amaflags'],
        #                 account_code=row['accountcode'], user_field=row['userfield'], recording_file=row['recordingfile'],
        #                 c_num=row['cnum'], c_nam=row['cnam'], outbound_cnum=row['outbound_cnum'],
        #                 outbound_cnam=row['outbound_cnam'], dst_cnam=row['dst_cnam'], did=row['did'])
        #         f.save()