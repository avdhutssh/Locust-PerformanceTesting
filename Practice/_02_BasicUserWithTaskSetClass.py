from locust import task, User, between, TaskSet


class SearchProduct(TaskSet):
    @task
    def search_men_products(self):
        print("Searching men products")

    @task
    def search_kids_products(self):
        print("Searching kids products")


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct]

##User and tasks in different class
