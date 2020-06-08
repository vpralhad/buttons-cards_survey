# -*- coding: utf-8 -*-

"""
Sample code for using webexteamsbot
"""

import os
import requests
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
import sys
import json
import payloads
import csv
import os
from datetime import date
from pprint import pprint

from simple_smartsheet import Smartsheet
from simple_smartsheet.models import Sheet, Column, Row, Cell, ColumnType

# Retrieve required details from environment variables
bot_email = os.getenv("TEAMS_BOT_EMAIL")
teams_token = os.getenv("TEAMS_BOT_TOKEN")
bot_url = os.getenv("TEAMS_BOT_URL")
bot_app_name = os.getenv("TEAMS_BOT_APP_NAME")
#sheet_link = "https://app.smartsheet.com/sheets/HFR56Jxm2jHgQwCWw2vX4rCx3x49VMjFMV36mfR1"
TOKEN = "hrol393n3zawzkdlezm2nj6l89"
SHEET_NAME = "devnetsurvey"
smartsheet = Smartsheet(TOKEN)
sheet = smartsheet.sheets.get(SHEET_NAME)

# Example: How to limit the approved Webex Teams accounts for interaction
#          Also uncomment the parameter in the instantiation of the new bot
# List of email accounts of approved users to talk with the bot
# approved_users = [
#     "josmith@demo.local",
# ]

# If any of the bot environment variables are missing, terminate the app
if not bot_email or not teams_token or not bot_url or not bot_app_name:
    print(
        "sample.py - Missing Environment Variable. Please see the 'Usage'"
        " section in the README."
    )
    if not bot_email:
        print("TEAMS_BOT_EMAIL")
    if not teams_token:
        print("TEAMS_BOT_TOKEN")
    if not bot_url:
        print("TEAMS_BOT_URL")
    if not bot_app_name:
        print("TEAMS_BOT_APP_NAME")
    sys.exit()

# Create a Bot Object
#   Note: debug mode prints out more details about processing to terminal
#   Note: the `approved_users=approved_users` line commented out and shown as reference
bot = TeamsBot(
    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
    debug=True,
    # approved_users=approved_users,
    webhook_resource_event=[
        {"resource": "messages", "event": "created"},
        {"resource": "attachmentActions", "event": "created"},
    ],
)


# Create a custom bot greeting function returned when no command is given.
# The default behavior of the bot is to return the '/help' command response
def greeting(incoming_msg):
    # Loopkup details about sender
    sender = bot.teams.people.get(incoming_msg.personId)

    # Create a Response object and craft a reply in Markdown.
    response = Response()
    response.markdown = "Hello {}, I'm a DevNet Survey bot. ".format(sender.firstName)
    response.markdown += "type **/survey** to start the survey using form."
    return response


# Create functions that will be linked to bot commands to add capabilities
# ------------------------------------------------------------------------


# This function generates a basic adaptive card and sends it to the user
# You can use Microsofts Adaptive Card designer here:
# https://adaptivecards.io/designer/. The formatting that Webex Teams
# uses isn't the same, but this still helps with the overall layout
# make sure to take the data that comes out of the MS card designer and
# put it inside of the "content" below, otherwise Webex won't understand
# what you send it.
def show_card(incoming_msg):
    attachment = payloads.survey_payload
    backupmessage = "This is DevNet Survey Adaptive Cards."

    c = create_message_with_attachment(
        incoming_msg.roomId, msgtxt=backupmessage, attachment=attachment
    )
    print(c)
    return ""


# An example of how to process card actions
def handle_cards(api, incoming_msg):
    """
    Sample function to handle card actions.
    :param api: webexteamssdk object
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    m = get_attachment_actions(incoming_msg["data"]["id"])
    #with open('devnetsurvey.csv', 'a') as file:
        #data = json.dumps(m["inputs"])
    data = m["inputs"]
        #file.write(data)
        #print(type(data))
        #writer = csv.writer(file)
        #for value in m:
        #writer.writerow(m["inputs"])
    new_rows = [
        Row(
            to_top=True,
            cells=sheet.make_cells(
                {"Your name": data["Name"],
                "Website": data["how_web"],
                "Getting set up and verifying the lab environment" : data["lab_setup"],
                "Python Fundamentals" : data["python"],
                "REST API fundamentals" : data["restapi"],
                "Model-Driven Programmability" : data["model_driven"],
                "Model-Driven Programmability: the MISSION" : data["model_driven_mission"],
                "Guest Shell" : data["guest_shell"],
                "Guest Shell: the MISSION" : data["guest_shell_mission"],
                "NFVIS" : data["nfvis"],
                "NFVIS: the MISSION" : data["nfvis_mission"],
                "Understanding of DNA before" : data["before"],
                "Understanding of DNA after" : data["after"],
                "General comments" : data["comments"]
                }
            ),
        ),
    ]

    smartsheet.sheets.add_rows(sheet.id, new_rows)
    return "Thank you for submitting the Survey!!"
    #return "FOllowing Info Added - {}".format(m["inputs"]["comments"])


# Temporary function to send a message with a card attachment (not yet
# supported by webexteamssdk, but there are open PRs to add this
# functionality)
def create_message_with_attachment(rid, msgtxt, attachment):
    headers = {
        "content-type": "application/json; charset=utf-8",
        "authorization": "Bearer " + teams_token,
    }

    url = "https://api.ciscospark.com/v1/messages"
    data = {"roomId": rid, "attachments": [attachment], "markdown": msgtxt}
    response = requests.post(url, json=data, headers=headers)
    return response.json()


# Temporary function to get card attachment actions (not yet supported
# by webexteamssdk, but there are open PRs to add this functionality)
def get_attachment_actions(attachmentid):
    headers = {
        "content-type": "application/json; charset=utf-8",
        "authorization": "Bearer " + teams_token,
    }

    url = "https://api.ciscospark.com/v1/attachment/actions/" + attachmentid
    response = requests.get(url, headers=headers)
    return response.json()


# Set the bot greeting.
bot.set_greeting(greeting)

# Add new commands to the bot.
bot.add_command("attachmentActions", "*", handle_cards)
bot.add_command("/survey", "start a survey", show_card)
# Every bot includes a default "/echo" command.  You can remove it, or any
# other command with the remove_command(command) method.
bot.remove_command("/echo")

if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=7000)
