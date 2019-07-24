# -*- coding:utf-8 -*-
#待解决

from tasks import hello
import schedule
import time

def job():
    print("I'm working...")
    hello.delay()
    print('-'*30)

schedule.every(1).second.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    print('-' * 20)
    time.sleep(2)


