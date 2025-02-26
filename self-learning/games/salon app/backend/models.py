from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_salon = Column(Boolean, default=False)
    
    salon = relationship("Salon", back_populates="owner", uselist=False)

class Salon(Base):
    __tablename__ = "salons"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    booking_link = Column(String, unique=True)
    
    owner = relationship("User", back_populates="salon")
    services = relationship("Service", back_populates="salon")
    bookings = relationship("Booking", back_populates="salon")

class Service(Base):
    __tablename__ = "services"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    duration = Column(Integer)  # in minutes
    price = Column(Float)
    salon_id = Column(Integer, ForeignKey("salons.id"))
    
    salon = relationship("Salon", back_populates="services")
    bookings = relationship("Booking", back_populates="service")

class Booking(Base):
    __tablename__ = "bookings"
    
    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime)
    customer_name = Column(String)
    customer_email = Column(String)
    status = Column(String)  # pending, confirmed, completed, cancelled
    salon_id = Column(Integer, ForeignKey("salons.id"))
    service_id = Column(Integer, ForeignKey("services.id"))
    
    salon = relationship("Salon", back_populates="bookings")
    service = relationship("Service", back_populates="bookings") 