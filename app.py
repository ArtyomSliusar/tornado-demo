from uuid import uuid4
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url
from tornado.websocket import WebSocketHandler
from pika_client import PikaClient


class WsHandler(WebSocketHandler):

    def _get_sess_id(self):
        return self.sess_id

    def check_origin(self, origin):
        return True

    def open(self):
        self.sess_id = uuid4().hex
        self.application.pc.register_websocket(self._get_sess_id(), self)

    def on_message(self, message):
        self.application.pc.redirect_incoming_message(self._get_sess_id(), message)

    def on_close(self):
        """
        remove connection from pool on connection close.
        """
        self.application.pc.unregister_websocket(self._get_sess_id())


class RootHandler(RequestHandler):

    def get(self):
        self.render("index.html")


settings = {
    "static_path": "static/",
    "template_path": "templates/",
    "debug": True
}


def make_app():
    return Application([
        url(r"/", RootHandler),
        url(r"/ws", WsHandler),
    ], **settings)


def main():
    my_ioloop = IOLoop.current()

    # setup pika client
    pc = PikaClient(my_ioloop)
    app = make_app()
    app.pc = pc
    pc.connect()
    app.listen(8888)
    my_ioloop.start()


if __name__ == '__main__':
    main()
