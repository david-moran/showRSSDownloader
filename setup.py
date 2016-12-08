import os
from setuptools import setup
from pip.req import parse_requirements


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def requirements(fname):
        reqs = parse_requirements(os.path.join(os.path.dirname(__file__),
                                               fname), session=False)
        return [str(ir.req) for ir in reqs]


setup(
    name="showRSSDownloader",
    version="0.0.1",
    author="David Morán",
    author_email="david@dmoran.es",
    description=("Download shows from ShowRSS.info"),
    license="BSD",
    keywords="showrss torrent download",
    url="http://github.com/david-moran/showrssdownloader",
    packages=['showRSSDownloader'],
    long_description=read('README.md'),
    install_requires=requirements('requirements.txt'),
    entry_points = {
        'console_scripts': [
                'showRSSDownloader = showRSSDownloader.showrssdownloader:main'
        ]
    },
)
