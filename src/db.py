from sqlmodel import create_engine, Session, SQLModel

def get_engine():
    engine = create_engine('sqlite:///books.db')
    return engine

def get_session():
    engine = get_engine()
    session = Session(engine)
    return session

def create_all_tables():
    engine = get_engine()
    SQLModel.metadata.create_all(engine)
    