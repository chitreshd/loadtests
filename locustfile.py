from locust import HttpUser, TaskSet, task
from locust.env import Environment

class UserBehavior(TaskSet):
    @task
    def index(self):
        import pdb; pdb.set_trace()
        self.client.get("/")

class WebsiteUser(HttpUser):
    task_set = UserBehavior
    host = 'http://google.com'
    min_wait = 1000
    max_wait = 2000

if __name__ == '__main__':
    my_env = Environment(user_classes=[WebsiteUser])
    WebsiteUser(my_env).run()