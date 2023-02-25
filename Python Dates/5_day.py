from datetime import date, timedelta

ans = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',ans)