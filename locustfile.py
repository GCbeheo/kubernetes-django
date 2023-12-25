import math
from locust import HttpUser, TaskSet, task, between
from locust import LoadTestShape
import random, time

class UserTasks(TaskSet):
    @task
    def get_root(self):
        self.client.get("/")


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    tasks = [UserTasks]

class CustomLoadShape(LoadTestShape):
    """
    A custom load shape class with spawn_rate increasing randomly until reaching 2500 users.
    """
    
    max_users = 2000
    time_limit = 125

    def tick(self):
        run_time = round(self.get_run_time())
        spawn_rate = random.randint(1, self.max_users)

        if run_time < self.time_limit:
            if (self.max_users>self.get_current_user_count()):
                users= min(self.max_users, spawn_rate)
                time.sleep(2)
            else:
                return None
            return (users, spawn_rate)
        else:
            return None
