from configparser import ConfigParser
from os.path import expanduser


class Settings:
    DEFAULTS = {
        "global": {
            "database": expanduser("~/.showrss_downloader.sqlite3"),
        },
        "showrss": {
            "url": "http://showrss.info/user/113156.rss?magnets=true&"
                   "namespaces=true&name=null&quality=null&re=null",
            "timeout": 60,
        },
        "transmission": {
            "address": "localhost",
            "port": 9091,
            "user": "transmission",
            "password": "transmission"
        }
    }

    SETTINGS_FILE = "~/.showrssdownloader"

    def __init__(self):
        self.configparser = ConfigParser()
        self.configparser.read_dict(Settings.DEFAULTS)
        self.configparser.read(Settings.SETTINGS_FILE)

    @property
    def database(self):
        return self.configparser.get("global", "database")

    @property
    def showrss_url(self):
        return self.configparser.get("showrss", "url")

    @property
    def showrss_timeout(self):
        return self.configparser.get("showrss", "timeout")

    @property
    def transmission_address(self):
        return self.configparser.get("transmission", "address")

    @property
    def transmission_port(self):
        return self.configparser.get("transmission", "port")

    @property
    def transmission_user(self):
        return self.configparser.get("transmission", "user")

    @property
    def transmission_password(self):
        return self.configparser.get("transmission", "password")
