from locust import events

from TaskSetLib.CategoryNavigate import NavigateByCategory
from UserLib.GuestHttpUser import GuestHttpUser
from UserLib.RegisteredHttpUser import RegisteredHttpUser


@events.test_start.add_listener
def on_test_start(**kwargs):
    print(kwargs['environment'].host)
    print("......... Initiating Load Test .........")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print("........ Load Test Completed ........")


class UserGroupA(RegisteredHttpUser):
    weight = 5
    RegisteredHttpUser.tasks = [NavigateByCategory]


class UserGroupB(GuestHttpUser):
    weight = 1
    RegisteredHttpUser.tasks = [NavigateByCategory]
