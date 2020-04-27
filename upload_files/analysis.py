import csv
import datetime
from datetime import timedelta, date, time
from datetime import date
import calendar
from functools import reduce


# converting datetime format and finding date, month and year from datetime
def findDay(datetim):
    try:
        date = datetime.datetime.strptime(datetim, '%Y-%m-%d %H:%M:%S')
        tim = datetime.datetime.strptime(datetim, '%Y-%m-%d %H:%M:%S').time()
        year = date.year
        day = date.day
        month = date.month
        born = datetime.date(year, month, day)
        weekday = born.strftime("%a")
        month = born.strftime("%b")
        year = born.strftime("%Y")
        date_month = str(day) + "/" + month  # gives date and month in the format of date/month
        return day, month, date_month, weekday, year, tim, date
    except ValueError:
        pass
    except TypeError:
        pass
    except AttributeError:
        pass


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def inbound_performance(date_n_data):
    aband_on_queue, agent_ans, agent_ans_and_transf, total_calls = [], [], [], []
    count_aband_on_que, count_agent_ans, count_agent_ans_and_transf, count_aband_on_que_less_20_sec, \
    count_aband_on_que_less_10_sec, count_calls_ans_sl_less_than_20, count_calls_ans_sl_less_than_10, a = 0, 0, 0, 0, 0, 0, 0, 0
    d = ''
    for i in date_n_data:
        try:
            result = findDay(datetim=i.Queue_Entry_Time)
            d = result[2:4]
            x = i.Queue_Wait_Time
            h, m, s = x.split(':')
            time_in_sec = int(h) * 3600 + int(m) * 60 + int(s)
            if i.Status == 'ABANDONED ON QUEUE':
                aband_on_queue.append(i)
                count_aband_on_que += 1

            if i.Status == 'AGENT ANSWERED':
                a += 1

            if i.Status == 'AGENT ANSWERED AND TRANSFERRED':
                agent_ans_and_transf.append(i)
                count_agent_ans_and_transf += 1

            if i.Status == 'ABANDONED ON QUEUE' and time_in_sec <= 10:
                count_aband_on_que_less_10_sec += 1

            if i.Status == 'AGENT ANSWERED' and time_in_sec <= 10:
                count_calls_ans_sl_less_than_10 += 1

            if i.Status == 'ABANDONED ON QUEUE' and time_in_sec <= 20:
                count_aband_on_que_less_20_sec += 1

            if (i.Status == 'AGENT ANSWERED AND TRANSFERRED' or i.Status == 'AGENT ANSWERED' or
                i.Status == 'ABANDONED ON QUEUE') and time_in_sec <= 20:
                count_calls_ans_sl_less_than_20 += 1

            if i.Status == 'AGENT ANSWERED' or i.Status == 'AGENT ANSWERED AND TRANSFERRED':
                agent_ans.append(i)
                count_agent_ans += 1

        except ValueError:
            pass
        except TypeError:
            pass
        except AttributeError:
            pass
    total_calls.extend(agent_ans)
    total_calls.extend(aband_on_queue)
    offered_calls = len(total_calls)
    calls_ans = count_agent_ans
    calls_ans_and_transferred = count_agent_ans + count_agent_ans_and_transf
    calls_ans_percentage = (count_agent_ans / offered_calls) * 100

    # calculations for less than 20 sec calls ans
    calls_ans_sl_less_than_20 = count_calls_ans_sl_less_than_20
    calls_ans_sl_percentage = (count_calls_ans_sl_less_than_20 / offered_calls) * 100
    abandoned = count_aband_on_que - count_aband_on_que_less_20_sec
    aband_on_que_less_20_sec = count_aband_on_que_less_20_sec
    abandoned_percentage = (abandoned / offered_calls) * 100
    abandoned_less_than_20_sec_percentage = (aband_on_que_less_20_sec / offered_calls) * 100
    calls_ans_less_than_20_sec_percentage = (count_agent_ans / (offered_calls - aband_on_que_less_20_sec)) * 100
    service_level_less_than_20_sec_percentage = (count_calls_ans_sl_less_than_20 / (
            offered_calls - count_aband_on_que_less_20_sec)) * 100

    # calculations for less than 10 sec calls ans
    calls_ans_sl_less_than_10 = count_calls_ans_sl_less_than_10
    service_level_less_than_10_sec = (count_calls_ans_sl_less_than_10 / offered_calls) * 100
    service_level_less_than_10_sec_percentage = (count_calls_ans_sl_less_than_10 / (
            offered_calls - count_aband_on_que_less_10_sec)) * 100
    aband_on_que_less_10_sec = count_aband_on_que_less_10_sec
    aband_on_que_less_10_sec_percentage = (aband_on_que_less_10_sec / offered_calls) * 100

    records = {'date': d[0], 'day': d[1], 'calls_offered': offered_calls, 'calls_answered': calls_ans,
               'calls_ans_and_transferred': calls_ans_and_transferred,
               'calls_ans_percentage': truncate(calls_ans_percentage, 2),
               'abandoned': abandoned,
               'calls_answered_sl': calls_ans_sl_less_than_20,
               'service_level_percentage': truncate(calls_ans_sl_percentage, 2),
               'abandoned_percentage': truncate(abandoned_percentage, 2),
               'aband_on_que_less_20_sec': aband_on_que_less_20_sec,
               'abandoned_less_than_20_sec_percentage': truncate(abandoned_less_than_20_sec_percentage, 2),
               'calls_ans_less_than_20_sec_percentage': truncate(calls_ans_less_than_20_sec_percentage, 2),
               'service_level_less_than_20_sec_percentage': truncate(service_level_less_than_20_sec_percentage, 2),
               'calls_ans_sl_less_than_10_sec': calls_ans_sl_less_than_10,
               'service_level_less_than_10_sec': truncate(service_level_less_than_10_sec),
               'service_level_less_than_10_sec_percentage': truncate(service_level_less_than_10_sec_percentage, 2),
               'abandoned_less_than_10_sec': aband_on_que_less_10_sec,
               'aband_on_que_less_10_sec_percentage': truncate(aband_on_que_less_10_sec_percentage, 2)}
    return records


