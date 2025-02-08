from locust import User, between, SequentialTaskSet, task


class SearchProduct(SequentialTaskSet):
    @task
    def search_men_products(self):
        print("Searching men products")

    @task
    def search_kids_products(self):
        print("Searching kids products")


class ViewCart(SequentialTaskSet):
    @task
    def get_cart_items(self):
        print("Get all cart items")

    @task
    def search_cart_item(self):
        print("Searching item from cart")


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchProduct, ViewCart]

##Disadvantage: Here it will only pick tasks from one TaskSetClass
