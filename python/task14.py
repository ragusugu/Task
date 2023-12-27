from sqlalchemy import String, create_engine, Column, Integer, JSON, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
import json

Base = declarative_base()

# Define the SQLAlchemy model for attribute_issue_count
class AttributeIssueCount(Base):
    __tablename__ = 'attribute_issue_count'

    issue_count_id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, nullable=False)
    integration_id = Column(Integer, nullable=False)
    meta_data_id = Column(Integer, nullable=False)
    created_month = Column(TIMESTAMP, nullable=False)
    issue_count = Column(Integer, nullable=False)
    issue_details = Column(String, nullable=False)
    data_set_id = Column(Integer, nullable=False)
    env_id = Column(Integer, nullable=False)

# Define the SQLAlchemy model for dataset_issue_count
class DatasetIssueCount(Base):
    __tablename__ = 'dataset_issue_count'

    issue_count_id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, nullable=False)
    integration_id = Column(Integer, nullable=False)
    data_set_id = Column(Integer, nullable=False)
    created_month = Column(TIMESTAMP, nullable=False)
    issue_count = Column(Integer, nullable=False)
    issue_details = Column(String, nullable=False)
    env_id = Column(Integer, nullable=False)

# Define the SQLAlchemy model for datasource_issue_count
class DatasourceIssueCount(Base):
    __tablename__ = 'datasource_issue_count'

    issue_count_id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, nullable=False)
    env_id = Column(Integer, nullable=False)
    integration_id = Column(Integer, nullable=False)
    created_month = Column(TIMESTAMP, nullable=False)
    issue_count_dataset_level = Column(Integer, nullable=False)
    issue_details_dataset_level = Column(String, nullable=False)  # Use String from sqlalchemy
    issue_count_attribute_level = Column(Integer, nullable=False)
    issue_details_attribute_level = Column(String, nullable=False)  # Use String from sqlalchemy

# Create an SQLite in-memory database
engine = create_engine('sqlite:///:memory:', echo=True)

# Create the tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert records into attribute_issue_count
attribute_issue_count_records = [
    (1664, 2566, 322384, '2023-11-01 00:00:00.000000', 1, '{"44961": 1}', 55396, 1485),
    (1664, 2566, 322386, '2023-11-01 00:00:00.000000', 2, '{"44961": 1, "44982": 1}', 55396, 1485),
    (1664, 2566, 322388, '2023-11-01 00:00:00.000000', 1, '{"44961": 1}', 55396, 1485),
    (1664, 2566, 322382, '2023-11-01 00:00:00.000000', 1, '{"44967": 1}', 55396, 1485),
    (1664, 2566, 322383, '2023-11-01 00:00:00.000000', 1, '{"44961": 1}', 55397, 1485),
    (1664, 2566, 322385, '2023-11-01 00:00:00.000000', 2, '{"44961": 1, "44982": 1}', 55397, 1485),
    (1664, 2566, 322387, '2023-11-01 00:00:00.000000', 1, '{"44961": 1}', 55397, 1485),
    (1664, 2566, 322393, '2023-11-01 00:00:00.000000', 1, '{"44967": 1}', 55397, 1485),
]

for record in attribute_issue_count_records:
    record_dict = {
        'issue_count_id': record[0],
        'tenant_id': record[1],
        'integration_id': record[2],
        'meta_data_id': record[3],
        'created_month': record[4],
        'issue_count': record[5],
        'issue_details': record[6],
        'data_set_id': record[7],
        'env_id': record[8],
    }
    session.add(AttributeIssueCount(**record_dict))

# Insert records into dataset_issue_count
dataset_issue_count_records = [
    (1664, 2566, 55396, '2023-11-01 00:00:00.000000', 3, '{"44961": 1, "44967": 1, "44982": 1}', 1485),
    (1664, 2566, 55397, '2023-11-01 00:00:00.000000', 3, '{"44961": 1, "44967": 1, "44982": 1}', 1485),
]

for record in dataset_issue_count_records:
    record_dict = {
        'issue_count_id': record[0],
        'tenant_id': record[1],
        'integration_id': record[2],
        'data_set_id': record[3],
        'created_month': record[4],
        'issue_count': record[5],
        'issue_details': record[6],
        'env_id': record[7],
    }
    session.add(DatasetIssueCount(**record_dict))

# Commit the changes
session.commit()

# Query and print records from attribute_issue_count
print("Records from attribute_issue_count:")
for record in session.query(AttributeIssueCount).all():
    print(record.__dict__)

# Query and print records from dataset_issue_count
print("\nRecords from dataset_issue_count:")
for record in session.query(DatasetIssueCount).all():
    print(record.__dict__)

# Aggregate data and insert into datasource_issue_count
integration_ids = [322384, 322386, 322388, 322382, 322383, 322385, 322387, 322393]

for integration_id in integration_ids:
    # Aggregate attribute_issue_count data
    attribute_data = (
        session.query(
            func.sum(AttributeIssueCount.issue_count).label('total_issue_count_attribute_level'),
            func.jsonb_object_agg(AttributeIssueCount.issue_details, func.sum(1)).label('aggregated_issue_details_attribute_level')
        )
        .filter(AttributeIssueCount.integration_id == integration_id)
        .group_by(AttributeIssueCount.integration_id)
        .first()
    )

    # Aggregate dataset_issue_count data
    dataset_data = (
        session.query(
            func.sum(DatasetIssueCount.issue_count).label('total_issue_count_dataset_level'),
            func.jsonb_object_agg(DatasetIssueCount.issue_details, func.sum(1)).label('aggregated_issue_details_dataset_level')
        )
        .filter(DatasetIssueCount.integration_id == integration_id)
        .group_by(DatasetIssueCount.integration_id)
        .first()
    )

    # Insert aggregated data into datasource_issue_count
    datasource_record = DatasourceIssueCount(
        tenant_id=attribute_data.total_issue_count_attribute_level,
        env_id=attribute_data.total_issue_count_dataset_level,
        integration_id=integration_id,
        created_month=datetime.now(),
        issue_count_dataset_level=dataset_data.total_issue_count_dataset_level,
        issue_details_dataset_level=json.dumps(dataset_data.aggregated_issue_details_dataset_level),
        issue_count_attribute_level=attribute_data.total_issue_count_attribute_level,
        issue_details_attribute_level=json.dumps(attribute_data.aggregated_issue_details_attribute_level)
    )

    session.add(datasource_record)

# Commit the changes
session.commit()

# Query and print records from datasource_issue_count
print("\nRecords from datasource_issue_count:")
for record in session.query(DatasourceIssueCount).all():
    print(record.__dict__)
