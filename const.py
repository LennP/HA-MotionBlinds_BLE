"""Constants for the MotionBlinds BLE integration."""

from enum import StrEnum

ATTR_CONNECTION_TIMEOUT = "connection_timeout"
ATTR_CONNECTION_TYPE = "connection_type"
ATTR_SPEED = "speed"
ATTR_BATTERY = "battery"

CONF_LOCAL_NAME = "local_name"
CONF_ADDRESS = "address"
CONF_MAC_CODE = "mac_code"
CONF_BLIND_TYPE = "blind_type"

DOMAIN = "motionblinds_ble"

ERROR_ALREADY_CONFIGURED = "already_configured"
ERROR_COULD_NOT_FIND_MOTOR = "could_not_find_motor"
ERROR_INVALID_MAC_CODE = "invalid_mac_code"
ERROR_NO_BLUETOOTH_ADAPTER = "no_bluetooth_adapter"
ERROR_NO_DEVICES_FOUND = "no_devices_found"

ICON_SPEED = "mdi:run-fast"

SERVICE_CONNECT = "connect"
SERVICE_DISCONNECT = "disconnect"
SERVICE_FAVORITE = "favorite"
SERVICE_STATUS = "status"

SETTING_DOUBLE_CLICK_TIME = 500  # Milliseconds


class MotionBlindType(StrEnum):
    POSITION = "position"
    POSITION_TILT = "position_tilt"


class MotionRunningType(StrEnum):
    CLOSING = "closing"
    OPENING = "opening"
    STILL = "still"
