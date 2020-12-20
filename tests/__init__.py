from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

TEST_DATABASE = "sqlite:///./test.db"

test_sqlite_engine = create_engine(TEST_DATABASE, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_sqlite_engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def setup_teardown(func):
    def wrapper(base):
        print("Creating Test DB Tables")
        base().metadata.create_all(test_sqlite_engine)
        func()
        print("Deleting Test DB Tables")
    return wrapper
