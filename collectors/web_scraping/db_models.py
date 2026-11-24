from sqlalchemy import Column, Text, Integer, String, DateTime, ARRAY
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from .model import ScrapingItem

Base = declarative_base()

class Property(Base):
    __tablename__ = 'properties'

    id = Column(String(32), primary_key=True, index = True)
    url = Column(String(500), unique=True, nullable=False)
    title = Column(String(500), nullable=False)
    address = Column(String(500), nullable=False)
    price = Column(Integer)
    description = Column(String(1000))
    bedrooms = Column(Integer)
    receptions= Column(Integer)
    epc_rating = Column(String(10))
    image_url = Column(String(500))
    tags = Column(ARRAY(String), default = [])

@classmethod
def from_scraping_item(cls, item: ScrapingItem):
    return cls(

        id = item.id,
        url=item.url,
        title=item.title,
        price=item.price,
        address=item.address,
        description=item.description,
        bedrooms=item.bedrooms,
        receptions=item.receptions,
        epc_rating=item.epc_rating,
        image_url=item.image_url,
        tags=item.tags
    )