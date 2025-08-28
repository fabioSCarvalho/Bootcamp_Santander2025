import pytz
from datetime import datetime

date = datetime.now(pytz.timezone("Europe/Oslo"))
date2 = datetime.now(pytz.timezone("America/Sao_Paulo"))


print(date)
print(date2)


