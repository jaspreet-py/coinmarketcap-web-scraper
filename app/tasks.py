import json
import requests
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta
from scraping import scrape, url

app = Celery("tasks")
app.conf.beat_schedule = {
    "scrape-every-5-seconds": {
        "task": "tasks.update_data",
        "schedule": timedelta(seconds=5)
    }
}

@app.task
def update_data():
    data = scrape(url)
    request = requests.post("http://localhost:8000/app/", data={
        "source": url,
        "data": json.dumps(data),
    })