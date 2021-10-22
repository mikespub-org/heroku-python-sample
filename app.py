import os
import socket
import sys
import time

from flask import Flask, escape, json, request

app = Flask(__name__)


@app.route("/")
def hello():
    # return 'Hello World!'
    info = json.dumps(request.environ, indent=2, default=lambda o: repr(o))
    tmpl = (
        "<h3>Hello {name}!</h3>"
        "<b>Hostname:</b> {hostname}<br/>"
        "<b>File:</b> {file}<br/>"
        "<b>Modified:</b> {date}<br/>"
        "<b>Python:</b> {version}<br/>"
        "<b>Environ:</b> <pre>{environ}</pre>"
    )
    return tmpl.format(
        name=os.getenv("APP_NAME", "World"),
        hostname=socket.gethostname(),
        file=__file__,
        date=time.ctime(os.path.getmtime(__file__)),
        version=escape(sys.version),
        environ=escape(info),
    )


if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
