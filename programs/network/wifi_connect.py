import time
import pywifi
from loguru import logger


wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
logger.info(iface.name())

nets = list()

if iface.status() == pywifi.const.IFACE_DISCONNECTED:
    iface.scan()
    time.sleep(10)
    for p in iface.scan_results():
        nets.append(p.ssid)

if "SCB-RHYX" in nets:
    logger.info("Aha! Catch [SCB-RHYX]!")

    profile = pywifi.Profile()
    profile.ssid = 'SCB-RHYX'
    profile.auth = pywifi.const.AUTH_ALG_OPEN
    profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
    profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
    profile.key = 'CMOS10086'

    logger.info("Connecting...")
    profile = iface.add_network_profile(profile)
    iface.connect(profile)

    time.sleep(10)

    if iface.status() == pywifi.const.IFACE_CONNECTED:
        logger.info("Connected!")
