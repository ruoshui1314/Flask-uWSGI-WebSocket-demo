Flask-uWSGI-WebSocket-demo
=====================
Demo provide you a websocket server based on
`flask-uwsgi-websocket
<https://github.com/zeekay/flask-uwsgi-websocket/>`_.
It supports pubsub by redis instead of subscribing channel peer connection by creating asyncio task.
For same channels, SUBSCRIBE module will add it to set and subscribe once to redis.
Chat server will provide interface for different functions (only chat supplied currently).

Attention:Run it with python3 and pip3.

Installation
------------
Preferred method of installation is via pip::

    $ pip install Flask-uWSGI-WebSocket

Installing uWSGI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Of course you'll also need uWSGI (with SSL support, at minimum). It can also be
installed with pip::

    $ pip install uwsgi

If you are installing uWSGI into a virtualenv, the process is::

    $ python3 -m venv pyvenv
    $ . pyvenv/bin/activate
Now it is same as above.

Deployment
----------
You can use uWSGI's built-in HTTP router to get up and running quickly::

    $ uwsgi --http localhost:5000 --http-websockets --master  --gevent 100 --wsgi chat_websocket:app --python-autoreload 1

...or::

    app.run(debug=True, gevent=100)