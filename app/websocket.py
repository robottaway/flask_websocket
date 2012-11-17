# coding: utf-8
import json

def handle_websocket(ws):
    count = 0
    while True:
        message = ws.receive()
        if message is None:
            break
        else:
            message = json.loads(message)
            print message

            r  = "I have received this message #%s from you : %s" % (count, message)
            r += "<br>Glad to be your webserver."
            ws.send(json.dumps({'output': r}))
            count = count + 1
