from sqlalchemy import create_engine, Column, Integer, TIMESTAMP, JSON, text
from sqlalchemy.orm import declarative_base
from urllib.parse import quote
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
import task14a
import subprocess


subprocess.run(["python", r"C:\Users\HI\Documents\git\sample\Task\python\task14a.py"])

# print(task14a.person)

password = 'Sugan@123'
encoded_password = quote(password)
DATABASE_URL = f'postgresql://postgres:{encoded_password}@localhost/sugan'

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Define the base class for declarative table definitions
Base = declarative_base()

# Define the datasource_issue_count table
# class DatasourceIssueCount(Base):
#     __tablename__ = 'datasource_issue_count'
#     issue_count_id = Column(Integer, primary_key=True, autoincrement=True)
#     tenant_id = Column(Integer, nullable=False)
#     env_id = Column(Integer, nullable=False)
#     integration_id = Column(Integer, nullable=False)
#     created_month = Column(TIMESTAMP, nullable=False)
#     issue_count_dataset_level = Column(Integer, nullable=False)
#     issue_details_dataset_level = Column(JSON, nullable=False)
#     issue_count_attribute_level = Column(Integer, nullable=False)
#     issue_details_attribute_level = Column(JSON, nullable=False)

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session
session = Session(engine)
AttributeIssueCount=task14a.AttributeIssueCount()
DatasetIssueCount=task14a.DatasetIssueCount()
DatasourceIssueCount=task14a.DatasourceIssueCount()
# Aggregate data from attribute_issue_count and dataset_issue_count
result = session.query(
    AttributeIssueCount.integration_id,
    AttributeIssueCount.created_month,
    func.sum(AttributeIssueCount.issue_count).label('total_issue_count_attribute'),
    func.jsonb_object_agg(
        func.cast(AttributeIssueCount.issue_count, Integer),
        func.sum(func.cast(AttributeIssueCount.issue_count, Integer))
    ).label('agg_issue_details_attribute')
).group_by(AttributeIssueCount.integration_id, AttributeIssueCount.created_month).all()

for row in result:
    integration_id = row.integration_id
    created_month = row.created_month
    total_issue_count_attribute = row.total_issue_count_attribute
    agg_issue_details_attribute = row.agg_issue_details_attribute

    # Fetch additional data from dataset_issue_count
    dataset_result = session.query(
        DatasetIssueCount.integration_id,
        func.sum(DatasetIssueCount.issue_count).label('total_issue_count_dataset'),
        func.jsonb_object_agg(
            func.cast(DatasetIssueCount.issue_count, Integer),
            func.sum(func.cast(DatasetIssueCount.issue_count, Integer))
        ).label('agg_issue_details_dataset')
    ).filter(
        DatasetIssueCount.integration_id == integration_id,
        DatasetIssueCount.created_month == created_month
    ).group_by(DatasetIssueCount.integration_id).first()

    if dataset_result:
        total_issue_count_dataset = dataset_result.total_issue_count_dataset
        agg_issue_details_dataset = dataset_result.agg_issue_details_dataset
    else:
        total_issue_count_dataset = 0
        agg_issue_details_dataset = {}

    # Insert data into datasource_issue_count
    datasource_issue_count = DatasourceIssueCount(
        tenant_id=1664,
        env_id=1485,
        integration_id=integration_id,
        created_month=created_month,
        issue_count_dataset_level=total_issue_count_dataset,
        issue_details_dataset_level=agg_issue_details_dataset,
        issue_count_attribute_level=total_issue_count_attribute,
        issue_details_attribute_level=agg_issue_details_attribute
    )
    session.add(datasource_issue_count)
task14a()
# Commit the changes to the database
session.commit()

# Close the session
session.close()

