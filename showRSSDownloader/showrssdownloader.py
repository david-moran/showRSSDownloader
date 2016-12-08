#!/usr/bin/env python

import time
import asyncio
from showRSSDownloader.showrss import ShowRSS
from showRSSDownloader.settings import Settings


settings = Settings()


async def wait_for_downloads():
    while True:
        rss = ShowRSS()
        for show in await rss.get_shows():
            if not show.is_downloaded():
                print("{} not yet download. Added to download queue."
                      .format(show.id))
                show.download()
        time.sleep(int(settings.showrss_timeout))


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait_for_downloads())


if __name__ == '__main__':
    main()
