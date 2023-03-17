#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  db.py
#  
#  Copyright 2023 deb <deb@deb-ThinkPad-T14-Gen-2a>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('home.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS USER")
cursor_obj.execute("DROP TABLE IF EXISTS PASS")
cursor_obj.execute("DROP TABLE IF EXISTS APPL")
cursor_obj.execute("DROP TABLE IF EXISTS APPLST")
cursor_obj.execute("DROP TABLE IF EXISTS ALARM")

# Creating table
table = """ CREATE TABLE USER (
			Name CHAR(25) NOT NULL,
			Pass VARCHAR(25) NOT NULL,
			Score INT
		); """
		
cursor_obj.execute(table)

table = """ CREATE TABLE PASS (
			Pass VARCHAR(25) NOT NULL,
			Score INT
		); """
		
cursor_obj.execute(table)

table = """ CREATE TABLE APPL (
			Applnum	INTEGER NOT NULL PRIMARY KEY,
			Appl CHAR(25) NOT NULL,
			Room CHAR(25) NOT NULL,
			St BOOLEAN NOT NULL,
			Score INT
		); """

cursor_obj.execute(table)

table = """ CREATE TABLE ALARM (
			Applnum	INTEGER NOT NULL PRIMARY KEY,
			St BOOLEAN NOT NULL,
			Score INT
		); """
		
cursor_obj.execute(table)

#inserting data into geek table

connection_obj.execute("""INSERT INTO USER (Name, Pass,Score) VALUES ("Devanshi","123", 1)""")
connection_obj.execute("""INSERT INTO USER (Name, Pass,Score) VALUES ("Jow","123", 1)""")
connection_obj.execute("""INSERT INTO USER (Name, Pass,Score) VALUES ("Bob","123", 1)""")
connection_obj.execute("""INSERT INTO APPL (Applnum, Appl,Room, St, Score) VALUES (1,"Ligts","BedRoom", 0,0)""")
connection_obj.execute("""INSERT INTO APPL (Applnum, Appl,Room, St, Score) VALUES (2,"Fans","BedRoom", 0,1)""")

connection_obj.commit()


# cursor object
cursor_obj = connection_obj.cursor()

# to select all column we will use
statement = '''SELECT * FROM USER'''

cursor_obj.execute(statement)

print("All the data")
output = cursor_obj.fetchall()
for row in output:
	print(row)

connection_obj.commit()

# Close the connection
connection_obj.close()



