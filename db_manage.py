import sqlite3 as lite
import json
import datetime
import pytz
import ast


class DbManage(object):
    '''
    This module will have database operations as directed by the timer module
    '''
     #statusuuid
    active = '37806757-4391-4c40-8cae-6bbfd71e893e'
    pending = '0eaec4f3-c524-40ab-b295-2db5cb7a0770'
    finished = 'f82db8cc-a969-4495-bffd-bb0ce0ba877a'
    running = '6c25b6d2-75cc-42c3-9c8c-ccf7b54ba585'

    #sounduuid
    on = '510b9503-7899-4d69-83c0-690342daf271'
    off = '05797a63-51f5-4c1d-9068-215c593bba8d' 


    def __init__(self):
        self.con = ''
        self.cur = ''

    def connect_db(self):
        self.con = lite.connect('dbase/pomodoro.db')
        with self.con:            
            self.cur = self.con.cursor()
            print '.'*100 

    def get_respective_soundstatus(self, uuid):
        self.connect_db();
        self.cur.execute("SELECT * FROM timer_details WHERE uuid = '%s' AND sounduuid = '%s'"
            %(uuid, DbManage.off))
        data = self.cur.fetchall()
        self.con.close()
        return data       

    def get_all_tasks_by_name(self, title_name):
        self.connect_db();
        self.cur.execute("SELECT * FROM timer_details WHERE title = '%s'"%title_name)
        data = self.cur.fetchall()
        self.con.close()
        return data

    def get_entries_with_status(self, status, title_name =''):
        self.connect_db();
        if title_name == '':
            self.cur.execute("SELECT * FROM timer_details WHERE statusuuid = '%s'" %status)
        else:
            self.cur.execute("SELECT * FROM timer_details WHERE statusuuid = '%s' and title ='%s'"
            %(status,title_name))
        data = self.cur.fetchall()
        self.con.close() 
        return data

    def store_a_new_record(self, record):
        self.connect_db();
        row = []
        row.append(record['uuid'])
        row.append(record['title'])
        row.append(record['start_time'])
        row.append(record['duration'])
        row.append(record['shortbreak'])
        row.append(record['longbreak'])
        row.append(record['cycle'])
        row.append(record['statusuuid'])
        row.append(record['sounduuid'])

        self.cur.execute("INSERT INTO timer_details VALUES(?,?,?,?,?,?,?,?,?)", tuple(row))
        self.con.commit()
        self.con.close()
        

    def update_the_status(self, uuid, status):
        self.connect_db();
        print self.cur.execute("UPDATE timer_details SET statusuuid = '%s' WHERE uuid = '%s'"%(status,uuid))
        self.con.commit()
        self.con.close()

    def retrieve_all_entries(self):
        self.connect_db();
        self.cur.execute("SELECT * FROM timer_details")
        data = self.cur.fetchall()
        self.con.close()
        return self.format_list_items(data)

    def retrieve_entries_past_timestamp(self, timestamp):
        self.connect_db();
        self.cur.execute("SELECT * FROM timer_details WHERE start_time >= '%s'"%timestamp)
        data = self.cur.fetchall()
        self.con.close()
        return self.format_list_items(data)

    def timestamp_to_normal(self, timestamp, form):        
        '''Method coverts timestamp to Normal time'''
        if 'full' in form:            
            time = str(datetime.datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S'))
        else:
            time =  str(datetime.datetime.fromtimestamp(timestamp).strftime('%HHrs %MMin %SSec'))             
        return time

    def format_list_items(self, resultset):
        temp = []
        counter  = 0
        for row in resultset:
            counter =counter +1            
            sublist = []
            status = 'Active'
            sound = 'On'
            sublist.append(counter)

            sublist.append(row[1])

            sublist.append(self.timestamp_to_normal(row[2], 'full'))

            sublist.append(self.timestamp_to_normal(row[3], 'simple'))

            sublist.append(self.timestamp_to_normal(row[4], 'simple'))

            sublist.append(self.timestamp_to_normal(row[5], 'simple'))

            sublist.append(row[6])

            if row[7] == DbManage.pending:
                status = 'Pending' 
            elif row[7] == DbManage.finished: 
                status = 'Finished' 
            elif row[7] == DbManage.running: 
                status = 'Running'            
            sublist.append(status)

            if row[8] == DbManage.off:
                sound = 'Off'
            sublist.append(sound)

            temp.append(tuple(sublist))

        return tuple(temp)

    def populate_temp_dictionaries(self,status):
        temp = {}
        elems = self.get_entries_with_status(status)
        for item in elems:
            temp[item[0]] = item[2] + item[3] + 10800
        return temp


if __name__ == '__main__':
    db = DbManage()
    for iterm in db.retrieve_all_entries():
        print iterm









