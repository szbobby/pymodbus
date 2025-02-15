"""TLS communication."""
from __future__ import unicode_literals
from __future__ import absolute_import

import logging
from pymodbus.client.asynchronous.factory.tls import get_factory
from pymodbus.constants import Defaults
from pymodbus.factory import ClientDecoder
from pymodbus.transaction import ModbusTlsFramer

_logger = logging.getLogger(__name__)


class AsyncModbusTLSClient: # pylint: disable=too-few-public-methods
    """ Actual Async TLS Client to be used.

    To use do::

        from pymodbus.client.asynchronous.tls import AsyncModbusTLSClient
    """
    def __new__(cls, scheduler, host="127.0.0.1", port=Defaults.TLSPort, # pylint: disable=too-many-arguments
                framer=None, sslctx=None, certfile=None, keyfile=None,
                password=None, source_address=None, timeout=None, **kwargs):
        """ Scheduler to use:
            - async_io (asyncio)
        :param scheduler: Backend to use
        :param host: Target server's name, also matched for certificate
        :param port: Port
        :param framer: Modbus Framer to use
        :param sslctx: The SSLContext to use for TLS (default None and auto create)
        :param certfile: The optional client's cert file path for TLS server request
        :param keyfile: The optional client's key file path for TLS server request
        :param password: The password for for decrypting client's private key file
        :param source_address: source address specific to underlying backend
        :param timeout: Time out in seconds
        :param kwargs: Other extra args specific to Backend being used
        :return:
        """
        framer = framer or ModbusTlsFramer(ClientDecoder())
        factory_class = get_factory(scheduler)
        yieldable = factory_class(host=host, port=port, sslctx=sslctx,
                                  certfile=certfile, keyfile=keyfile,
                                  password=password, framer=framer,
                                  source_address=source_address,
                                  timeout=timeout, **kwargs)
        return yieldable
