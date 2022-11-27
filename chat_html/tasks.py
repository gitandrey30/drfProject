import datetime
import time

import channels.layers
from asgiref.sync import async_to_sync
from celery import shared_task, app
from django.contrib.sites import requests



channels_layer = channels.layers.get_channel_layer()


@app.task
def summ(x,y):
    time.sleep(3)
    res = x + y
    print(res, 'результат сложения')
    return res


@shared_task
def send_to_chat():
    date = datetime.datetime.now()
    async_to_sync(channels_layer.group_send)(
        'chat_pupsiki',{'type': 'send_timer', 'time': date}
    )
    send_euro.__apply_async(countdown=2)


@shared_task
def send_euro(id):
    euro = requests.get(f'https://www.nbrb.by/api/exrates/rates[/{id}] ')
    async_to_sync(channels_layer.group_send)(
        'chat_pupsiki', {'type': 'send_timer', 'kurs':str(euro)}
    )