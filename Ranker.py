import sqlite3
import time 
import re
import urllib2
import json
import string

db = sqlite3.connect("Players.db")
cursor = db.cursor()
cursor.execute("delete from Players")
comparison = re.compile(r'^(?P<name>.+?) - (?P<IGN>.+?$)')
f = open('output.txt','w')

file = open(sys.argv[0])
for line in file:
	m=comparison.search(line)
	try:
		corrected = m.group('IGN').replace(" ", "")
		url = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/"+corrected+"?api_key=7aaa05ad-dd5a-4c3c-bcdc-0217086c681f"
		response = urllib2.urlopen(url)
		json_string = response.read()
		parsed_json = json.loads(json_string)
		ids = str(parsed_json[string.lower(corrected)]['id'])
		try:
			url = "https://na.api.pvp.net/api/lol/na/v2.4/league/by-summoner/"+ ids + "?api_key=7aaa05ad-dd5a-4c3c-bcdc-0217086c681f"
			response = urllib2.urlopen(url)
			json_string = response.read()
			parsed_json = json.loads(json_string)
			query = "INSERT INTO Players (Real_Name, IGN_main, Rank_main) VALUES ('" + m.group('name') + "','" +m.group('IGN') + "','"+parsed_json[ids][0]['tier']+"')" 
		except:
			query = "INSERT INTO Players (Real_Name, IGN_main, Rank_main) VALUES ('" + m.group('name') + "','" +m.group('IGN') + "','UNRANKED')" 
		print query
		result = cursor.execute(query)
		time.sleep(2)
		db.commit()
	except: 
		pass
query = "SELECT Real_Name, IGN_main FROM Players where Rank_main='UNRANKED'"
result = cursor.execute(query)
Players = cursor.fetchall()
print >> f, "Unranked players: "
print >> f
for Player in Players:
	print >> f, str(Player[0]) + " - " + str(Player[1]) 
print >> f

query = "SELECT Real_Name, IGN_main FROM Players where Rank_main='BRONZE'"
result = cursor.execute(query)
Players = cursor.fetchall()
print >> f, "Bronze players: "
print >> f
for Player in Players:
	print >> f, str(Player[0]) + " - " + str(Player[1]) 
print >> f

query = "SELECT Real_Name, IGN_main FROM Players where Rank_main='SILVER'"
result = cursor.execute(query)
Players = cursor.fetchall()
print >> f, "Silver players: "
print >> f
for Player in Players:
	print >> f, str(Player[0]) + " - " + str(Player[1]) 
print >> f

query = "SELECT Real_Name, IGN_main FROM Players where Rank_main='GOLD'"
result = cursor.execute(query)
Players = cursor.fetchall()
print >> f, "Gold players: "
print >> f
for Player in Players:
	print >> f, str(Player[0]) + " - " + str(Player[1]) 
print >> f

query = "SELECT Real_Name, IGN_main FROM Players where Rank_main='PLATINUM'"
result = cursor.execute(query)
Players = cursor.fetchall()
print >> f, "Platinum players: "
print >> f
for Player in Players:
	print >> f, str(Player[0]) + " - " + str(Player[1]) 
print >> f

query = "SELECT Real_Name, IGN_main FROM Players where Rank_main='DIAMOND'"
result = cursor.execute(query)
Players = cursor.fetchall()
print >> f, "Diamond players: "
print >> f
for Player in Players:
	print >> f, str(Player[0]) + " - " + str(Player[1])
print >> f

query = "SELECT Real_Name, IGN_main FROM Players where Rank_main='CHALLENGER'"
result = cursor.execute(query)
Players = cursor.fetchall()
print >> f, "Challenger players: "
print >> f
for Player in Players:
	print >> f, str(Player[0]) + " - " + str(Player[1]) 
print >> f

