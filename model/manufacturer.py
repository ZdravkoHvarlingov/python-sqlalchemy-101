from db.core import Base
from sqlalchemy import Column, Integer, String


class Manufacturer(Base):
    __tablename__ = 'manufacturer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    foundation_year = Column(Integer, nullable=False)

    def __init__(self, name, foundation_year):
        self.name = name
        self.foundation_year = foundation_year
    
    def __repr__(self) -> str:
        return f'(name={self.name}, foundation_year={self.foundation_year})'
