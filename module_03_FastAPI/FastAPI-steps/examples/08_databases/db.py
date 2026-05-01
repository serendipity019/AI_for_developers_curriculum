from sqlmodel import Session, SQLModel, create_engine
print("import successful!")
DABASE_URL = "sqlite:///./my_first_python_db.db"

engine = create_engine(
    DABASE_URL,
    echo=False, # To not appea the SQL queries on terminal. 
    connect_args={"check_same_thread": False}, # Required for SQLite
)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
