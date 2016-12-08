from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from showRSSDownloader.settings import Settings
from datetime import datetime


__Base = declarative_base()
__settings = Settings()
__engine = create_engine('sqlite:///{}'.format(__settings.database))


class ShowRSS(__Base):
    __tablename__ = 'showrss'
    id = Column(Integer, primary_key=True)
    creation_time = Column(DateTime, nullable=False, default=datetime.utcnow)
    showrss_id = Column(String, nullable=False, unique=True)


def session():
    Session = sessionmaker(bind=__engine)
    return Session()


__Base.metadata.create_all(__engine)
