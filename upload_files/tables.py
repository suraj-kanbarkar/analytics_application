import django_tables2 as tables
from .models import CALLENTRY_TO_CDR_MATCHED, CALLENTRY_TO_CDR_UN_MATCHED, CDR_TO_CALLENTRY_MATCHED, \
    CDR_TO_CALLENTRY_UN_MATCHED, CALL_ENTRY, CALL_PROGRESS, CDR


class SimpleTable(tables.Table):
    class Meta:
        model = CALLENTRY_TO_CDR_MATCHED
