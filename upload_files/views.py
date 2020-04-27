import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core import serializers
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Q
import djqscsv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
import datetime
from upload_files.analysis import dat
from upload_files.cuemath_report import *


# setting pagination for tables
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
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def validation(request):
    if request.method == 'GET':
        file = request.GET.get('file')
        print(file)

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
        elif file == "lifestyle cdr":
            return lifestyle_cdr(request)
        elif file == "cuemath":
            return cuemath_report(request)


# for call_entry
def call_entry(request):
    start_date = request.GET.get('startdate')
    end_dat = request.GET.get('enddate')
    end_date = datetime.datetime.strptime(end_dat, '%Y-%m-%d').date()  # converting str date into datetime format
    end_date += datetime.timedelta(days=1)  # increment date by 1
    print(start_date, end_date)
    query = request.GET.get('q_c_entry')
    csv = request.GET.get('csv')
    posts_list = CallEntry.objects.filter(datetime_init__gte=start_date, datetime_init__lte=end_date)
    if csv:
        return djqscsv.render_to_csv_response(posts_list)
    elif query:
        posts_list = CallEntry.objects.filter(
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
    end_dat = request.GET.get('enddate')
    end_date = datetime.datetime.strptime(end_dat, '%Y-%m-%d').date()  # converting str date into datetime format
    end_date += datetime.timedelta(days=1)  # increment date by 1
    print(start_date, end_date)
    query = request.GET.get('q_c_progress')
    csv = request.GET.get('csv')
    posts_list = CallProgress.objects.filter(datetime_entry__range=(start_date, end_date))
    if csv:
        return djqscsv.render_to_csv_response(posts_list)
    elif query:
        posts_list = CallProgress.objects.filter(
            Q(unique_id__icontains=query) |
            Q(datetime_entry__icontains=query) | Q(new_status__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    data = paginate_query_set(posts_list, page)
    return render(request, 'call_progress.html', {'items': data})


# for call_entry and cdr
def call_entry_and_cdr(request):
    start_date = request.GET.get('startdate')
    end_dat = request.GET.get('enddate')
    end_date = datetime.datetime.strptime(end_dat, '%Y-%m-%d').date()  # converting str date into datetime format
    end_date += datetime.timedelta(days=1)  # increment date by 1
    print(start_date, end_date)
    query = request.GET.get('q_ce_and_cdr')
    csv = request.GET.get('csv')
    posts_list = CallEntryAndCdr.objects.filter(call_date__range=(start_date, end_date))
    if csv:
        return djqscsv.render_to_csv_response(posts_list)
    elif query:
        posts_list = CallEntryAndCdr.objects.filter(
            Q(unique_id__icontains=query) | Q(call_date__icontains=query) |
            Q(datetime_init__icontains=query) | Q(status__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    data = paginate_query_set(posts_list, page)
    return render(request, 'call_entry_and_cdr.html', {'items': data})


# for cdr
def cdr(request):
    start_date = request.GET.get('startdate')
    end_dat = request.GET.get('enddate')
    end_date = datetime.datetime.strptime(end_dat, '%Y-%m-%d').date()  # converting str date into datetime format
    end_date += datetime.timedelta(days=1)  # increment date by 1
    print(start_date, end_date)
    query = request.GET.get('q_cdr')
    csv = request.GET.get('csv')
    posts_list = Cdr.objects.filter(call_date__range=(start_date, end_date))
    if csv:
        return djqscsv.render_to_csv_response(posts_list)
    elif query:
        posts_list = Cdr.objects.filter(
            Q(unique_id__icontains=query) |
            Q(call_date__icontains=query) | Q(disposition__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    data = paginate_query_set(posts_list, page)
    return render(request, 'cdr.html', {'items': data})


# for call_entry_not_matched
def call_entry_not_matched(request):
    start_date = request.GET.get('startdate')
    end_dat = request.GET.get('enddate')
    end_date = datetime.datetime.strptime(end_dat, '%Y-%m-%d').date()  # converting str date into datetime format
    end_date += datetime.timedelta(days=1)  # increment date by 1
    print(start_date, end_date)
    query = request.GET.get('q_ce_not_matched')
    csv = request.GET.get('csv')
    posts_list = CallEntryAndCdrNotMatched.objects.filter(datetime_entry_queue__range=(start_date, end_date))
    if csv:
        return djqscsv.render_to_csv_response(posts_list)
    elif query:
        posts_list = CallEntryAndCdrNotMatched.objects.filter(
            Q(unique_id__icontains=query) |
            Q(datetime_entry_queue__icontains=query) | Q(disposition__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    data = paginate_query_set(posts_list, page)
    return render(request, 'callentry_not_matched.html', {'items': data})


# for call_entry_not_matched
def cdr_not_matched(request):
    start_date = request.GET.get('startdate')
    end_dat = request.GET.get('enddate')
    end_date = datetime.datetime.strptime(end_dat, '%Y-%m-%d').date()  # converting str date into datetime format
    end_date += datetime.timedelta(days=1)  # increment date by 1
    print(start_date, end_date)
    query = request.GET.get('q_cdr_not_matched')
    csv = request.GET.get('csv')
    posts_list = CdrAndCallEntryNotMatched.objects.filter(call_date__range=(start_date, end_date))
    if csv:
        return djqscsv.render_to_csv_response(posts_list)
    elif query:
        posts_list = CdrAndCallEntryNotMatched.objects.filter(
            Q(unique_id__icontains=query) |
            Q(call_date__icontains=query) | Q(disposition__icontains=query)
        ).distinct()
    page = request.GET.get('page')
    data = paginate_query_set(posts_list, page)
    return render(request, 'cdr_not_matched.html', {'items': data})


# lifestyle cdr performance report
def lifestyle_cdr(request):
    s_date = request.GET.get('startdate')
    e_date = request.GET.get('enddate')
    e_date = datetime.datetime.strptime(e_date[:10], '%Y-%m-%d')  # converting str date into datetime format
    s_date = datetime.datetime.strptime(s_date[:10], '%Y-%m-%d')  # converting str date into datetime format
    e_date += datetime.timedelta(days=1)  # increment date by 1
    print(s_date, e_date)
    csv = request.GET.get('csv')
    posts_list = CdrLifestyle.objects.filter(Queue_Entry_Time__range=(s_date, e_date))
    if posts_list:
        posts_list = posts_list.order_by('Queue_Entry_Time')
        data_2 = dat(posts_list)
        if csv:
            return djqscsv.render_to_csv_response(posts_list)
        # data = serializers.serialize('json', data)
        return render(request, 'life_style_cdr.html', {'items_0': data_2[0],
                                                       'items_1': data_2[1],
                                                       'items_2': data_2[2],
                                                       'items_3': data_2[3],
                                                       'items_4': data_2[4],
                                                       'items_5': data_2[5],
                                                       'items_6': data_2[6],
                                                       'items_7': data_2[7],
                                                       'date_month': data_2[8]
                                                       })
    else:
        return render(request, 'life_style_cdr.html')


# cuemath agent performance report
def cuemath_report(request):
    s_date = request.GET.get('startdate')
    e_date = request.GET.get('enddate')
    page = request.GET.get('page')
    csv = request.GET.get('csv')
    e_date = datetime.datetime.strptime(e_date, '%Y-%m-%d')  # converting str date into datetime format
    s_date = datetime.datetime.strptime(s_date, '%Y-%m-%d')  # converting str date into datetime format
    e_date += datetime.timedelta(days=1)  # increment date by 1
    print(s_date, e_date)
    cdr_report = CdrReport.objects.filter(date__range=(s_date, e_date))
    break_report = BreakReport.objects.filter(date__range=(s_date, e_date))
    login_logout = LoginLogout.objects.filter(date_init__range=(s_date, e_date))
    agent_id = AgentId.objects.all()
    if cdr_report and break_report and login_logout and agent_id:
        report = cuemath_report_analysis(cdr_report, break_report, login_logout, agent_id)
        # download(request,report[1])
        if csv:
            return report[1]
        data = paginate_query_set(report[0], page)
        return render(request, 'cuemath.html', {'items': data
                                            })
    else:
        return render(request, 'cuemath.html')


def cuemath_agent_performance(request):
    s_date = request.GET.get('startdate')
    e_date = request.GET.get('enddate')
    agent_no = request.GET.get('agent_no')
    e_date = datetime.datetime.strptime(e_date, '%Y-%m-%d')  # converting str date into datetime format
    s_date = datetime.datetime.strptime(s_date, '%Y-%m-%d')  # converting str date into datetime format
    e_date += datetime.timedelta(days=1)  # increment date by 1
    print(s_date, e_date, agent_no)
    # posts = [{'source': i.source, 'des': i.destination} for i in CdrReport.objects.filter(date__range=(s_date, e_date)).filter(source=agent_no)]
    cdr_report = CdrReport.objects.filter(date__range=(s_date, e_date)).filter(Q(source=agent_no) | Q(dst_channel=agent_no))
    break_report = BreakReport.objects.filter(date__range=(s_date, e_date)).filter(no_agent=agent_no)
    login_logout = LoginLogout.objects.filter(date_init__range=(s_date, e_date)).filter(agent=agent_no)
    posts = cuemath_agent_report(cdr_report, break_report, login_logout)
    return JsonResponse({"posts":  posts}, status=200)


def reports(request):
    return render(request, 'table_call.html')


# sending the all table data without filtering
class TABLES:
    def __init__(self):
        self.GET = None

    def call_entry(self):
        posts_list = CallEntry.objects.all()
        query = self.GET.get('q_c_entry')
        csv = self.GET.get('csv')
        if csv:
            return djqscsv.render_to_csv_response(posts_list)
        if query:
            posts_list = CallEntry.objects.filter(
                Q(unique_id__icontains=query) |
                Q(datetime_init__icontains=query) | Q(status__icontains=query)
            ).distinct()
        page = self.GET.get('page')
        data = paginate_query_set(posts_list, page)
        return render(self, 'call_entry.html', {'items': data})

    def call_progress(self):
        posts_list = CallProgress.objects.all()
        query = self.GET.get('q_c_progress')
        csv = self.GET.get('csv')
        if csv:
            return djqscsv.render_to_csv_response(posts_list)
        if query:
            posts_list = CallProgress.objects.filter(
                Q(unique_id__icontains=query) |
                Q(datetime_entry__icontains=query) | Q(new_status__icontains=query)
            ).distinct()
        page = self.GET.get('page')
        data = paginate_query_set(posts_list, page)
        return render(self, 'call_progress.html', {'items': data})

    def cdr(self):
        posts_list = Cdr.objects.all()
        query = self.GET.get('q_cdr')
        csv = self.GET.get('csv')
        if csv:
            return djqscsv.render_to_csv_response(posts_list)
        if query:
            posts_list = Cdr.objects.filter(
                Q(unique_id__icontains=query) |
                Q(call_date__icontains=query) | Q(disposition__icontains=query)
            ).distinct()
        page = self.GET.get('page')
        data = paginate_query_set(posts_list, page)
        # data = serializers.serialize('json', data)
        return render(self, 'cdr.html', {'items': data})

    def call_entry_and_cdr(self):
        query = self.GET.get('q_ce_and_cdr')
        posts_list = CallEntryAndCdr.objects.all()
        csv = self.GET.get('csv')
        if csv:
            return djqscsv.render_to_csv_response(posts_list)
        elif query:
            posts_list = CallEntryAndCdr.objects.filter(
                Q(unique_id__icontains=query) | Q(call_date__icontains=query) |
                Q(datetime_init__icontains=query) | Q(status__icontains=query)
            ).distinct()
        page = self.GET.get('page')
        data = paginate_query_set(posts_list, page)
        return render(self, 'call_entry_and_cdr.html', {'items': data})

    def call_entry_not_matched(self):
        query = self.GET.get('q_ce_not_matched')
        posts_list = CallEntryAndCdrNotMatched.objects.all()
        csv = self.GET.get('csv')
        if csv:
            return djqscsv.render_to_csv_response(posts_list)
        elif query:
            posts_list = CallEntryAndCdrNotMatched.objects.filter(
                Q(unique_id__icontains=query) | Q(datetime_entry_queue__icontains=query) |
                Q(status__icontains=query)
            ).distinct()
        page = self.GET.get('page')
        data = paginate_query_set(posts_list, page)
        return render(self, 'callentry_not_matched.html', {'items': data})

    def cdr_not_matched(self):
        query = self.GET.get('q_cdr_not_matched')
        posts_list = CdrAndCallEntryNotMatched.objects.all()
        csv = self.GET.get('csv')
        if csv:
            return djqscsv.render_to_csv_response(posts_list)
        elif query:
            posts_list = CdrAndCallEntryNotMatched.objects.filter(
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


def register_user(request):
    message = "Please Sign up"
    f_name = request.POST.get('first_name')
    l_name = request.POST.get('last_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    print(email, password1)
    if email:
        try:
            if (
                    '@gmail.com' or '.com' or '.in' or '.co' or '@facebook.com' or '@grssl.uk' or '@grassrootsbpo.com' or '@yahoo.com') in email:
                if password1 == password2:
                    validate_email = User.objects.get(email=email)
                    if validate_email.email:
                        message = 'User with this email already exist.'
                    else:
                        message = 'Invalid login, Email or Password is incorrect.'
                else:
                    message = "Password doesn't matched"
            else:
                message = 'Invalid login, Email or Password is incorrect.'

        except ObjectDoesNotExist:
            try:
                if len(password1) < 6:
                    message = "password length must be greater than 6"

                elif (password1 and password2) is not None:
                    User.objects.create_user(username=username, email=email, password=password1, first_name=f_name,
                                             last_name=l_name)
                    return HttpResponseRedirect('/login')
                else:
                    message = 'Invalid login, Email or Password is incorrect.'
            except IntegrityError:
                message = "Username already exists"
    return render(request, 'register.html', {'message': message})


def change_pass(request):
    message = "Change Password"
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(password1, password2)
        try:
            if password1 == password2:
                u = User.objects.get(email=email)
                u.set_password(password1)
                u.save()
                return HttpResponseRedirect('/login')
            else:
                message = "Passwords doesn't Match"
        except ObjectDoesNotExist:
            message = "E-mail not matched"
    return render(request, 'change_password.html', {'message': message})


def login(request):
    message = "Please Sign In"
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']
        print(password)
        try:
            user = User.objects.get(email=email)
            if authenticate(username=user.username, password=password):
                return HttpResponseRedirect('/accounts/index/')
            else:
                message = 'Invalid login, Please try again.'
        except ObjectDoesNotExist:
            message = 'Invalid login, Please try again.'
        except AttributeError:
            message = message
    return render(request, 'login.html', {'message': message})


def index(request):
    _cdr = Cdr.objects.all()
    ans = Cdr.objects.filter(disposition='ANSWERED')
    no_ans = Cdr.objects.filter(disposition='NO ANSWER')
    fail = Cdr.objects.filter(disposition='FAILED')
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
