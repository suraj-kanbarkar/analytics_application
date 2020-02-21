from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
import djqscsv
from django.contrib.sessions.backends.db import SessionStore
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from .models import *


def paginate_query_set(d, page):
    paginator = Paginator(d, 12)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return data


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def validation(request):
    if request.method == 'GET':
        file = request.GET.get('file')

        if file == "callentry not matched":
            return call_entry_not_matched(request)
        elif file == "cdr not matched":
            return cdr_not_matched(request)
        elif file == "call_entry":
            return call_entry(request)
        elif file == "call progress":
            return call_progress(request)
        elif file == "cdr":
            return cdr(request)
        elif file == "callentry and cdr":
            return call_entry_and_cdr(request)


# for call_entry
def call_entry(request):
    start_date = request.GET.get('startdate')
    end_date = request.GET.get('enddate')
    query = request.GET.get('q_c_entry')
    csv = request.GET.get('csv')
    posts_list = CALL_ENTRY.objects.filter(datetime_init__gte=start_date, datetime_init__lte=end_date)
    if csv:
        return djqscsv.render_to_csv_response(posts_list)
    elif query:
        posts_list = CALL_ENTRY.objects.filter(
            Q(unique_id__icontains=query) |
            Q(datetime_init__icontains=query) | Q(status__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    data = paginate_query_set(posts_list, page)
    print(data)
    return render(request, 'call_entry.html', {'items': data})


# for call_progress
def call_progress(request):
    start_date = request.GET.get('startdate')
    end_date = request.GET.get('enddate')
    query = request.GET.get('q_c_progress')
    csv = request.GET.get('csv')
    posts_list = CALL_PROGRESS.objects.filter(datetime_entry__range=(start_date, end_date))
    if csv:
        return djqscsv.render_to_csv_response(posts_list)
    elif query:
        posts_list = CALL_PROGRESS.objects.filter(
            Q(unique_id__icontains=query) |
            Q(datetime_entry__icontains=query) | Q(new_status__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    data = paginate_query_set(posts_list, page)
    return render(request, 'call_progress.html', {'items': data})


def call_entry_and_cdr(request):
    start_date = request.GET.get('startdate')
    end_date = request.GET.get('enddate')
    query = request.GET.get('q_ce_and_cdr')
    csv = request.GET.get('csv')
    posts_list = CALL_ENTRY_AND_CDR.objects.filter(call_date__range=(start_date, end_date))
    if csv:
        return djqscsv.render_to_csv_response(posts_list)
    elif query:
        posts_list = CALL_ENTRY_AND_CDR.objects.filter(
            Q(unique_id__icontains=query) | Q(call_date__icontains=query) |
            Q(datetime_init__icontains=query) | Q(status__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    data = paginate_query_set(posts_list, page)
    return render(request, 'call_entry_and_cdr.html', {'items': data})


# for cdr
def cdr(request):
    start_date = request.GET.get('startdate')
    end_date = request.GET.get('enddate')
    query = request.GET.get('q_cdr')
    csv = request.GET.get('csv')
    posts_list = CDR.objects.filter(call_date__range=(start_date, end_date))
    if csv:
        return djqscsv.render_to_csv_response(posts_list)
    elif query:
        posts_list = CDR.objects.filter(
            Q(unique_id__icontains=query) |
            Q(call_date__icontains=query) | Q(disposition__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    data = paginate_query_set(posts_list, page)
    return render(request, 'cdr.html', {'items': data})


# for call_entry_not_matched
def call_entry_not_matched(request):
    start_date = request.GET.get('startdate')
    end_date = request.GET.get('enddate')
    query = request.GET.get('q_ce_not_matched')
    csv = request.GET.get('csv')
    posts_list = CALL_ENTRY_AND_CDR_NOT_MATCHED.objects.filter(datetime_entry_queue__range=(start_date, end_date))
    if csv:
        return djqscsv.render_to_csv_response(posts_list)
    elif query:
        posts_list = CALL_ENTRY_AND_CDR_NOT_MATCHED.objects.filter(
            Q(unique_id__icontains=query) |
            Q(datetime_entry_queue__icontains=query) | Q(disposition__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    data = paginate_query_set(posts_list, page)
    return render(request, 'callentry_not_matched.html', {'items': data})


# for call_entry_not_matched
def cdr_not_matched(request):
    start_date = request.GET.get('startdate')
    end_date = request.GET.get('enddate')
    query = request.GET.get('q_cdr_not_matched')
    csv = request.GET.get('csv')
    posts_list = CDR_AND_CALL_ENTRY_NOT_MATCHED.objects.filter(call_date__range=(start_date, end_date))
    if csv:
        return djqscsv.render_to_csv_response(posts_list)
    elif query:
        posts_list = CDR_AND_CALL_ENTRY_NOT_MATCHED.objects.filter(
            Q(unique_id__icontains=query) |
            Q(call_date__icontains=query) | Q(disposition__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    data = paginate_query_set(posts_list, page)
    return render(request, 'cdr_not_matched.html', {'items': data})


# converting queryset to csv response
def get_csv(request):
    csv = request.GET.get('get_csv')
    print(csv)
    posts_list = CALLENTRY_TO_CDR_MATCHED.objects.all()
    return djqscsv.render_to_csv_response(posts_list)


def graphs(request):
    return render(request, 'chart.html')


class TABLES:
    def __init__(self):
        self.GET = None

    def call_entry(self):
        posts_list = CALL_ENTRY.objects.all()
        query = self.GET.get('q_c_entry')
        csv = self.GET.get('csv')
        if csv:
            return djqscsv.render_to_csv_response(posts_list)
        if query:
            posts_list = CALL_ENTRY.objects.filter(
                Q(unique_id__icontains=query) |
                Q(datetime_init__icontains=query) | Q(status__icontains=query)
            ).distinct()
        page = self.GET.get('page')
        data = paginate_query_set(posts_list, page)
        return render(self, 'call_entry.html', {'items': data})

    def call_progress(self):
        posts_list = CALL_PROGRESS.objects.all()
        query = self.GET.get('q_c_progress')
        csv = self.GET.get('csv')
        if csv:
            return djqscsv.render_to_csv_response(posts_list)
        if query:
            posts_list = CALL_PROGRESS.objects.filter(
                Q(unique_id__icontains=query) |
                Q(datetime_entry__icontains=query) | Q(new_status__icontains=query)
            ).distinct()
        page = self.GET.get('page')
        data = paginate_query_set(posts_list, page)
        return render(self, 'call_progress.html', {'items': data})

    def cdr(self):
        posts_list = CDR.objects.all()
        query = self.GET.get('q_cdr')
        csv = self.GET.get('csv')
        if csv:
            return djqscsv.render_to_csv_response(posts_list)
        if query:
            posts_list = CDR.objects.filter(
                Q(unique_id__icontains=query) |
                Q(call_date__icontains=query) | Q(disposition__icontains=query)
            ).distinct()
        page = self.GET.get('page')
        data = paginate_query_set(posts_list, page)
        return render(self, 'cdr.html', {'items': data})

    def call_entry_and_cdr(self):
        query = self.GET.get('q_ce_and_cdr')
        posts_list = CALL_ENTRY_AND_CDR.objects.all()
        csv = self.GET.get('csv')
        if csv:
            return djqscsv.render_to_csv_response(posts_list)
        elif query:
            posts_list = CALL_ENTRY_AND_CDR.objects.filter(
                Q(unique_id__icontains=query) | Q(call_date__icontains=query) |
                Q(datetime_init__icontains=query) | Q(status__icontains=query)
            ).distinct()
        page = self.GET.get('page')
        data = paginate_query_set(posts_list, page)
        return render(self, 'call_entry_and_cdr.html', {'items': data})

    def call_entry_not_matched(self):
        query = self.GET.get('q_ce_not_matched')
        posts_list = CALL_ENTRY_AND_CDR_NOT_MATCHED.objects.all()
        csv = self.GET.get('csv')
        if csv:
            return djqscsv.render_to_csv_response(posts_list)
        elif query:
            posts_list = CALL_ENTRY_AND_CDR_NOT_MATCHED.objects.filter(
                Q(unique_id__icontains=query) | Q(datetime_entry_queue__icontains=query) |
                Q(status__icontains=query)
            ).distinct()
        page = self.GET.get('page')
        data = paginate_query_set(posts_list, page)
        return render(self, 'callentry_not_matched.html', {'items': data})

    def cdr_not_matched(self):
        query = self.GET.get('q_cdr_not_matched')
        posts_list = CDR_AND_CALL_ENTRY_NOT_MATCHED.objects.all()
        csv = self.GET.get('csv')
        if csv:
            return djqscsv.render_to_csv_response(posts_list)
        elif query:
            posts_list = CDR_AND_CALL_ENTRY_NOT_MATCHED.objects.filter(
                Q(unique_id__icontains=query) | Q(call_date__icontains=query) |
                Q(cl_id__icontains=query) | Q(disposition__icontains=query)
            ).distinct()
        page = self.GET.get('page')
        data = paginate_query_set(posts_list, page)
        return render(self, 'cdr_not_matched.html', {'items': data})


# getting insights from cdr table
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def index(request):
    _cdr = CDR.objects.all()
    ans = CDR.objects.filter(disposition='ANSWERED')
    no_ans = CDR.objects.filter(disposition='NO ANSWER')
    fail = CDR.objects.filter(disposition='FAILED')
    length_cdr = _cdr.count()
    ans_calls = (ans.count() / length_cdr) * 100
    no_ans_calls = (no_ans.count() / length_cdr) * 100
    failed_calls = (fail.count() / length_cdr) * 100
    less_than_10, less_than_20, less_than_30, greater_than_30 = [], [], [], []
    for i in _cdr:
        if int(i.cdr_duration) <= 10:
            less_than_10.append(i.cdr_duration)
        elif int(i.cdr_duration) <= 20:
            less_than_20.append(i.cdr_duration)
        elif int(i.cdr_duration) <= 30:
            less_than_30.append(i.cdr_duration)
        elif int(i.cdr_duration) > 30:
            greater_than_30.append(i.cdr_duration)
    less_than_10_sec = (len(less_than_10) / length_cdr) * 100
    less_than_20_sec = (len(less_than_20) / length_cdr) * 100
    less_than_30_sec = (len(less_than_30) / length_cdr) * 100
    greater_than_30_sec = (len(greater_than_30) / length_cdr) * 100
    return render(request, 'index.html', {'ans_calls': truncate(ans_calls, 2),
                                          'ans_count': len(ans),
                                          'no_ans_calls': truncate(no_ans_calls, 2),
                                          'no_ans_count': len(no_ans),
                                          'failed_calls': truncate(failed_calls, 2),
                                          'failed_count': len(fail),
                                          'less_than_10_sec': truncate(less_than_10_sec, 2),
                                          'less_than_10_count': len(less_than_10),
                                          'less_than_20_sec': truncate(less_than_20_sec, 2),
                                          'less_than_20_count': len(less_than_20),
                                          'less_than_30_sec': truncate(less_than_30_sec, 2),
                                          'less_than_30_count': len(less_than_30),
                                          'greater_than_30_sec': truncate(greater_than_30_sec, 2),
                                          'greater_than_30_count': len(greater_than_30)})
