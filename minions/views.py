#!venv/bin/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from minions import app

@app.route("/sms", methods = ['GET', 'POST'])
def process_request():
	message_body = request.form['Body'].lower().split()
	resp = MessagingResponse()
	command = message_body[0]
	if command.lower() == 'assemble':
		return recruit_minions(message_body, resp)
	else:
	    resp.message("Acknowledged, Chief Youth Inspirer")
	return str(resp)

def recruit_minions(message_body, resp):
	day_of_week = message_body[message_body.index("on") + 1]
	time = message_body[message_body.index("at") + 1]
	if ":" in time:
	    time = time.replace(':', '.')
        resp.message("recruit minions on " + day_of_week + " at " + time)
	return str(resp)
