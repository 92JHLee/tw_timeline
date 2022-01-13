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
api_key =
api_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


spreadsheet_url = "https://docs.google.com/spreadsheets/d/1AV1ZAzqHroreRq99h3Whs97gxDulaIORsCHxtpCBavk/edit#gid=0"
doc = gc.open_by_key(spreadsheet_url) #스프레드시트 문서 가져오기

worksheet = doc.worksheet('시트1')

statuses = api.home_timeline(since_id="1481427182131941376",max_id="1481431145480798208")

worksheet.update('B1',statuses)