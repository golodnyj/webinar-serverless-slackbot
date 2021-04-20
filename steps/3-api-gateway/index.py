import json
def handler(event, context):
    print(f"Received event:\n{event}\nWith context:\n{context}")

    slack_body = event.get("body")
    slack_event = json.loads(slack_body)
    challenge_answer = slack_event.get("challenge")

    return {
        'statusCode': 200,
        'body': challenge_answer
    }
