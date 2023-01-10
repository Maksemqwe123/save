from work.db_api.db_bot_user import TimedBaseModel
from sqlalchemy import Column, String, BigInteger, sql


class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    name = Column(String(200), primary_key=True)
    update_name = Column(String(50), primary_key=True)

    query: sql.select
