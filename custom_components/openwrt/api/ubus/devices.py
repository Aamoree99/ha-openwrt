# mypy: disable-error-code="attr-defined"
from __future__ import annotations

import contextlib
import logging
from typing import Any

from ..base import (
    ConnectedDevice,
    DhcpLease,
    IpNeighbor,
    LldpNeighbor,
)
from .exceptions import (
    UbusAuthError,
    UbusConnectionError,
    UbusError,
    UbusPermissionError,
    UbusSslError,
    UbusTimeoutError,
)

_LOGGER = logging.getLogger(__name__)
UBUS_JSONRPC_VERSION = "2.0"
UBUS_ID_AUTH = 1
UBUS_ID_CALL = 2

SPLACEHOLDER_DEVICES_PY