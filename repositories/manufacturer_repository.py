from db.connection import DbSession
from model.manufacturer import Manufacturer


class ManufacturerRepository:
    
    @staticmethod
    def find_all():
        with DbSession.create() as session:
            return session.query(Manufacturer).all()
    
    @staticmethod
    def find_by_name(name: str):
        with DbSession.create() as session:
            return session.query(Manufacturer).filter(Manufacturer.name == name).first()
    
    @staticmethod
    def upsert(manufacturer: Manufacturer):
        with DbSession.create() as session:
            session.add(manufacturer)
            session.flush()
            session.commit()

            return manufacturer

    @staticmethod
    def delete(manufacturer: Manufacturer):
        if not manufacturer or not manufacturer.id:
            return
        
        ManufacturerRepository.delete_by_id(manufacturer.id)

    @staticmethod
    def delete_by_id(manufacturer_id: int):
        with DbSession.create() as session:
            session.query(Manufacturer).filter(Manufacturer.id == manufacturer_id).delete()
            session.commit()
