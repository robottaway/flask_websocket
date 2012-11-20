# coding: utf-8
import json
from junk import rclient

def handle_websocket(ws):
    rclient.set('somekey', '0')
    while True:
        message = ws.receive()
        if message is None:
            break
        else:
            message = json.loads(message)
            r  = "I have received this message #%s from you : %s" % (rclient.get('somekey'), message)
            ws.send(json.dumps({'output': r}))
            rclient.incr('somekey')
