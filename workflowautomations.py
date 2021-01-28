from locust import HttpUser, task
from datetime import datetime
from locust.env import Environment

class Workflows(HttpUser):
    min_wait = 50
    max_wait = 100
    host = 'https://api.nylas.com'
    def on_start(self):
        self.calendar_id = 'please enter a valid value here'

    @task
    def create_workflow(self):
        print("creating workflow")
        now = int(datetime.now().timestamp())
        start_time = now + 62*60
        end_time = start_time + 30*60
        token = "please enter a valid token"
        jsonStr = self.payload(start_time, end_time)
        response = self.client.post(url="/workflows", json=jsonStr, headers={
            "Authorization": "Bearer {}".format(token),
            "content-type": "application/json"
        })
        print("request path {} data {}".format(response.request.path_url, response.request.body))
        print("status {} data {}".format(response.status_code, response.content))
        print(response)

    def payload(self, start_time, end_time):
        jsonStr = {
            "template": "calendar-event-reminder",
            "data": {
                "create_calendar_event": {
                    "title": "The Package",
                    "when": {
                        "start_time": start_time,
                        "end_time": end_time
                    },
                    "location": "Coffee Shop at mandalore",
                    "calendar_id": self.calendar_id,
                    "participants": [
                        {
                            "email": "mandalorianchitresh@gmail.com",
                            "name": "Chitresh Mandalorian",
                            "phone_number": "+12056496996"
                        }
                    ]
                },
                "reminders": [
                    {
                        "type": "email",
                        "time_before_event": "60",
                        "subject": "May the force be with you.",
                        "body": "We need to ship Baby yoda to Jedi temple"
                    },
                    {
                        "type": "webhook",
                        "time_before_event": "60",
                        "url": "https://hooks.slack.com/services/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",
                        "payload": "{\"text\" : \"we need to ship baby yoda to jedi temple\"}"
                    },
                    {
                        "type": "sms",
                        "time_before_event": "60",
                        "message": "Hurry! Ship the baby yoda to Jedi temple."
                    }
                ]
            }
        }
        return jsonStr

if __name__ == '__main__':
    print("starting")
    my_env = Environment(user_classes=[Workflows])
    Workflows(my_env).run()