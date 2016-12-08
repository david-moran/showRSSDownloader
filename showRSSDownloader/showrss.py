import aiohttp
import asyncio
import feedparser
from sqlalchemy import literal
from showRSSDownloader.settings import Settings
import showRSSDownloader.models as models
from transmissionrpc.client import Client as TransmissionClient


settings = Settings()
transmission = TransmissionClient(address=settings.transmission_address,
                                  port=settings.transmission_port,
                                  user=settings.transmission_user,
                                  password=settings.transmission_password)


class Show:
    def __init__(self, id, title, url):
        self.session = models.session()
        self.loop = asyncio.get_event_loop()
        self.id = id
        self.title = title
        self.url = url

    def is_downloaded(self):
        q = self.session.query(models.ShowRSS).filter_by(showrss_id=self.id)
        return self.session.query(literal(True)).filter(q.exists()).scalar()

    def download(self):
        self.session = models.session()
        self.session.add(models.ShowRSS(showrss_id=self.id))
        transmission.add_torrent(self.url)
        self.session.commit()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '"{self.title}" [{self.id}]'.format(self=self)


class ShowGenerator:
    def __init__(self, rss):
        self.pos = 0
        self.rss = rss

    def __iter__(self):
        return self

    def __next__(self):
        entries = self.rss['entries']

        if len(entries) == self.pos:
            raise StopIteration

        entry = entries[self.pos]

        id = entry['id']
        title = entry['title']
        url = entry['link']

        self.pos += 1
        return Show(id, title, url)


class ShowRSS:
    def __init__(self, url=settings.showrss_url):
        self.url = url

    async def parse(self):
        loop = asyncio.get_event_loop()

        async with aiohttp.ClientSession(loop=loop) as session:
            rss = await self._fetch(session)
            return await loop.run_in_executor(None, feedparser.parse, rss)

    async def get_shows(self):
        rss = await self.parse()
        return ShowGenerator(rss)

    async def _fetch(self, session):
        async with session.get(self.url) as response:
            return await response.text()
