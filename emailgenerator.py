from locust import HttpUser, task
from datetime import datetime
from locust.env import Environment
from utils import *
import json

class EmailGenerator(HttpUser):
    min_wait = 50
    max_wait = 100
    host = 'https://api.nylas.com'
    def on_start(self):
        self.calendar_id = 'please enter a valid value here'

    @task
    def generate_email(self):
        print("generating email")
        with open('./test_data.json') as f:
            data = json.load(f)

        for token in data["accessTokens"]:
            emails = data["emails"]
            now = int(datetime.now().timestamp())
            jsonStr = email_payload(now, emails)
            response = self.client.post(url="/send", json=jsonStr, headers={
                "Authorization": "Bearer {}".format(token),
                "content-type": "application/json"
            })
            print("request path {} data {}".format(response.request.path_url, response.request.body))
            print("status {} data {}".format(response.status_code, response.content))
            print(response)


if __name__ == '__main__':
    print("starting")
    my_env = Environment(user_classes=[EmailGenerator])
    EmailGenerator(my_env).run()