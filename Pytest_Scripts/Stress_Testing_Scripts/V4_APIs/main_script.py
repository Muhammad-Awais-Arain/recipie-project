from get_login import login
from get_all_news import get_all_news
from get_member_tools import get_member_tools
from get_Navigations import get_navigation
from get_Bills import get_all_bills
from get_albums import get_all_albums
from get_gallery import get_all_gallery
from get_notifications import get_notifications
from get_union_representatives import get_union_representatives
from get_member_discounts import get_member_discounts
from get_all_events import get_all_events
from organize_workplace import organize_workplace
from app_login import app_login
from app_forget_password import forgot_password
from app_register import app_register
from get_my_elected_officials import get_elected_official
from get_all_backend_homesections import get_all_homesections
import sys
import json
import requests

# Perform login and obtain access token and user ID
email = 'henry@mailinator.com'
password = 'henry'
access_token, user_id = login(email, password)

news_output = get_all_news()
navigations_output = get_navigation()
bills_output = get_all_bills()
albums_data = get_all_albums()
gallery_data = get_all_gallery()
notifications_output = get_notifications()
unionrepresentatives_output = get_union_representatives()
memberdiscounts_output = get_member_discounts()
events_output = get_all_events()
organize_workplace_output = organize_workplace()
app_login_api = app_login()
app_forgetpassword = forgot_password()
app_registered = app_register()
elected_official = get_elected_official()

#homesections = get_all_homesections()

# Use the access token and user ID in subsequent API calls
if access_token and user_id:
    member_tools_output = get_member_tools(access_token, user_id)
else:
# the login failure or exit the script
    print('failed')

url = "https://hooks.slack.com/services/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"
headers = {
    "Authorization": "Bearer",
    "Content-Type": "application/json"
}

text = "🚀 *V4 APIs Script* 🚀\n\n"
text += f"💡 *Get News Output (118):*\n```\n{news_output}\n```\n\n"
text += f"🗺️ *Navigation Output (118):*\n```\n{navigations_output}\n```\n\n"
text += f"💰 *Bills Output (118):*\n```\n{bills_output}\n```\n\n"
text += f"🛠️ *Member Tools Output (118):*\n```\n{member_tools_output}\n```\n"
text += f"📸 *Get Albums Result (118):*\n```\n{albums_data}\n```\n"
text += f"🖼️ *Get Gallery Result (118):*\n```\n{gallery_data}\n```\n"
text += f"🔔 *Get Notifications Output (118):*\n```\n{notifications_output}\n```\n"
text += f"👨‍💼 *Get Union Representaive Output (118):*\n```\n{unionrepresentatives_output}\n```\n"
text += f"🛒 *Get Member Discounts Output (118):*\n```\n{memberdiscounts_output}\n```\n"
text += f"📅 *Get All Events (118):*\n```\n{events_output}\n```\n"
text += f"📋 *Get Organize Workplace (118):*\n```\n{organize_workplace_output}\n```\n"
text += f"🔐 *App Login (118):*\n```\n{app_login_api}\n```\n"
text += f"👥 *App Register (118):*\n```\n{app_registered}\n```\n"
text += f"🔓 *App Forget Password (118):*\n```\n{app_forgetpassword}\n```\n"
text += f"🗳️ *Get Elected Official (118):*\n```\n{elected_official}\n```\n"

# text += f"🏠 *All Home Sections Output:*\n```\n{homesections}\n```\n"

payload = {
    "channel": "staging",
    "text": text
}

response = requests.post(url, data=json.dumps(payload), headers=headers)
