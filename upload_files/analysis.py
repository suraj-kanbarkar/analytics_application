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
    calls_ans_percentage = (count_agent_ans / len(total_calls)) * 100

    # calculations for less than 20 sec calls ans
    calls_ans_sl_less_than_20 = count_calls_ans_sl_less_than_20
    calls_ans_sl_percentage = (count_calls_ans_sl_less_than_20 / len(total_calls)) * 100
    abandoned = count_aband_on_que - count_aband_on_que_less_20_sec
    aband_on_que_less_20_sec = count_aband_on_que_less_20_sec
    abandoned_percentage = (abandoned / len(total_calls)) * 100
    abandoned_less_than_20_sec_percentage = (aband_on_que_less_20_sec / len(total_calls)) * 100
    calls_ans_less_than_20_sec_percentage = (count_agent_ans / (len(total_calls) - aband_on_que_less_20_sec)) * 100
    service_level_less_than_20_sec_percentage = (count_calls_ans_sl_less_than_20 / (
            len(total_calls) - count_aband_on_que_less_20_sec)) * 100

    # calculations for less than 10 sec calls ans
    calls_ans_sl_less_than_10 = count_calls_ans_sl_less_than_10
    service_level_less_than_10_sec = (count_calls_ans_sl_less_than_10 / len(total_calls)) * 100
    service_level_less_than_10_sec_percentage = (count_calls_ans_sl_less_than_10 / (
            len(total_calls) - count_aband_on_que_less_10_sec)) * 100
    aband_on_que_less_10_sec = count_aband_on_que_less_10_sec
    aband_on_que_less_10_sec_percentage = (aband_on_que_less_10_sec / len(total_calls)) * 100

    records = dict()
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
               'service_level_less_than_10_sec': service_level_less_than_10_sec,
               'service_level_less_than_10_sec_percentage': truncate(service_level_less_than_10_sec_percentage, 2),
               'abandoned_less_than_10_sec': aband_on_que_less_10_sec,
               'aband_on_que_less_10_sec_percentage': truncate(aband_on_que_less_10_sec_percentage, 2)}

    return records


def total_lifestyle_inbound_performance(date_n_data):
    aband_on_queue, agent_ans, agent_ans_and_transf, total_calls = [], [], [], []
    count_aband_on_que, count_agent_ans, count_agent_ans_and_transf, count_aband_on_que_less_20_sec, \
    count_aband_on_que_less_10_sec, count_calls_ans_sl_less_than_20, count_calls_ans_sl_less_than_10, a = 0, 0, 0, 0, 0, 0, 0, 0
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
    calls_ans_percentage = (count_agent_ans / len(total_calls)) * 100

    # calculations for less than 20 sec calls ans
    calls_ans_sl_less_than_20 = count_calls_ans_sl_less_than_20
    calls_ans_sl_percentage = (count_calls_ans_sl_less_than_20 / len(total_calls)) * 100
    abandoned = count_aband_on_que - count_aband_on_que_less_20_sec
    aband_on_que_less_20_sec = count_aband_on_que_less_20_sec
    abandoned_percentage = (abandoned / len(total_calls)) * 100
    abandoned_less_than_20_sec_percentage = (aband_on_que_less_20_sec / len(total_calls)) * 100
    calls_ans_less_than_20_sec_percentage = (count_agent_ans / (len(total_calls) - aband_on_que_less_20_sec)) * 100
    service_level_less_than_20_sec_percentage = (count_calls_ans_sl_less_than_20 / (
            len(total_calls) - count_aband_on_que_less_20_sec)) * 100

    # calculations for less than 10 sec calls ans
    calls_ans_sl_less_than_10 = count_calls_ans_sl_less_than_10
    service_level_less_than_10_sec = (count_calls_ans_sl_less_than_10 / len(total_calls)) * 100
    service_level_less_than_10_sec_percentage = (count_calls_ans_sl_less_than_10 / (
            len(total_calls) - count_aband_on_que_less_10_sec)) * 100
    aband_on_que_less_10_sec = count_aband_on_que_less_10_sec
    aband_on_que_less_10_sec_percentage = (aband_on_que_less_10_sec / len(total_calls)) * 100

    records = dict()
    records = {'day': 'Total', 'calls_offered': offered_calls, 'calls_answered': calls_ans,
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
               'service_level_less_than_10_sec': service_level_less_than_10_sec,
               'service_level_less_than_10_sec_percentage': truncate(service_level_less_than_10_sec_percentage, 2),
               'abandoned_less_than_10_sec': aband_on_que_less_10_sec,
               'aband_on_que_less_10_sec_percentage': truncate(aband_on_que_less_10_sec_percentage, 2)}

    return records


# calls offered for lifestyle inbound by time
def calls_offered(d_1, time_n_data):
    m_s_d_1 = '00:00'
    m_s_d_2 = '59:59'
    d_2 = datetime.datetime.strptime(str(d_1), '%Y-%m-%d')
    d_2 = d_2.strftime('%Y-%m-%d')
    a = []
    records = dict()
    for hour in range(10, 24):
        count_aband_on_que, count_ans_calls, count_agent_ans_and_transf = 0, 0, 0
        start_hour = hour
        end_hour = hour
        time_in_hours = str(hour) + '_' + str((hour + 1))
        result = time_n_data.filter(
            Queue_Entry_Time__range=(str(d_1) + ' ' + str(start_hour)
                                     + ':' + m_s_d_1, d_2 + ' ' + str(end_hour) + ':' + m_s_d_2))
        for i in result:
            date_month = findDay(datetim=i.Queue_Entry_Time)
            d = date_month[2]
            if i.Status == 'ABANDONED ON QUEUE':
                count_aband_on_que += 1

            if i.Status == 'AGENT ANSWERED':
                count_ans_calls += 1

            if i.Status == 'AGENT ANSWERED AND TRANSFERRED':
                count_agent_ans_and_transf += 1

            records['date_month'] = d
        records[time_in_hours] = count_aband_on_que + count_ans_calls + count_agent_ans_and_transf
        a.append(count_aband_on_que + count_ans_calls + count_agent_ans_and_transf)
    records['count'] = reduce((lambda x, y: x + y), a)
    return records


# total calls offered counts by time for lifestyle cdr
def total_calls_offered(calls_offer):
    count, c_10_11, c_11_12, c_12_13, c_13_14, c_14_15, c_15_16, c_16_17, c_17_18, c_18_19, c_19_20, c_20_21, c_21_22 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    for i in calls_offer:
        count += i['count']
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
    data = {'date_month':'Total', 'count':count, '10_11':c_10_11, '11_12':c_11_12, '12_13':c_12_13, '13_14':c_13_14,
            '14_15':c_14_15, '15_16':c_15_16, '16_17':c_16_17, '17_18':c_17_18, '18_19':c_18_19,
            '19_20':c_19_20, '20_21':c_20_21, '21_22':c_21_22}
    return data

def dat(cdr_life):
    array, date_month, time_array, inbound_record, inbound_calls_offered = [], [], [], [], []
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
    inbound_record.append(total_lifestyle_inbound_performance(date_n_data=cdr_life))  # appending total record details into inbound

    # lifestyle offered calls between time
    for d_1 in array:
        result_2 = calls_offered(d_1, time_n_data=cdr_life)
        inbound_calls_offered.append(result_2)
    inbound_calls_offered.append(total_calls_offered(calls_offer=inbound_calls_offered))

    return inbound_record, inbound_calls_offered
