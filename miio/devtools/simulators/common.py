"""Common functionalities for miio and miot simulators."""
from hashlib import md5


def create_info_response(model, mac):
    """Create a response for miIO.info call using the given model and mac."""
    INFO_RESPONSE = {
        "ap": {"bssid": "FF:FF:FF:FF:FF:FF", "rssi": -68, "ssid": "network"},
        "cfg_time": 0,
        "fw_ver": "1.2.4_16",
        "hw_ver": "MW300",
        "life": 24,
        "mac": mac,
        "mmfree": 30312,
        "model": model,
        "netif": {
            "gw": "192.168.xxx.x",
            "localIp": "192.168.xxx.x",
            "mask": "255.255.255.0",
        },
        "ot": "otu",
        "ott_stat": [0, 0, 0, 0],
        "otu_stat": [320, 267, 3, 0, 3, 742],
        "token": 32 * "0",
        "wifi_fw_ver": "SD878x-14.76.36.p84-702.1.0-WM",
    }
    return INFO_RESPONSE


def mac_from_model(model):
    """Creates a mac address based on the model name.

    This allows simulating multiple different devices separately as the homeassistant
    unique_id is based on the mac address.
    """
    m = md5()  # nosec
    m.update(model.encode())
    digest = m.hexdigest()[:12]
    mac = ":".join([digest[i : i + 2] for i in range(0, len(digest), 2)])
    return mac
