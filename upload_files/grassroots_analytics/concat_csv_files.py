import os
import glob
import csv
import pandas as pd
import numpy as np


br= "/home/appdevelopement/Desktop/CMT/BREAK"
cdr= "/home/appdevelopement/Desktop/CMT/CDR"
log= "/home/appdevelopement/Desktop/CMT/LOGIN"

def concat_files(br,cdr, log):
    extension = 'csv' # extension for csv files

    # concatenating break report csv files
    os.chdir(br) # loading break report os path
    all_filenames = [pd.read_csv(i).drop(['Agent Name'], axis=1)[:-1]for i in glob.glob('*.{}'.format(extension))]
    break_report = pd.concat(all_filenames) #combine all files in the list
    break_report.to_csv( "/home/appdevelopement/Desktop/break_report.csv", index=False)     #export to csv

    # concatenating cdr csv files
    os.chdir(cdr) # loading cdr report os path
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    new_cdr = pd.DataFrame()
    dst_channel, cdr_destination, date, time, source, source_channel, status, duration, \
    mob_no, call_type = [], [], [], [], [], [], [], [], [], []
    for file in all_filenames:
        cdr = pd.read_csv(file)
        for i in cdr.index:
            new_date, new_time = cdr['Date'][i].split()
            if cdr['Destination'][i] != 's':
                try:
                    # if len(sou) == 4 and int(sou) in range(1001, 1035) and len(str(cdr['Destination'][i])) == 10\
                    #         and isinstance(int(cdr['Destination'][i]), int):
                    sou = int(round(cdr['Source'][i]))
                    if sou in range(1001, 1035) and isinstance(int(cdr['Destination'][i]), int)\
                            and len(str(cdr['Destination'][i])) == 10:
                        new_duration = cdr['Duration'][i].split('s')[0]
                        duration.append(new_duration)
                        date.append(new_date)
                        time.append(new_time)
                        source.append(sou)
                        status.append(cdr['Status'][i])
                        cdr_destination.append(cdr['Destination'][i])
                        dst_channel.append(cdr['Dst. Channel'][i])
                        mob_no.append(cdr['Destination'][i])
                        call_type.append('Outgoing')

                    if int(cdr['Destination'][i]) in range(4000, 4023) and isinstance(int(cdr['Source'][i]), int)\
                            and len(str(sou)) == 10:
                            new_duration = cdr['Duration'][i].split('s')[0]
                            duration.append(new_duration)
                            date.append(new_date)
                            time.append(new_time)
                            source.append(sou)
                            status.append(cdr['Status'][i])
                            cdr_destination.append(cdr['Destination'][i])
                            dst_channel.append(cdr['Dst. Channel'][i].split('/')[1])
                            mob_no.append(cdr['Source'][i])
                            call_type.append('Incoming')
                except ValueError:
                    pass

    new_cdr['date'] = date
    new_cdr['time'] = time
    new_cdr['source'] = source
    new_cdr['destination'] = cdr_destination
    new_cdr['dst_channel'] = dst_channel
    new_cdr['status'] = status
    new_cdr['duration_in_sec'] = duration
    new_cdr['mob_no'] = mob_no
    new_cdr['call_type'] = call_type
    new_cdr.to_csv('/home/appdevelopement/Desktop/cdr.csv', index=False)


    # concatenating login csv files
    os.chdir(log) # loading login os path
    all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
    agent, date_init, date_end = [], [], []
    log = pd.DataFrame() # Creating empty dataframe
    for file in all_filenames:
        login = pd.read_csv(file)
        login_logout = login.iloc[:,:-1][:-1]
        for i in login_logout.index:
            agent.append(login_logout['Agent'][i])
            date_init.append(login_logout['Date Init'][i])
            date_end.append(login_logout['Date End'][i])
    
    # adding data into dataframe
    log['agent'] = agent
    log['date_init'] = date_init
    log['date_end'] = date_end
    log.to_csv("/home/appdevelopement/Desktop/login_logout.csv", index=False)     #export to csv



concat_files(br, cdr, log)
