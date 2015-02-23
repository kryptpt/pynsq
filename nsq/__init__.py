from __future__ import absolute_import

import signal
import tornado.ioloop
import logging

from nsq import protocol
from nsq.message import Message
from nsq.backoff_timer import BackoffTimer
from nsq.sync import SyncConn
from nsq.async import AsyncConn
from nsq.reader import Reader
from nsq.legacy_reader import LegacyReader
from nsq.writer import Writer
from nsq.version import __version__  # NOQA


def _handle_term_signal(sig_num, frame):
    logging.getLogger(__name__).info(
        'TERM Signal handler called with signal %r', sig_num
    )
    tornado.ioloop.IOLoop.instance().stop()


def run():
    """
    Starts any instantiated :class:`nsq.Reader` or :class:`nsq.Writer`
    """
    signal.signal(signal.SIGTERM, _handle_term_signal)
    tornado.ioloop.IOLoop.instance().start()


__author__ = "Matt Reiferson <snakes@gmail.com>"
__all__ = ["Reader", "Writer", "run", "BackoffTimer", "Message", "Error", "LegacyReader",
           "SyncConn", "AsyncConn", "unpack_response", "decode_message",
           "identify", "subscribe", "ready", "finish", "touch", "requeue", "nop", "pub", "mpub",
           "valid_topic_name", "valid_channel_name",
           "FRAME_TYPE_RESPONSE", "FRAME_TYPE_ERROR", "FRAME_TYPE_MESSAGE"]
