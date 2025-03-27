import logging
import random  # noqa
import time
import pytest

import requests
import urllib3
from locust import HttpUser, task, SequentialTaskSet
from locust.exception import StopUser

# Disable warnings of unverified HTTPS requests (i.e. verify = False)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class DMS(HttpUser):
    @task
    class MainAPIs(SequentialTaskSet):

        # def on_start(self) -> None:
        #     # data = {"Username": "aisultan", "Password": "ais"}
        #     # headers_type = {"Content-Type": "application/json"}
        #     # response = requests.post(
        #     #     "https://dev-api.mycar.kz/mymapping/supersecretadmin/login/",
        #     #     headers=headers_type,
        #     #     json=data,
        #     #     verify=False,
        #     # )
        #     # result = response.json()
        #     # self.token = result["access"]
        #     # logging.info(f"Token: {self.token}")
        #
        #     # Pause for a bit for token to become valid
        #     # time.sleep(5)
        #     #
        #     # logging.info(
        #     #     f"Running tasks sequentially: {self.user=}, {len(self.tasks)=}"
        #     # )

        @task
        def get_mapper_mapping(self):
            data = {
                "mark": {
                    "name": "BMW"
                },
                "model": {
                    "name": "X5"
                },
                "generation": {
                    "name": "I E71 [рестайлинг]"
                },
                "color": {
                    "name": "черный"
                }
            }
            response = self.client.post(
                "https://api.mycar.kz/mymapping/v1/mapper/find/",
                verify=False,
                json=data
            )
            print (response.text)
            return response

        #
        # @task
        # def done(self):
        #     logging.info(f"Stopping and quitting the user {self.user}")
        #     raise StopUser()
