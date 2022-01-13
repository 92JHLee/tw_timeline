from datetime import datetime

import tweepy
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]

json_file_name = 'spreadtest-337315-1e7666f53a48.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)

#트위터 api, access token 저장, api 소환!
api_key = ''
api_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


spreadsheet_url = "1AV1ZAzqHroreRq99h3Whs97gxDulaIORsCHxtpCBavk"
doc = gc.open_by_key(spreadsheet_url) #스프레드시트 문서 가져오기

worksheet = doc.worksheet('시트2')

statuses = api.home_timeline(since_id="1481532352761593856", count=200)


tmline = list([status.user.name, str(status.created_at), status.text] for status in statuses)

worksheet.update('B2:D300', tmline)