# ---------------------------------------------------------------------------------------------------------------------


# calls offered for lifestyle inbound by time
def calls_analysis_by_time(d_1, time_n_data):
    m_s_d_1, m_s_d_2 = '00:00', '59:59'
    d_2 = datetime.datetime.strptime(str(d_1), '%Y-%m-%d')
    d_2 = d_2.strftime('%Y-%m-%d')
    a, b, c, d, e, f, g = [], [], [], [], [], [], []
    offered_calls = None
    records_calls_offered = dict()
    records_calls_answered = dict()
    records_calls_answered_percentage = dict()
    records_service_level_calls = dict()
    records_s_l_calls_percentage = dict()
    records_aband_on_que = dict()
    records_aband_on_que_percentage = dict()

    for hour in range(10, 22):
        count_aband_on_que, count_ans_calls, count_agent_ans_and_transf, count_aband_on_que_greater_20_sec, \
        count_calls_ans_sl_less_than_20 = 0, 0, 0, 0, 0

        start_hour = hour
        end_hour = hour
        time_in_hours = str(hour) + '_' + str((hour + 1))
        result = time_n_data.filter(
            Queue_Entry_Time__range=(str(d_1) + ' ' + str(start_hour)
                                     + ':' + m_s_d_1, d_2 + ' ' + str(end_hour) + ':' + m_s_d_2))
        for i in result:
            date_data = findDay(datetim=str(i.Queue_Entry_Time))
            date_month = date_data[2]

            # sorting data by Queue_Wait_Time for service level calls
            tim = str(i.Queue_Wait_Time)
            h, m, s = tim.split(':')
            time_in_sec = int(h) * 3600 + int(m) * 60 + int(s)

            if i.Status == 'ABANDONED ON QUEUE' and time_in_sec > 20:
                count_aband_on_que_greater_20_sec += 1

            if (i.Status == 'AGENT ANSWERED AND TRANSFERRED' or i.Status == 'AGENT ANSWERED' or
                i.Status == 'ABANDONED ON QUEUE') and time_in_sec <= 20:
                count_calls_ans_sl_less_than_20 += 1

            if i.Status == 'ABANDONED ON QUEUE':
                count_aband_on_que += 1

            if i.Status == 'AGENT ANSWERED':
                count_ans_calls += 1

            if i.Status == 'AGENT ANSWERED AND TRANSFERRED':
                count_agent_ans_and_transf += 1

            # Adding date and month to records
            records_calls_offered['date_month'] = date_month
            records_calls_answered['date_month'] = date_month
            records_calls_answered_percentage['date_month'] = date_month
            records_service_level_calls['date_month'] = date_month
            records_s_l_calls_percentage['date_month'] = date_month
            records_aband_on_que['date_month'] = date_month
            records_aband_on_que_percentage['date_month'] = date_month
        try:
            # offered calls counts
            offered_calls = count_aband_on_que + count_ans_calls + count_agent_ans_and_transf
            a.append(offered_calls)
            records_calls_offered[time_in_hours] = offered_calls

            # answered calls counts
            answered_calls = count_ans_calls + count_agent_ans_and_transf
            b.append(answered_calls)
            records_calls_answered[time_in_hours] = answered_calls

            # answered calls percentage
            answered_calls_percentage = truncate((answered_calls / offered_calls) * 100, 2)
            c.append(answered_calls_percentage)
            records_calls_answered_percentage[time_in_hours] = answered_calls_percentage

            # Service level calls counts
            service_level_calls = count_calls_ans_sl_less_than_20
            d.append(service_level_calls)
            records_service_level_calls[time_in_hours] = service_level_calls

            # Service level calls percentage
            s_l_calls_percentage = truncate((service_level_calls / offered_calls) * 100, 2)
            e.append(s_l_calls_percentage)
            records_s_l_calls_percentage[time_in_hours] = s_l_calls_percentage

            # Abandoned calls counts
            abandoned = count_aband_on_que_greater_20_sec
            g.append(abandoned)
            records_aband_on_que[time_in_hours] = abandoned

            # Abandoned calls percentage
            abandoned = truncate((count_aband_on_que_greater_20_sec / offered_calls) * 100, 2)
            f.append(abandoned)
            records_aband_on_que_percentage[time_in_hours] = abandoned
        except ZeroDivisionError:
            pass
    # calculating the total counts of offered calls by time
    try:
        offer_call = reduce((lambda x, y: x + y), a)
        records_calls_offered['calls_offered_count'] = offer_call

        # calculating the total counts of answered calls data by time
        records_calls_answered['calls_answered_count'] = reduce((lambda x, y: x + y), b)

        # calculating the total percentage of answered calls y time
        records_calls_answered_percentage['calls_answered_count_percentage'] = truncate(
            (reduce((lambda x, y: x + y), b) / offer_call) * 100, 2)

        # calculating the total counts for service level calls
        records_service_level_calls['service_level_calls_counts'] = reduce((lambda x, y: y + x), d)

        # calculating the total serviice level calls percentage
        records_s_l_calls_percentage['s_l_calls_percentage'] = truncate((reduce((lambda x, y: x + y), d) / offer_call) * 100, 2)

        # calculating the total abandoned calls
        records_aband_on_que['aband_on_que_counts'] = reduce((lambda x, y: y + x), g)

        # calculating the total abandoned calls percentage
        records_aband_on_que_percentage['aband_on_que_percentage'] = truncate((reduce((lambda x, y: x + y), g) / offer_call) * 100, 2)
    except TypeError:
        pass
    return records_calls_offered, records_calls_answered, records_calls_answered_percentage, \
           records_service_level_calls, records_s_l_calls_percentage, records_aband_on_que, \
           records_aband_on_que_percentage


