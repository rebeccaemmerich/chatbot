"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json
import datetime

@route('/', method='GET')
def index():
    return template("chatbot.html")

cu = ['shit', 'fuck', 'hell', 'bitch', 'ass']


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    if any(x in user_message for x in cu):
        return curse()
    elif str(user_message).find("?") != -1:
        return question(user_message)
    return message(user_message)


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


def curse():
        word = "SORRY I DON'T RESPOND TO RUDE MESSAGES"
        anm = "crying"
        return json.dumps({"animation": anm, "msg": word})


def question(user_message):
        if str(user_message).find("time") != -1:
            word = str(datetime.datetime.now())
            anm = "takeoff"
        else:
            word = "Think of a better  question"
            anm = 'bored'
        return json.dumps({"animation": anm, "msg": word})

def message(user_message):
    word = ''
    anm = ''
    afraid = ['scary','monster', 'scared','afraid','terror']

    money = ['rich','business','pay','money']
    default = "I'm sorry, I don't know what you mean by that"

    if str(user_message).find("name") != -1:
        word = "Nice to meet you!"
        anm = "excited"
    elif str(user_message).find("joke") != -1:
        word = "I don't know any jokes"
        anm = "giggling"
    elif any(x in user_message for x in money):
        word = "Good for you"
        anm = "money"
    elif str(user_message).find("love") != -1:
        word = "That's nice"
        anm = "inlove"
    elif str(user_message).find("sad") != -1:
        word = "I'm sorry to hear that"
        anm = "crying"
    elif str(user_message).find("funny") != -1:
        word = "That is funny"
        anm = "laughing"
    elif any(x in user_message for x in afraid):
        word = "AH SCARY"
        anm = "afraid"
    elif str(user_message).find("you") != -1:
        word = "Thanks! Really means a lot"
        anm = "dancing"
    elif str(user_message).find("pets") != -1:
        word = "I love animals"
        anm = "dog"
    else:
        word = default
        anm = "confused"
    return json.dumps({"animation": anm, "msg":word})

@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
