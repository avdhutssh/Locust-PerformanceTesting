from locust import task, User, between, TaskSet


class SearchProduct(TaskSet):
    @task(3)
    def search_men_products(self):
        print("Searching men products")

    @task(1)
    def search_kids_products(self):
        print("Searching kids products")


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct]

##User and tasks in different class
