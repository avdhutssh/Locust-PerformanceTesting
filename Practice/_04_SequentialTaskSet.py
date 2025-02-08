from locust import User, between, SequentialTaskSet, task


class SearchProduct(SequentialTaskSet):
    @task
    def search_men_products(self):
        print("Searching men products")

    @task
    def search_kids_products(self):
        print("Searching kids products")


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct]

##User and SequentialTaskSet tasks in different class
