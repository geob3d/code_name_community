# coding: utf-8
from sqlalchemy import BigInteger, CheckConstraint, Column, Date, ForeignKey, Integer, Numeric, String, Text, Time, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class CommunityEvent(Base):
    __tablename__ = 'community_events'
    __table_args__ = {'schema': 'STD'}

    id = Column(BigInteger, primary_key=True)
    event_name = Column(String(55), nullable=False)
    event_location = Column(String(75), nullable=False)
    event_date = Column(Date, nullable=False)
    event_time = Column(Time, nullable=False)
    event_cost = Column(Numeric(8, 2))
    description = Column(Text, nullable=False)
    address = Column(String(75), nullable=False)
    city = Column(String(55), nullable=False)
    state = Column(String(3), nullable=False)
    zip_code = Column(Integer, nullable=False)
    email = Column(String(55), nullable=False)


class OrganizationGroupClas(Base):
    __tablename__ = 'organization_group_class'
    __table_args__ = {'schema': 'STD'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"STD\".organization_group_class_id_seq'::regclass)"))
    name = Column(String(55), nullable=False)
    description = Column(Text, nullable=False)


class Organization(Base):
    __tablename__ = 'organizations'
    __table_args__ = (
        CheckConstraint('zip_code <= 99999'),
        {'schema': 'STD'}
    )

    id = Column(BigInteger, primary_key=True)
    name = Column(String(55), nullable=False)
    city = Column(String(55), nullable=False)
    state = Column(String(3), nullable=False)
    zip_code = Column(Integer, nullable=False)
    email = Column(String(55), nullable=False)
    phone_number = Column(String(10), nullable=False)
    org_type_class_id = Column(ForeignKey('STD.organization_group_class.id'), nullable=False)

    org_type_class = relationship('OrganizationGroupClas')


class OrgGroup(Base):
    __tablename__ = 'org_groups'
    __table_args__ = (
        CheckConstraint('zip_code <= 99999'),
        {'schema': 'STD'}
    )

    id = Column(BigInteger, primary_key=True)
    name = Column(String(55), nullable=False)
    organization_id = Column(ForeignKey('STD.organizations.id'), nullable=False)
    city = Column(String(55), nullable=False)
    state = Column(String(3), nullable=False)
    zip_code = Column(Integer, nullable=False)
    email = Column(String(55), nullable=False)
    phone_number = Column(String(10), nullable=False)

    organization = relationship('Organization')


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'schema': 'STD'}

    id = Column(BigInteger, primary_key=True)
    user_name = Column(String(55), nullable=False)
    org_group_id = Column(ForeignKey('STD.org_groups.id'), nullable=False)
    password = Column(String(20))
    email = Column(String(55), nullable=False)

    org_group = relationship('OrgGroup')
