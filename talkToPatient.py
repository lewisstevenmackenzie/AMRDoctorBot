import requests
import json


def send_utt(user_ID, msg):
    json = {"sender": user_ID, "message": msg}

    response = requests.post("http://localhost:5005/webhooks/rest/webhook", json=json)
    final_json = response.json()
    print(final_json)

    user = user_ID
    message = msg
    resp = final_json[0]["text"]

    with open("./log-rasa-" + user + ".txt", "a") as f:
        output = (
            "USER ID: "
            + user
            + "\nMESSAGE: "
            + message
            + "\nRESPONSE: "
            + resp
            + "\n##########################\n"
        )
        if resp == "Goodbye":
            ended = True
        print(response)
        f.write(output)


ended = False
user_ID = "test"
while ended == False:
    msg = input("Your turn: ")
    send_utt(user_ID, msg)
