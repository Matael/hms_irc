import logging


def get_logger():
    return logging.getLogger(__name__)


def msg_to_privmsg(msg):
    """Extract the PRIVMSG content from the RabbitMQ message."""
    return '[reddit /u/{}] {} {}'.format(
        msg['author'], msg['title'], msg['url'])


def handle(irc_server, irc_chan, msg):

    irc_server.privmsg(irc_chan, msg_to_privmsg(msg))

    get_logger().info('Posted reddit link {} from {}'.format(
        msg['id'], msg['author']))
