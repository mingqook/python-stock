import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2723368580038-2727131983477-Vd6TIL7MwVUNqaIvw5yt2PSj"
 
post_message(myToken,"#python-stock","hello slack!")