# ---------------------------------------------------------------------------------------------------------------------


# total calls offered counts by time for lifestyle cdr
def total_calls_analysis(calls_offer, calls_ans, calls_s_l, call_aban):
    # total counts for offered calls by time
    calls_offered_count, c_10_11, c_11_12, c_12_13, c_13_14, c_14_15, c_15_16, c_16_17, c_17_18, c_18_19, c_19_20, \
    c_20_21, c_21_22 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    data_1 = dict()
    for i in calls_offer:
        try:
            calls_offered_count += i['calls_offered_count']
            c_10_11 += i['10_11']
            c_11_12 += i['11_12']
            c_12_13 += i['12_13']
            c_13_14 += i['13_14']
            c_14_15 += i['14_15']
            c_15_16 += i['15_16']
            c_16_17 += i['16_17']
            c_17_18 += i['17_18']
            c_18_19 += i['18_19']
            c_19_20 += i['19_20']
            c_20_21 += i['20_21']
            c_21_22 += i['21_22']
        except KeyError:
            pass
    data_1['date_month'] = 'Total'
    data_1['calls_offered_count'] = calls_offered_count
    data_1['10_11'] = c_10_11
    data_1['11_12'] = c_11_12
    data_1['12_13'] = c_12_13
    data_1['13_14'] = c_13_14
    data_1['14_15'] = c_14_15
    data_1['15_16'] = c_15_16
    data_1['16_17'] = c_16_17
    data_1['17_18'] = c_17_18
    data_1['18_19'] = c_18_19
    data_1['19_20'] = c_19_20
    data_1['20_21'] = c_20_21
    data_1['21_22'] = c_21_22
    # appending the offered counts for further use
    a = [calls_offered_count, c_10_11, c_11_12, c_12_13, c_13_14, c_14_15, c_15_16, c_16_17, c_17_18, c_18_19, c_19_20,
         c_20_21, c_21_22]

    # total counts for answered calls by time
    calls_answered_count, c_10_11, c_11_12, c_12_13, c_13_14, c_14_15, c_15_16, c_16_17, c_17_18, c_18_19, c_19_20, \
    c_20_21, c_21_22 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    data_2 = dict()
    data_3 = dict()
    for i in calls_ans:
        try:
            calls_answered_count += i['calls_answered_count']
            c_10_11 += i['10_11']
            c_11_12 += i['11_12']
            c_12_13 += i['12_13']
            c_13_14 += i['13_14']
            c_14_15 += i['14_15']
            c_15_16 += i['15_16']
            c_16_17 += i['16_17']
            c_17_18 += i['17_18']
            c_18_19 += i['18_19']
            c_19_20 += i['19_20']
            c_20_21 += i['20_21']
            c_21_22 += i['21_22']
        except KeyError:
            pass
    data_2['date_month'] = 'Total'
    data_2['calls_answered_count'] = calls_answered_count
    data_2['10_11'] = c_10_11
    data_2['11_12'] = c_11_12
    data_2['12_13'] = c_12_13
    data_2['13_14'] = c_13_14
    data_2['14_15'] = c_14_15
    data_2['15_16'] = c_15_16
    data_2['16_17'] = c_16_17
    data_2['17_18'] = c_17_18
    data_2['18_19'] = c_18_19
    data_2['19_20'] = c_19_20
    data_2['20_21'] = c_20_21
    data_2['21_22'] = c_21_22

    # appending the answered counts for further use
    b = [calls_answered_count, c_10_11, c_11_12, c_12_13, c_13_14, c_14_15, c_15_16, c_16_17, c_17_18,
         c_18_19, c_19_20, c_20_21, c_21_22]
    try:
        # calculating the percentage of total answered calls by time
        total_percentage = list(map((lambda x, y: (x / y) * 100), b, a))
        lst = ['calls_answered_count_percentage', '10_11', '11_12', '12_13', '13_14', '14_15', '15_16', '16_17',
               '17_18', '18_19', '19_20', '20_21', '21_22']
        for i in range(len(lst)):
            data_3[lst[i]] = truncate(total_percentage[i], 2)
        data_3['date_month'] = 'Total'

    except ZeroDivisionError:
        pass

    # calculating the total service level calls by time
    service_level_calls_counts, c_10_11, c_11_12, c_12_13, c_13_14, c_14_15, c_15_16, c_16_17, c_17_18, c_18_19, c_19_20, \
    c_20_21, c_21_22 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    data_4 = dict()
    data_5 = dict()
    for i in calls_s_l:
        try:
            service_level_calls_counts += i['service_level_calls_counts']
            c_10_11 += i['10_11']
            c_11_12 += i['11_12']
            c_12_13 += i['12_13']
            c_13_14 += i['13_14']
            c_14_15 += i['14_15']
            c_15_16 += i['15_16']
            c_16_17 += i['16_17']
            c_17_18 += i['17_18']
            c_18_19 += i['18_19']
            c_19_20 += i['19_20']
            c_20_21 += i['20_21']
            c_21_22 += i['21_22']
        except KeyError:
            pass
    data_4['date_month'] = 'Total'
    data_4['service_level_calls_counts'] = service_level_calls_counts
    data_4['10_11'] = c_10_11
    data_4['11_12'] = c_11_12
    data_4['12_13'] = c_12_13
    data_4['13_14'] = c_13_14
    data_4['14_15'] = c_14_15
    data_4['15_16'] = c_15_16
    data_4['16_17'] = c_16_17
    data_4['17_18'] = c_17_18
    data_4['18_19'] = c_18_19
    data_4['19_20'] = c_19_20
    data_4['20_21'] = c_20_21
    data_4['21_22'] = c_21_22

    c = [service_level_calls_counts, c_10_11, c_11_12, c_12_13, c_13_14, c_14_15, c_15_16, c_16_17, c_17_18, c_18_19,
         c_19_20, c_20_21, c_21_22]
    # calculating total service level percentage by time
    try:
        total_sl_percentage = list(map((lambda x, y: (x / y) * 100), c, a))
        lst = ['s_l_calls_percentage', '10_11', '11_12', '12_13', '13_14', '14_15', '15_16', '16_17',
               '17_18', '18_19', '19_20', '20_21', '21_22']
        for i in range(len(lst)):
            data_5[lst[i]] = truncate(total_sl_percentage[i], 2)
        data_5['date_month'] = 'Total'
    except ZeroDivisionError:
        pass


    # calculating total abandoned calls by time
    aband_on_que_counts, c_10_11, c_11_12, c_12_13, c_13_14, c_14_15, c_15_16, c_16_17, c_17_18, c_18_19, c_19_20, \
    c_20_21, c_21_22 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    data_6 = dict()
    data_7 = dict()
    for i in call_aban:
        try:
            aband_on_que_counts += i['aband_on_que_counts']
            c_10_11 += i['10_11']
            c_11_12 += i['11_12']
            c_12_13 += i['12_13']
            c_13_14 += i['13_14']
            c_14_15 += i['14_15']
            c_15_16 += i['15_16']
            c_16_17 += i['16_17']
            c_17_18 += i['17_18']
            c_18_19 += i['18_19']
            c_19_20 += i['19_20']
            c_20_21 += i['20_21']
            c_21_22 += i['21_22']
        except KeyError:
            pass
    data_6['date_month'] = 'Total'
    data_6['aband_on_que_counts'] = aband_on_que_counts
    data_6['10_11'] = c_10_11
    data_6['11_12'] = c_11_12
    data_6['12_13'] = c_12_13
    data_6['13_14'] = c_13_14
    data_6['14_15'] = c_14_15
    data_6['15_16'] = c_15_16
    data_6['16_17'] = c_16_17
    data_6['17_18'] = c_17_18
    data_6['18_19'] = c_18_19
    data_6['19_20'] = c_19_20
    data_6['20_21'] = c_20_21
    data_6['21_22'] = c_21_22

    d = [aband_on_que_counts, c_10_11, c_11_12, c_12_13, c_13_14, c_14_15, c_15_16, c_16_17, c_17_18, c_18_19,
         c_19_20, c_20_21, c_21_22]

    # calculating total abandoned calls percentage by time
    try:
        total_aban_percentage = list(map((lambda x, y: (x / y) * 100), d, a))
        lst = ['aband_on_que_percentage', '10_11', '11_12', '12_13', '13_14', '14_15', '15_16', '16_17',
               '17_18', '18_19', '19_20', '20_21', '21_22']
        for i in range(len(lst)):
            data_7[lst[i]] = truncate(total_aban_percentage[i], 2)
        data_7['date_month'] = 'Total'
    except ZeroDivisionError:
        pass

    return data_1, data_2, data_3, data_4, data_5, data_6, data_7


