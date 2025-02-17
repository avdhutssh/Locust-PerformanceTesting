from locust import HttpUser, between


class RegisteredHttpUser(HttpUser):
    wait_time = between(3, 5)
    abstract = True

    def __init__(self, parent):
        super(RegisteredHttpUser, self).__init__(parent)
        self.user_attr = None

    def on_start(self):
        pass

    def on_stop(self):
        pass
