from sqlalchemy import Column, String
from model_builder.db import Base


class MLModel(Base):
    __tablename__ = 'ml_model'
    id = Column(String(255), primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    model_path = Column(String(255))
    model_weight_path = Column(String(255))
    model_code_path = Column(String(255))
    model_result_path = Column(String(255))
