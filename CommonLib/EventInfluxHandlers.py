import json
import pytz
import datetime
import socket
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from locust import events


class EventInfluxHandlers:
    hostname = socket.gethostname()

    # InfluxDB v2.x connection details
    url = "http://localhost:8086"
    token = "4rUTe07tHIuT_Zbp3FDzUOI8htzk-ugCT9S9kYmmaGt9Q_YmchZ66i_CV0P-Z7TioFTuEBgqVHn5lDah4oXCTQ=="
    org = "demo"
    bucket = "locust"
    measurement = "REST_Table"

    # Create client connection
    client = InfluxDBClient(url=url, token=token, org=org)
    write_api = client.write_api(write_options=SYNCHRONOUS)

    @staticmethod
    def init_influx_client():
        # Create bucket if it doesn't exist
        buckets_api = EventInfluxHandlers.client.buckets_api()
        bucket_names = [bucket.name for bucket in buckets_api.find_buckets().buckets]

        if EventInfluxHandlers.bucket not in bucket_names:
            organization_api = EventInfluxHandlers.client.organizations_api()
            org_id = organization_api.find_organizations(org=EventInfluxHandlers.org)[0].id
            buckets_api.create_bucket(bucket_name=EventInfluxHandlers.bucket, org_id=org_id)

    @staticmethod
    @events.request_success.add_listener
    def request_success_handlers(request_type, name, response_time, response_length, **kwargs):
        point = Point(EventInfluxHandlers.measurement) \
            .tag("hostname", EventInfluxHandlers.hostname) \
            .tag("requestName", name) \
            .tag("requestType", request_type) \
            .tag("status", "PASS") \
            .field("responseTime", float(response_time)) \
            .field("responseLength", int(response_length)) \
            .time(datetime.datetime.now(tz=pytz.UTC))

        EventInfluxHandlers.write_api.write(
            bucket=EventInfluxHandlers.bucket,
            org=EventInfluxHandlers.org,
            record=point
        )

    @staticmethod
    @events.request_failure.add_listener
    def request_failure_handlers(request_type, name, response_time, response_length, exception, **kwargs):
        point = Point(EventInfluxHandlers.measurement) \
            .tag("hostname", EventInfluxHandlers.hostname) \
            .tag("requestName", name) \
            .tag("requestType", request_type) \
            .tag("status", "FAIL") \
            .tag("exception", str(exception)) \
            .field("responseTime", float(response_time)) \
            .field("responseLength", int(response_length) if response_length is not None else 0) \
            .time(datetime.datetime.now(tz=pytz.UTC))

        EventInfluxHandlers.write_api.write(
            bucket=EventInfluxHandlers.bucket,
            org=EventInfluxHandlers.org,
            record=point
        )
