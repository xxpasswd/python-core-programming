# coding: utf-8
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine('sqlite:///aaaa.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = relationship('Address', back_populates="user", uselist=False)

    def __repr__(self):
        return "<User(name=%s)" % self.name


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates="address")

Base.metadata.create_all(engine)


session = Session()


ed_user = User(name='aaa')
ed_user.address = Address(name='bbb')
session.add(ed_user)
session.commit()

