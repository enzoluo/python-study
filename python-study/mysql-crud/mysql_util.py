from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import User

#创建引擎


#create session
def get_session(_ip, _port, _userName, _password, _database):
    url = "mysql+mysqlconnector://$userName:$password@$ip:$port/$database"
    url = url.replace('$ip', _ip).replace('$port', _port).replace(
        '$userName',
        _userName).replace('$password',
                           _password).replace('$database', _database)
    engine = create_engine(url)
    db_session = sessionmaker(bind=engine)
    session = db_session()
    return session


def insert_user(_session, _user):
    if isinstance(_user, list):
        _session.add_all(_user)
    else:
        _session.add(_user)
    _session.commit()


if __name__ == "__main__":
    ip = 'localhost'
    port = '3306'
    user_name = 'root'
    password = 'root'
    database = 'python'
    session = get_session(ip, port, user_name, password, database)

    user1 = User(name='enzo', age=11, birth_day='2020-11-11')
    user2 = User(name='lisi', age=23, birth_day='1990-02-23')
    insert_user(session, [user1,user2])

    res = session.query(User).all()
    print(1)