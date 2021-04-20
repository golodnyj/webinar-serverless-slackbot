import logging
import sys
import os

from kikimr.public.sdk.python import client as ydb

sys.path.insert(1, "vendor")
from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler

# process_before_response must be True when running on FaaS
app = App(process_before_response=True)

def get_config():
    endpoint = os.getenv("ENDPOINT")
    database = os.getenv("DATABASE")
    if endpoint is None or database is None:
        raise AssertionError("Нужно указать обе переменные окружения")
    credentials = ydb.construct_credentials_from_environ()
    return ydb.DriverConfig(endpoint, database, credentials=credentials)

def execute(config, query, params):
    with ydb.Driver(config) as driver:
        try:
            driver.wait(timeout=5)
        except TimeoutError:
            print("Connect failed to YDB")
            print("Last reported errors by discovery:")
            print(driver.discovery_debug_details())
            return None

        session = driver.table_client.session().create()
        prepared_query = session.prepare(query)

        return session.transaction(ydb.SerializableReadWrite()).execute(
            prepared_query,
            params,
            commit_tx=True
        )

def find_name(id):
    config = get_config()
    query = """
        DECLARE $id AS Utf8;

        SELECT name FROM coffee where id=$id;
        """
    params = {'$id': id}

    result_set = execute(config, query, params)
    if not result_set or not result_set[0].rows:
        return None

    return result_set[0].rows[0].name

@app.command("/what-kind-of-coffee")
def respond_to_slack_within_3_seconds(say):
    coffee_name = find_name("1")
    say(f'Today we us {coffee_name}')

SlackRequestHandler.clear_all_log_handlers()
logging.basicConfig(format="%(asctime)s %(message)s", level=logging.DEBUG)

def handler(event, context):
    slack_handler = SlackRequestHandler(app=app)
    return slack_handler.handle(event, context)