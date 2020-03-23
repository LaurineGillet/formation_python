from datetime import datetime

today = datetime.now()
birthday = datetime(2020, 5, 3)

c = birthday - today

print("Mon anniversaire est dans : ", c)