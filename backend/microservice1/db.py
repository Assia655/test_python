from models import Base, Item, get_engine

def init_db():
    engine = get_engine()
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()
