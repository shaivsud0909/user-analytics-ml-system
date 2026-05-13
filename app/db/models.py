from typing import Text

from sqlalchemy import (
    TIMESTAMP,
    Boolean,
    Column,
    Float,
    Integer,
    String,
    text,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.db.database import Base












class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    email = Column(String, unique=True)

    password = Column(String)

    role = Column(String, default="user")

    is_deleted = Column(
        Boolean,
        default=False,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )

    # ONE USER -> MANY PREDICTIONS
    predictions = relationship(
        "Prediction",
        back_populates="user",
        cascade="all, delete"
    )







class Prediction(Base):

    __tablename__ = "predictions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )
    gender = Column(String, nullable=False)

    SeniorCitizen = Column(Integer, nullable=False)

    Partner = Column(String, nullable=False)

    Dependents = Column(String, nullable=False)

    tenure = Column(Integer, nullable=False)

    PhoneService = Column(String, nullable=False)

    MultipleLines = Column(String, nullable=False)

    InternetService = Column(String, nullable=False)

    OnlineSecurity = Column(String, nullable=False)

    OnlineBackup = Column(String, nullable=False)

    DeviceProtection = Column(String, nullable=False)

    TechSupport = Column(String, nullable=False)

    StreamingTV = Column(String, nullable=False)

    StreamingMovies = Column(String, nullable=False)

    Contract = Column(String, nullable=False)

    PaperlessBilling = Column(String, nullable=False)

    PaymentMethod = Column(String, nullable=False)

    MonthlyCharges = Column(Float, nullable=False)

    prediction = Column(Integer, nullable=False)

    probability = Column(Float, nullable=False)

    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )

    # MANY PREDICTIONS -> ONE USER
    user = relationship(
        "User",
        back_populates="predictions"
    )

    # ONE PREDICTION -> ONE FEEDBACK
    feedback = relationship(
        "Feedback",
        back_populates="prediction",
        uselist=False,
        cascade="all, delete"
    )








class Feedback(Base):

    __tablename__ = "feedback"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    prediction_id = Column(
        Integer,
        ForeignKey("predictions.id"),
        nullable=False,
        unique=True
    )

    rating = Column(Integer)

    is_correct = Column(
        Boolean,
        nullable=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP")
    )

    # ONE FEEDBACK -> ONE PREDICTION
    prediction = relationship(
        "Prediction",
        back_populates="feedback"
    )




