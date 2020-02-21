from django.contrib import admin

# Register your models here.

from .models import CALLENTRY_TO_CDR_MATCHED, CALLENTRY_TO_CDR_UN_MATCHED, CDR_TO_CALLENTRY_MATCHED, CDR_TO_CALLENTRY_UN_MATCHED,\
    CALL_ENTRY, CALL_PROGRESS, CDR

admin.site.register(CALLENTRY_TO_CDR_MATCHED)
admin.site.register(CALLENTRY_TO_CDR_UN_MATCHED)
admin.site.register(CDR_TO_CALLENTRY_MATCHED)
admin.site.register(CDR_TO_CALLENTRY_UN_MATCHED)
admin.site.register(CALL_ENTRY)
admin.site.register(CALL_PROGRESS)
admin.site.register(CDR)
