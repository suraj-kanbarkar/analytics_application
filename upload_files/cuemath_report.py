import csv
import datetime
from django.http import HttpResponse


def calculate_total_time(a):
    totalSecs, sec = divmod(a, 60)
    hr, min = divmod(totalSecs, 60)
    hrs = ("%d:%02d:%02d" % (hr, min, sec))
    return hrs


# cuemath day wise report
def cuemath_report_analysis(cdr_report, break_report, login_logout, agent_id):
    a = []
    d = {}
    for i in range(len(login_logout) - 1):
        inout = login_logout[i]
        agent = inout.agent
        next_inout = login_logout[i + 1]
        start_date = inout.date_init.date()
        end_date = next_inout.date_init.date()
        no_of_times_logged = 0
        # calculating number of times logged
        for j in login_logout:
            x = j.date_init.date()
            if agent == j.agent and start_date == x:
                no_of_times_logged += 1

        # calculating login time and logout time
        if agent not in a:
            d[agent] = {}
            a.append(inout.agent)
            date = str(inout.date_init.time())

        if next_inout.agent not in a:
            new_date_end = str(inout.date_end.time())
            total_log_hrs = str(datetime.datetime.strptime(new_date_end, '%H:%M:%S') \
                                - datetime.datetime.strptime(date, '%H:%M:%S'))
            d[agent][start_date] = {'login': date, 'logout': new_date_end, 'total_log_hrs': total_log_hrs,
                                    'no_of_times_logged': no_of_times_logged}

        if start_date != end_date and inout.agent == next_inout.agent:
            new_date_end = str(inout.date_end.time())
            total_log_hrs = str(datetime.datetime.strptime(new_date_end, '%H:%M:%S') \
                                - datetime.datetime.strptime(date, '%H:%M:%S'))
            d[agent][start_date] = {'login': date, 'logout': new_date_end, 'total_log_hrs': total_log_hrs,
                                    'no_of_times_logged': no_of_times_logged}
            date = str(next_inout.date_init.time())

    for key, value in d.items():
        for v, k in value.items():
            for id in agent_id:
                if key == id.agent_id:
                    k['agent_name'] = id.agent_name
            for i in break_report:
                if key == str(i.no_agent) and v == i.date.date():
                    k['total_break_hrs_per_day'] = str(i.total)
                    k['tea_break'] = str(i.tea_break)
                    k['lunch_break'] = str(i.lunch_break)
                    k['manual_dial_break'] = str(i.manual_dial_break)
                    k['auxillary_break'] = str(i.auxillary_break)

            total_dialer_call_time, total_manual_call_time, out_going_short_calls, incoming_short_calls, \
            og_answered, og_busy, og_no_answered, og_failed, ic_answered = 0, 0, 0, 0, 0, 0, 0, 0, 0
            for present_row in cdr_report:
                date = present_row.date.date()
                # calculating for outgoing calls
                if v == date:
                    if present_row.source == key:
                        total_dialer_call_time += int(present_row.duration)
                        if int(present_row.duration) < 10:
                            out_going_short_calls += 1
                        if present_row.status == 'ANSWERED':
                            og_answered += 1
                        elif present_row.status == 'BUSY':
                            og_busy += 1
                        elif present_row.status == 'NO ANSWER':
                            og_no_answered += 1
                        elif present_row.status == 'FAILED':
                            og_failed += 1

                    elif present_row.dst_channel == key:
                        total_manual_call_time += int(present_row.duration)
                        if present_row.status == 'ANSWERED':
                            ic_answered += 1
                        if int(present_row.duration) < 10:
                            incoming_short_calls += 1
            k['outgoing_call_time'] = calculate_total_time(total_dialer_call_time)
            k['outgoing_short_calls'] = out_going_short_calls
            k['incoming_call_time'] = calculate_total_time(total_manual_call_time)
            k['incoming_short_calls'] = incoming_short_calls
            k['talk_time'] = calculate_total_time(total_dialer_call_time + total_manual_call_time)
            k['og_answered'] = og_answered
            k['og_no_answered'] = og_no_answered
            k['og_busy'] = og_busy
            k['og_failed'] = og_failed
            k['ic_answered'] = ic_answered
            total_production_hrs = str(datetime.datetime.strptime(k['total_log_hrs'], '%H:%M:%S')
                                       - datetime.datetime.strptime(k['total_break_hrs_per_day'], '%H:%M:%S')
                                       + datetime.datetime.strptime(k['outgoing_call_time'], '%H:%M:%S'))
            k['total_production_hrs'] = total_production_hrs.split()[1]

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="cuemath_report.csv"'
    field_names_2 = ['date', 'agent_no', 'agent_name', 'login_time', 'logout_time', 'total_log_hrs',
                     'no_of_times_logged', 'tea_break', 'lunch_break', 'manual_dial_break', 'auxillary_break',
                     'total_break_hrs_per_day',
                     'outgoing_short_calls', 'incoming_short_calls', 'og_answered', 'og_no_answered',
                     'og_busy', 'og_failed', 'ic_answered', 'outgoing_call_time', 'incoming_call_time', 'talk_time',
                     'total_production_hrs']
    agent_performance = csv.DictWriter(response, fieldnames=field_names_2)
    agent_performance.writeheader()
    perform = []
    for key, value in d.items():
        for v, k in value.items():
            performance = {'date': v, 'agent_no': key, 'agent_name': k['agent_name'], 'login_time': k['login'],
                           'logout_time': k['logout'], 'total_log_hrs': k['total_log_hrs'],
                           'no_of_times_logged': k['no_of_times_logged'],
                           'total_break_hrs_per_day': k['total_break_hrs_per_day'],
                           'tea_break': k['tea_break'], 'lunch_break': k['lunch_break'],
                           'manual_dial_break': k['manual_dial_break'], 'auxillary_break': k['auxillary_break'],
                           'outgoing_short_calls': k['outgoing_short_calls'],
                           'incoming_short_calls': k['incoming_short_calls'],
                           'og_answered': k['og_answered'], 'og_no_answered': k['og_no_answered'],
                           'og_busy': k['og_busy'], 'og_failed': k['og_failed'], 'ic_answered': k['ic_answered'],
                           'incoming_call_time': k['incoming_call_time'], 'outgoing_call_time': k['outgoing_call_time'],
                           'talk_time': k['talk_time'], 'total_production_hrs': k['total_production_hrs']}

            agent_performance.writerow(performance)
            perform.append(performance)
    return perform, response


