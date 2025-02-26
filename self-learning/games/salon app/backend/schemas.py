from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    is_salon: bool = False

class User(UserBase):
    id: int
    is_salon: bool
    
    class Config:
        orm_mode = True

class SalonBase(BaseModel):
    name: str
    address: str

class SalonCreate(SalonBase):
    pass

class Salon(SalonBase):
    id: int
    owner_id: int
    booking_link: str
    
    class Config:
        orm_mode = True

class ServiceBase(BaseModel):
    name: str
    duration: int
    price: float

class ServiceCreate(ServiceBase):
    salon_id: int

class Service(ServiceBase):
    id: int
    salon_id: int
    
    class Config:
        orm_mode = True

class BookingBase(BaseModel):
    datetime: datetime
    customer_name: str
    customer_email: str
    service_id: int

class BookingCreate(BookingBase):
    salon_id: int

class Booking(BookingBase):
    id: int
    status: str
    salon_id: int
    
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str 