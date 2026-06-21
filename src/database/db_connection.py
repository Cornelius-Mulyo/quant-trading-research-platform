from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql://postgres:QuantProject2026!@localhost:5432/quant_platform"
)

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as connection:
        print("Connected successfully!")
except Exception as e:
    print("Connection failed:")
    print(e)