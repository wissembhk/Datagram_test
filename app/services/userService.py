from producer import push_to_rabbitmq
from models.models import User
from models.schemas import UserSchema
from database import base, engine
from database import sessionLocal


def create_db():
    return base.metadata.create_all(bind=engine)


async def create_user(user: UserSchema):
    user = User(Firstname=user.Firstname,Lastname=user.Lastname)
    with sessionLocal() as session:
        try:
            session.add(user)
            session.commit()
            push_to_rabbitmq("user")
        except:
            print("an error was occured")
    return user
