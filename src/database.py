import json
import time
from sqlalchemy import create_engine, Table, Column, Float, String, MetaData


class Database:

    def __init__(self, db_url, seed_path):

        # try to initialize the DB 10 times
        for _ in range(10):
            try:
                self.engine = create_engine(db_url)
                self.meta = MetaData(self.engine)
                # create table accounts
                self.table = Table(
                    "account",
                    self.meta,
                    Column("acctid", String(15), primary_key=True),
                    Column("paid", Float, nullable=False),
                    Column("due", Float, nullable=False),
                )
                # connect to the DB and see if it works
                self.meta.create_all()
                self.connect()
                break

            except:
                time.sleep(5)

        # if conn attr does not exist or is closed raise error
        if not hasattr(self, "conn") or self.conn.closed:
            raise TimeoutError("Could not establish session to mysql db")

        # use json data to seed the dababase
        # note json has been converted from a dict into
        # a list of 3 dict to make it easier to consume by sqlalchemy
        with open(seed_path, "r") as handle:
            data = json.load(handle)

        self.result = self.conn.execute(self.table.insert(), data)
        self.disconnect()

    def connect(self):
        self.conn = self.engine.connect()
        if self.conn.closed:
            raise OSError("connect() succeed but session is still closed")

    def disconnect(self):
        # hasattr(self, "conn") and
        if not self.conn.closed:
            self.conn.close()
            if not self.conn.closed:
                raise OSError("close() succeeded but session is still open")

    def balance(self, acct_id):
        select_acct = self.table.select().where(
            self.table.c.acctid == acct_id.upper()
        )
        result = self.conn.execute(select_acct)
        acct = result.fetchone()
        if acct:
            bal = acct["due"] - acct["paid"]
            return f"{bal:.2f} USD"

        return None
