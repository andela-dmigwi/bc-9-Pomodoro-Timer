import sqlite3 as lite
import sys

#statusuuid
# active = 37806757-4391-4c40-8cae-6bbfd71e893e
# pending = 0eaec4f3-c524-40ab-b295-2db5cb7a0770
# finished = f82db8cc-a969-4495-bffd-bb0ce0ba877a
# unknown = 6c25b6d2-75cc-42c3-9c8c-ccf7b54ba585

#sounduuid
# on = 510b9503-7899-4d69-83c0-690342daf271
# off = 05797a63-51f5-4c1d-9068-215c593bba8d

def initialize_n_create_db():
	'''
	This is a script that creates a database called pomodoro 
	with a table called timer_details. The timer_details
	table is populated with dummy data that will be used 
	for testing
	'''

	try:
		print 'Initialize database Creation'

		con = lite.connect(r'pomodoro.db')
		cur = con.cursor()
		cur.executescript("""
			DROP TABLE IF EXISTS timer_details;
	        CREATE TABLE timer_details(uuid TEXT, title TEXT, start_time TIMESTAMP, duration INT, shortbreak INT,
	        				longbreak INT, cycle INT, statusuuid TEXT, sounduuid TEXT);

	        INSERT INTO timer_details VALUES('12f63828-e21a-40c1-ab43-5f4dd5a5dd8a', 'presentn1', 1472026136, 25, 3, 10, 1, 
	        					'0eaec4f3-c524-40ab-b295-2db5cb7a0770', '510b9503-7899-4d69-83c0-690342daf271');

			INSERT INTO timer_details VALUES('d57037fe-df12-4ca5-abff-1dd626cba2b5', 'presentn2', 1472026236, 30, 5, 14, 2,
								'37806757-4391-4c40-8cae-6bbfd71e893e', '510b9503-7899-4d69-83c0-690342daf271');

			INSERT INTO timer_details VALUES('8cb1795f-a50b-40a6-b2b7-6843602ad95c', 'exercise', 1472026336, 10, 4, 20, 3,
								'0eaec4f3-c524-40ab-b295-2db5cb7a0770', '05797a63-51f5-4c1d-9068-215c593bba8d');

			INSERT INTO timer_details VALUES('78d9d2bc-6fd3-4fad-94cc-b706aa91f57e', 'learning', 1472026436, 15, 5, 15, 2,
								'37806757-4391-4c40-8cae-6bbfd71e893e', '510b9503-7899-4d69-83c0-690342daf271');

			INSERT INTO timer_details VALUES('9bffb77d-569f-491e-8713-7bad9adfefa6', 'revision', 1472026536, 5, 6, 15, 1,
								'f82db8cc-a969-4495-bffd-bb0ce0ba877a', '05797a63-51f5-4c1d-9068-215c593bba8d');

			""")
		con.commit()

		print 'Database timer_details creation finished succes!!'

	except lite.Error, e:
		
		print 'Error %s ocurred : Database Creation failed!!!'%e.arg[0]
