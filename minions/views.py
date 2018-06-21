#!venv/bin/python
from flask import request
from flask.ext.sqlalchemy import SQLAlchemy
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from minions import app, db
from models import Ambassador, Schedule

@app.route("/sms", methods = ['GET', 'POST'])
def process_request():
	message_body = request.form['Body'].lower().split()
	resp = MessagingResponse()
	command = message_body[0]
	if command.lower() == 'recruit':
		return recruit_minions(message_body, resp)
	elif command.lower() == 'assemble':
	    resp.message("Acknowledged, Chief Youth Inspirer")
	return str(resp)

def recruit_minions(message_body, resp):
	day_of_week = message_body[message_body.index("on") + 1]
	time = message_body[message_body.index("at") + 1]
	if ":" in time:
	    time = time.replace(':', '.')
        start_time = float(time)
	end_time = parse_time(start_time)
	resp.message(get_eligible_minions(day_of_week, start_time, end_time))
	return str(resp)

def parse_time(start):
    start = start + 0.30
    minutes = start % 1
    if minutes >= .6:
	start = start + 1
	minutes = minutes - 60
    return start

def get_eligible_minions(day, session_start, session_end):
    schedules = Schedule.query.filter(Schedule.day == day).filter(Schedule.start<=session_start).filter(Schedule.end >= session_end)
    minions = []
    for schedule in schedules:
    	minion = Ambassador.query.filter(Ambassador.id == schedule.id)[0]
	minions.append(minion)

    if schedules.count() == 0:
	return "No minions are available at that time."
    army_of_nerds = "Here are the available minions: "
    for minion in minions:
	get_nerd_metadata(minion)
	army_of_nerds += minion.name + (":%s " % (get_nerd_metadata(minion))) + "\n\n" 
    return army_of_nerds

def get_nerd_metadata(nerd):
    return("{ rank: %s, ethinicity %s, gender: %s}"% (nerd.rank, nerd.ethnicity, nerd.gender))




