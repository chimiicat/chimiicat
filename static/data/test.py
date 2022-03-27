import pandas
import pygsheets

gc = pygsheets.authorize(service_account_file='./winged-precept-316704-bce0a512e6aa.json')

survey_url = 'https://docs.google.com/spreadsheets/d/1zHDWuemNdDRy_i1Xw-x-r_fZjNuEsAnwgtKV6SrBl-A/edit#gid=0'

sh = gc.open_by_url(survey_url)

ws = sh.worksheet_by_title('VGA')

user_df = ws.get_as_df(start='1A', index_colum=0, empty_value='', include_tailing_empty=False)

print(user_df)

user_df.to_json("vga.json", orient='records')