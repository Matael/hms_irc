import logging
import json
import importlib

import irc.bot


def get_logger():
    return logging.getLogger(__name__)


class MyBot(irc.bot.SingleServerIRCBot):

    def __init__(self, channel, nickname, server, port=6667):
        super().__init__([(server, port)], nickname, nickname)
        self.channel = channel
        self.joined = False
        self.serv = None
        self.join_callback = None

    def on_welcome(self, serv, ev):
        self.serv = serv
        get_logger().info("Signed on")
        get_logger().info("Joining {}...".format(self.channel))
        serv.join(self.channel)

    def on_kick(self, serv, ev):
        get_logger().warning("Kicked")
        self.die('got kicked')

    def on_nicknameinuse(self, serv, ev):
        newnick = serv.get_nickname() + '_'
        get_logger().warning("Nick already in use, using {}".format(newnick))
        serv.nick(newnick)

    def on_join(self, serv, ev):
        self.joined = True
        get_logger().info("Joined {}".format(self.channel))

        if self.join_callback is not None:
            self.join_callback()

    def on_disconnect(self, serv, ev):
        get_logger().info("Disconnected")

    def handle_rabbit_msg(self, ch, method, properties, body):

        msg = json.loads(body.decode('utf-8'))

        try:
            module = importlib.import_module(
                'hms_irc.handlers.' + method.routing_key)
            func = getattr(module, 'handle')
            func(self.serv, self.channel, msg)

        except (ImportError, AttributeError) as e:
            get_logger().error(e)
