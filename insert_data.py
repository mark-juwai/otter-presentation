from sqlalchemy import create_engine
import time

engine = create_engine('mysql+mysqldb://otter:otter@172.16.1.9/test')
conn = engine.connect()
sql = "insert into salesforce_data (`value`, `url`, `has_sync`) values ('{0}', 'http://www.test.com/{0}', 0);"
index = 0
while(True):
    conn.execute(sql.format(index))
    index = index + 1
    # time.sleep(0.05)
