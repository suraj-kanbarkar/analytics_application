import csv
import datetime


def calculate_sec_to_time(a):
    totalSecs, sec = divmod(a, 60)
    hr, min = divmod(totalSecs, 60)
    hrs = ("%d:%02d:%02d" % (hr, min, sec))
    return hrs

def log_hrs(x,y):
    total_log_hrs = str(datetime.datetime.strptime(y, '%H:%M:%S') \
                                - datetime.datetime.strptime(x, '%H:%M:%S'))
    return total_log_hrs


cdr = '/home/appdevelopement/Desktop/cdr.csv'
br = '/home/appdevelopement/Desktop/break_report.csv'
log = '/home/appdevelopement/Desktop/login_logout.csv'
def agent_report(br, log, cdr):
    with open(br, 'rt') as csv_file_1, \
            open(log, 'rt') as csv_file_2, \
            open(cdr, 'rt') as csv_file_3:

        reader_1 = csv.DictReader(csv_file_1)
        break_report = list(reader_1)
        reader_2 = csv.DictReader(csv_file_2)
        login_logout = list(reader_2)
        reader_3 = csv.DictReader(csv_file_3)
        cdr_report = list(reader_3)

        agent_dict = {}
        a = []
        for i in login_logout:
            agent = i['agent']
            start_date = i['date_init'].split()[0]
            if agent not in a:
                a.append(agent)
                agent_dict[agent] = {}
                login_time = i['date_init'].split()[1]
                logout_time = i['date_end'].split()[1]
                agent_dict[agent][start_date] = {'login': login_time, 'logout': logout_time}

            if agent_dict[agent].get(start_date) is None:
                login_time = i['date_init'].split()[1]
                logout_time = i['date_end'].split()[1]
                agent_dict[agent][start_date] = {'login': login_time, 'logout': logout_time}
            existing_login = agent_dict[agent][start_date]['login']
            existing_logout = agent_dict[agent][start_date]['logout']

            if i['date_init'] < existing_login:
                login_time = i['date_init'].split()[1]
                agent_dict[agent][start_date]['login'] = login_time

            if existing_logout < i['date_end']:
                logout_time = i['date_end'].split()[1]
                agent_dict[agent][start_date]['logout'] = logout_time

    for key, value in agent_dict.items():
        for v, k in value.items():
            if key:
                k['total_log_hrs'] = log_hrs(k['login'], k['logout'])
            for i in break_report:
                if key == i['No. Agent'] and v == i['date']:
                    k['total_break_hrs_per_day'] = i['Total']
                    k['tea_break'] = i['Tea Break']
                    k['lunch_break'] = i['Lunch Break']
                    k['manual_dial_Break'] = i['Manual_dial_Break']
                    k['auxillary_break'] = i['Auxillary_Break']

            total_dialer_call_time, total_manual_call_time, out_going_short_calls, incoming_short_calls, \
            og_answered, og_busy, og_no_answered, og_failed, ic_answered = 0, 0, 0, 0, 0, 0, 0, 0, 0
            for present_row in cdr_report:
                new_duration = present_row['duration_in_sec']
                date = present_row['date']
                # calculating for outgoing calls
                if v == date:
                    if present_row['source'] == key:
                        total_dialer_call_time += int(new_duration)
                        if int(new_duration) < 10:
                            out_going_short_calls += 1
                        if present_row['status'] == 'ANSWERED':
                            og_answered += 1
                        elif present_row['status'] == 'BUSY':
                            og_busy += 1
                        elif present_row['status'] == 'NO ANSWER':
                            og_no_answered += 1
                        elif present_row['status'] == 'FAILED':
                            og_failed += 1

                    if present_row['destination'] == key:
                        total_manual_call_time += int(new_duration)
                        if present_row['status'] == 'ANSWERED':
                            ic_answered += 1
                        if int(new_duration) < 10:
                            incoming_short_calls += 1
            k['outgoing_call_time'] = calculate_sec_to_time(total_dialer_call_time)
            k['outgoing_short_calls'] = out_going_short_calls
            k['incoming_call_time'] = calculate_sec_to_time(total_manual_call_time)
            k['incoming_short_calls'] = incoming_short_calls
            k['talk_time'] = calculate_sec_to_time(total_dialer_call_time + total_manual_call_time)
            k['og_answered'] = og_answered
            k['og_no_answered'] = og_no_answered
            k['og_busy'] = og_busy
            k['og_failed'] = og_failed
            k['ic_answered'] = ic_answered
            total_production_hrs = str(datetime.datetime.strptime(k['total_log_hrs'], '%H:%M:%S')\
                                         - datetime.datetime.strptime(k['total_break_hrs_per_day'], '%H:%M:%S')\
                                         + datetime.datetime.strptime(k['outgoing_call_time'], '%H:%M:%S'))
            k['total_production_hrs'] = total_production_hrs.split()[1]

    with open('/home/appdevelopement/Desktop/agent_performance_report.csv', 'w') as file:
    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="cuemath_report.csv"'
        field_names = ['date', 'agent_no', 'login_t', 'logout_t', 't_log_hrs', 'tea_b', 'lun_b',
                         'aux_b', 'tb_hrs', 'og_sc', 'ic_sc', 'og_ans', 'og_no_ans', 'og_busy', 'og_failed', 'ic_ans',
                         'og_ct', 'ic_ct', 'tt', 'tp_hrs']
        agent_performance = csv.DictWriter(file, fieldnames=field_names)
        agent_performance.writeheader()

        for key, value in agent_dict.items():
            for v, k in value.items():
                performance = {'date': v, 'agent_no': key, 'login_t': k['login'],
                               'logout_t': k['logout'], 't_log_hrs': k['total_log_hrs'],
                               'tb_hrs': k['total_break_hrs_per_day'], 'tea_b':k['tea_break'],
                               'lun_b':k['lunch_break'], 'aux_b':k['auxillary_break'],
                               'og_sc': k['outgoing_short_calls'], 'ic_sc': k['incoming_short_calls'],
                               'og_ans': k['og_answered'], 'og_no_ans':k['og_no_answered'], 'og_busy': k['og_busy'],
                               'og_failed': k['og_failed'], 'ic_ans': k['ic_answered'], 'ic_ct': k['incoming_call_time'],
                               'og_ct': k['outgoing_call_time'], 'tt': k['talk_time'],
                               'tp_hrs': k['total_production_hrs']}
                agent_performance.writerow(performance)
        # return response

agent_report(br, log, cdr)