import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Float

with open('mysql.json', encoding='utf-8') as con_json:
    con_dict = json.load(con_json)

engine = create_engine(
    'mysql+mysqlconnector://{}:{}@{}:3306/{}'.format(con_dict['user'], con_dict['passwd'], con_dict['host'],
                                                     con_dict['database']),
    connect_args={'auth_plugin': 'mysql_native_password'})

# 创建对象的基本类
Base = declarative_base()


# 定义 Player 对象
class Player(Base):
    # 标的名字
    __tablename__ = 'player'

    # 表的结构
    player_id = Column(Integer, primary_key=True, autoincrement=True)
    team_id = Column(Integer)
    player_name = Column(String(255))
    height = Column(Float(3, 2))


# 创建 DBSession 类型
DBSession = sessionmaker(bind=engine)
# 创建 session 对象
session = DBSession()
# 创建 Player 对象
new_player = Player(team_id=1003, player_name='约翰-科林斯', height=2.08)
# 添加到session
session.add(new_player)
# 提交及保存到数据库
session.commit()
# 关闭 session
session.close()
