from sqlalchemy import create_engine, Column, Integer, TIMESTAMP, JSON, MetaData, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
from urllib.parse import quote

# person="hello"
# Define the database connection URL
password = 'Sugan@123'
encoded_password = quote(password)
DATABASE_URL = f'postgresql://postgres:{encoded_password}@localhost/sugan'

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Define the base class for declarative table definitions
Base = declarative_base()

# Define the attribute_issue_count table
class AttributeIssueCount(Base):
    __tablename__ = 'attribute_issue_count'
    issue_count_id = Column(Integer, primary_key=True, autoincrement=True)
    tenant_id = Column(Integer,primary_key=True)
    integration_id = Column(Integer, nullable=False)
    meta_data_id = Column(Integer, nullable=False)
    created_month = Column(TIMESTAMP, nullable=False)
    issue_count = Column(Integer, nullable=False)
    issue_details = Column(JSON, nullable=False)
    data_set_id = Column(Integer, nullable=False)
    env_id = Column(Integer, nullable=False)

# Define the dataset_issue_count table
class DatasetIssueCount(Base):
    __tablename__ = 'dataset_issue_count'
    issue_count_id = Column(Integer, primary_key=True, autoincrement=True)
    tenant_id = Column(Integer, nullable=False)
    integration_id = Column(Integer, nullable=False)
    data_set_id = Column(Integer, nullable=False)
    created_month = Column(TIMESTAMP, nullable=False)
    issue_count = Column(Integer, nullable=False)
    issue_details = Column(JSON, nullable=False)
    env_id = Column(Integer, nullable=False)

# Define the datasource_issue_count table
class DatasourceIssueCount(Base):
    __tablename__ = 'datasource_issue_count'
    issue_count_id = Column(Integer, primary_key=True, autoincrement=True)
    tenant_id = Column(Integer, nullable=False)
    env_id = Column(Integer, nullable=False)
    integration_id = Column(Integer, nullable=False)
    created_month = Column(TIMESTAMP, nullable=False)
    issue_count_dataset_level = Column(Integer, nullable=False)
    issue_details_dataset_level = Column(JSON, nullable=False)
    issue_count_attribute_level = Column(Integer, nullable=False)
    issue_details_attribute_level = Column(JSON, nullable=False)

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a connection to the database
conn = engine.connect()

# Insert records into attribute_issue_count table
try:
    conn.execute(text("""
        INSERT INTO attribute_issue_count (tenant_id, integration_id, meta_data_id, created_month, issue_count, issue_details, data_set_id, env_id)
        VALUES 
         (1664, 2566, 322384, TIMESTAMP '2023-11-01 00:00:00.000000', 1, cast('{"44961": 1}' as json), 55396, 1485),
         (1664, 2566, 322386, TIMESTAMP '2023-11-01 00:00:00.000000', 2, cast('{"44961": 1, "44982": 1}' as json), 55396, 1485),
         (1664, 2566, 322388, TIMESTAMP '2023-11-01 00:00:00.000000', 1, cast('{"44961": 1}' as json), 55396, 1485),
         (1664, 2566, 322382, TIMESTAMP '2023-11-01 00:00:00.000000', 1, cast('{"44967": 1}' as json), 55396, 1485),
         (1664, 2566, 322383, TIMESTAMP '2023-11-01 00:00:00.000000', 1, cast('{"44961": 1}' as json), 55397, 1485),
         (1664, 2566, 322385, TIMESTAMP '2023-11-01 00:00:00.000000', 2, cast('{"44961": 1, "44982": 1}' as json), 55397, 1485),
         (1664, 2566, 322387, TIMESTAMP '2023-11-01 00:00:00.000000', 1, cast('{"44961": 1}' as json), 55397, 1485),
         (1664, 2566, 322393, TIMESTAMP '2023-11-01 00:00:00.000000', 1, cast('{"44967": 1}' as json), 55397, 1485)
    """))
    conn.commit()
except Exception as e:
    print(f"Error: {e}")

# Insert records into dataset_issue_count table
try:
    conn.execute(text("""
        INSERT INTO dataset_issue_count (tenant_id, integration_id, data_set_id, created_month, issue_count, issue_details, env_id)
        VALUES 
        (1664, 2566, 55396, TIMESTAMP '2023-11-01 00:00:00.000000', 3, cast('{"44961": 1, "44967": 1, "44982": 1}' as json), 1485),
        (1664, 2566, 55397, TIMESTAMP '2023-11-01 00:00:00.000000', 3, cast('{"44961": 1, "44967": 1, "44982": 1}' as json), 1485)
    """))
    conn.commit()
except Exception as e:
    print(f"Error: {e}")

# Close the connection
conn.close()
