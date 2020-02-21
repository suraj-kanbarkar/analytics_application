from django.core.management.base import BaseCommand
from upload_files.models import CALLENTRY_TO_CDR_MATCHED, CALLENTRY_TO_CDR_UN_MATCHED, CDR_TO_CALLENTRY_MATCHED,\
    CDR_TO_CALLENTRY_UN_MATCHED, CALL_ENTRY, CALL_PROGRESS, CDR

class Command(BaseCommand):
    def handle(self, *args, **options):
        CALLENTRY_TO_CDR_MATCHED.objects.all().delete()
        CALLENTRY_TO_CDR_UN_MATCHED.objects.all().delete()
        CDR_TO_CALLENTRY_MATCHED.objects.all().delete()
        CDR_TO_CALLENTRY_UN_MATCHED.objects.all().delete()
        CALL_ENTRY.objects.all().delete()
        CALL_PROGRESS.objects.all().delete()
        CDR.objects.all().delete()
        print('deleted')