from locust import task, SequentialTaskSet


class NavigateByCategory(SequentialTaskSet):

    @task
    def navigate_to_women_category(self):
        print("Navigating to Women Category ..")
        pass

    @task
    def navigate_to_dresses_category(self):
        print("Navigating to Dresses Category ..")
        pass

    @task
    def navigate_to_shirt_category(self):
        print("Navigating to Shirts Category ..")
        pass

    @task
    def exit_task_execution(self):
        self.interrupt()
