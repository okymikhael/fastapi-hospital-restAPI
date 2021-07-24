from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql://root:@localhost/hospital")
meta = MetaData()
con = engine.connect()