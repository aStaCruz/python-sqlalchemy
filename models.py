from manage import db,app
from sqlalchemy import Date
import datetime, time

# Create our database model
class FeatureRequest(db.Model):
    __tablename__ = "requests"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(420))
    description = db.Column(db.String())
    client = db.Column(db.String(10))
    clientPriority = db.Column(db.Integer())
    targetDate = db.Column(Date, default=datetime.datetime.utcnow)
    productArea = db.Column(db.String(42))

    def __init__(self, title, description, client, clientPriority, targetDate, productArea):
        self.title = title
        self.description = description
        self.client = client
        self.clientPriority = clientPriority
        self.targetDate = targetDate
        self.productArea = productArea