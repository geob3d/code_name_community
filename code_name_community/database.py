
from sqlalchemy import create_engine,MetaData, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import inspect
from sqlalchemy.engine import reflection
from sqlalchemy import table, column
from sqlalchemy import BigInteger, CheckConstraint, Column, Date, ForeignKey, Integer, Numeric, String, Text, Time, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base





engine = create_engine('postgresql://postgres:C@mera12@localhost:5432/coummunity_db', echo=True)
Base = declarative_base()
metadata = Base.metadata

## CODE GEN CODE
##sqlacodegen postgresql://postgres:C@mera12@localhost:5432/coummunity_db --schema STD --outfile models.py

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

con = engine.connect()

con.execute("SET search_path TO 'STD'")
rs = con.execute("SELECT * FROM organization_group_class")


for r in rs.fetchall():
    print (r)

con.close()



class OrganizationGroupClas(Base):
    __tablename__ = 'organization_group_class'
    __table_args__ = {'schema': 'STD'}

    id = Column(Integer, primary_key=True, server_default=text("nextval('\"STD\".organization_group_class_id_seq'::regclass)"))
    name = Column(String(55), nullable=False)
    description = Column(Text, nullable=False)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
result = session.query(Organization).all()

for row in result:
    print (row.city)

# connection = engine.connect()

# z = "SELECT * FROM organization_group_class"


# # # Read
# result_set = connection.execute(z).fetchall()
# for r in result_set:  
#     print(r)



##11
# sql = "SELECT * FROM organization_group_class"

# result_set = engine.execute(sql)  
# for r in result_set:  
#     print(r)



## GET SCHEMA AND COLUMNS -- USEFUL ###

# inspector = inspect(engine)
# schemas = inspector.get_schema_names()

# for schema in schemas:
#     print("schema: %s" % schema)
#     for table_name in inspector.get_table_names(schema=schema):
#         print()
#         for column in inspector.get_columns(table_name, schema=schema):
#             print("Column: %s" % column)

# connection = engine.connect().execute('set search_path=STD')


# #results.connection.execute('set search_path=B_schema')
# my_query = 'SELECT * FROM organization_group_class'

# results = connection.execute(my_query).fetchall()