def cuemath_agent_report(cdr_report, break_report, login_logout):
    a = []
    d = {}
    for i in range(len(login_logout) - 1):
        inout = login_logout[i]
        agent = inout.agent
        next_inout = login_logout[i + 1]
        start_date = inout.date_init.date()
        end_date = next_inout.date_init.date()
        no_of_times_logged = 0
        # calculating number of times logged
        for j in login_logout:
            x = j.date_init.date()
            if agent == j.agent and start_date == x:
                no_of_times_logged += 1

        # calculating login time and logout time
        if agent not in a:
            d[agent] = {}
            a.append(inout.agent)
            date = str(inout.date_init.time())

        if next_inout.agent in a and start_date != end_date:
            new_date_end = str(inout.date_end.time())
            total_log_hrs = str(datetime.datetime.strptime(new_date_end, '%H:%M:%S') \
                                - datetime.datetime.strptime(date, '%H:%M:%S'))
            d[agent][start_date] = {'login': date, 'logout': new_date_end, 'total_log_hrs': total_log_hrs,
                                    'no_of_times_logged': no_of_times_logged}
            date = str(next_inout.date_init.time())

        elif next_inout.agent in a and start_date == end_date:
            new_date_end = str(next_inout.date_end.time())
            total_log_hrs = str(datetime.datetime.strptime(new_date_end, '%H:%M:%S') \
                                - datetime.datetime.strptime(date, '%H:%M:%S'))
            d[agent][start_date] = {'login': date, 'logout': new_date_end, 'total_log_hrs': total_log_hrs,
                                    'no_of_times_logged': no_of_times_logged}

    for key, value in d.items():
        for v, k in value.items():
            for i in break_report:
                if key == str(i.no_agent) and v == i.date.date():
                    k['total_break_hrs_per_day'] = str(i.total)
                    k['tea_break'] = str(i.tea_break)
                    k['lunch_break'] = str(i.lunch_break)
                    k['manual_dial_break'] = str(i.manual_dial_break)
                    k['auxillary_break'] = str(i.auxillary_break)

            total_dialer_call_time, total_manual_call_time, out_going_short_calls, incoming_short_calls,\
                og_answered, og_busy, og_no_answered, og_failed, ic_answered = 0, 0, 0, 0, 0, 0, 0, 0, 0
            for present_row in cdr_report:
                date = present_row.date.date()
                print(present_row.dst_channel)
                # calculating for outgoing calls
                if v == date:
                    if present_row.source == key:
                        total_dialer_call_time += int(present_row.duration)
                        if int(present_row.duration) < 10:
                            out_going_short_calls += 1
                        if present_row.status == 'ANSWERED':
                            og_answered += 1
                        elif present_row.status == 'BUSY':
                            og_busy += 1
                        elif present_row.status == 'NO ANSWER':
                            og_no_answered += 1
                        elif present_row.status == 'FAILED':
                            og_failed += 1

                    elif present_row.dst_channel == key:
                        total_manual_call_time += int(present_row.duration)
                        if present_row.status == 'ANSWERED':
                            ic_answered += 1
                        if int(present_row.duration) < 10:
                            incoming_short_calls += 1
            k['outgoing_call_time'] = calculate_total_time(total_dialer_call_time)
            k['outgoing_short_calls'] = out_going_short_calls
            k['incoming_call_time'] = calculate_total_time(total_manual_call_time)
            k['incoming_short_calls'] = incoming_short_calls
            k['talk_time'] = calculate_total_time(total_dialer_call_time + total_manual_call_time)
            k['og_answered'] = og_answered
            k['og_no_answered'] = og_no_answered
            k['og_busy'] = og_busy
            k['og_failed'] = og_failed
            k['ic_answered'] = ic_answered
            total_production_hrs = str(datetime.datetime.strptime(k['total_log_hrs'], '%H:%M:%S')
                                       - datetime.datetime.strptime(k['total_break_hrs_per_day'], '%H:%M:%S')
                                       + datetime.datetime.strptime(k['outgoing_call_time'], '%H:%M:%S'))
            k['total_production_hrs'] = total_production_hrs.split()[1]

    # Create the HttpResponse object with the appropriate CSV header.
    perform = []
    for key, value in d.items():
        for v, k in value.items():
            performance = {'date': v, 'agent_no': key, 'login_time': k['login'],
                           'logout_time': k['logout'], 'total_log_hrs': k['total_log_hrs'],
                           'no_of_times_logged': k['no_of_times_logged'],
                           'total_break_hrs_per_day': k['total_break_hrs_per_day'],
                           'tea_break': k['tea_break'], 'lunch_break': k['lunch_break'],
                           'manual_dial_break': k['manual_dial_break'], 'auxillary_break': k['auxillary_break'],
                           'outgoing_short_calls': k['outgoing_short_calls'],
                           'incoming_short_calls': k['incoming_short_calls'],
                           'og_answered': k['og_answered'], 'og_no_answered': k['og_no_answered'],
                           'og_busy': k['og_busy'], 'og_failed': k['og_failed'], 'ic_answered': k['ic_answered'],
                           'incoming_call_time': k['incoming_call_time'], 'outgoing_call_time': k['outgoing_call_time'],
                           'talk_time': k['talk_time'], 'total_production_hrs': k['total_production_hrs']}

            perform.append(performance)
    return perform