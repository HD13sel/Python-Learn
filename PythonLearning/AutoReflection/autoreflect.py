from datetime import datetime
from arquivo import *


day = datetime.today().date()
month = datetime.today().month
print(month)
print(day)
# arq = f'{day}.txt'
# if not arquivoexiste(arq):
#     criararquivo(arq)