# ----------------------------------------------------------------------------------------------------------------------


def dat(cdr_life):
    array, date_month, time_array, inbound_record, inbound_calls_offered, inbound_calls_answered, \
    inbound_calls_answered_percentage, inbound_service_level_calls, inbound_s_l_calls_percentage, \
    inbound_abandoned_percentage, inbound_abandoned = [], [], [], [], [], [], [], [], [], [], []
    for d in cdr_life:
        date = findDay(d.Queue_Entry_Time)
        date1 = date[6].date()
        time = date[5]
        if date1 not in array:
            array.append(date1)
        if date[2] not in date_month:
            date_month.append(date[2])
        if time not in time_array:
            time_array.append(time)
    # lifestyle inbound performance
    for d_1 in array:
        d_2 = datetime.datetime.strptime(str(d_1), '%Y-%m-%d').date()
        d_2 += datetime.timedelta(days=1)
        d_2 = d_2.strftime('%Y-%m-%d')
        result_1 = inbound_performance(date_n_data=cdr_life.filter(Queue_Entry_Time__range=(d_1, d_2)))
        inbound_record.append(result_1)

    result_2 = inbound_performance(date_n_data=cdr_life)  # appending total record details into inbound
    result_2['date'] = 'Total'
    result_2['day'] = ''
    inbound_record.append(result_2)

    # lifestyle offered calls, answered calls between time
    for d_1 in array:
        result_2 = calls_analysis_by_time(d_1, time_n_data=cdr_life)
        inbound_calls_offered.append(result_2[0])
        inbound_calls_answered.append(result_2[1])
        inbound_calls_answered_percentage.append(result_2[2])
        inbound_service_level_calls.append(result_2[3])
        inbound_s_l_calls_percentage.append(result_2[4])
        inbound_abandoned.append(result_2[5])
        inbound_abandoned_percentage.append(result_2[6])
    # for total lifestyle records
    calls = total_calls_analysis(calls_offer=inbound_calls_offered, calls_ans=inbound_calls_answered,
                                 calls_s_l=inbound_service_level_calls, call_aban=inbound_abandoned)

    inbound_calls_offered.append(calls[0])
    inbound_calls_answered.append(calls[1])
    inbound_calls_answered_percentage.append(calls[2])
    inbound_service_level_calls.append(calls[3])
    inbound_s_l_calls_percentage.append(calls[4])
    inbound_abandoned.append(calls[5])
    inbound_abandoned_percentage.append(calls[6])
    return inbound_record, inbound_calls_offered, inbound_calls_answered, inbound_calls_answered_percentage, \
           inbound_service_level_calls, inbound_s_l_calls_percentage, inbound_abandoned, \
           inbound_abandoned_percentage, date_month
