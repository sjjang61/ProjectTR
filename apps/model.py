from database import Base, init_db
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Unicode, CHAR
from sqlalchemy.orm import relationship

#########################################################################
# Structure of Star
#+-------------+---------------+------+-----+---------+----------------+
#| Field       | Type          | Null | Key | Default | Extra          |
#+-------------+---------------+------+-----+---------+----------------+
#| s_id        | int(11)       | NO   | PRI | NULL    | auto_increment |
#| s_desc      | varchar(1024) | YES  |     | NULL    |                |
#| s_img_url   | varchar(1024) | YES  |     | NULL    |                |
#| s_trans_key | int(11)       | YES  |     | NULL    |                |
#+-------------+---------------+------+-----+---------+----------------+

class User(Base):
    __tablename__ = 't_user'
    user_id = Column(Integer, primary_key=True, autoincrement=True) #index=True
    name = Column(String(32))
    id = Column(String(32))
    level = Column(Integer)
    score = Column(Integer)

    heroes = relationship('UserHero', backref='user', cascade='all, delete, delete-orphan')
    squads = relationship('UserSquad', backref='user', cascade='all, delete, delete-orphan')

    # @property
    # def serialize(self):
    #     return {
    #         'user_id': self.user_id,
    #         'name': self.name
    #     }

    # def columns_to_dict(self):
    #     dict_ = {}
    #     for key in self.__mapper__.c.keys():
    #         dict_[key] = getattr(self, key)
    #     return dict_

    def __init__(self, name, id ):
        self.name = name
        self.id = id
        self.level = 1
        self.score = 0

    def __repr__(self):
        return '<user %r, %r>' % ( self.id, self.heroes )



class UserHero(Base):
    __tablename__ = 't_user_hero'
    user_id = Column(Integer, ForeignKey(User.user_id), primary_key=True)
    hero_id = Column(Integer, primary_key=True)

    # user = relationship('User', backref='heroes', cascade='all, delete, delete-orphan')
    # crawls = relationship('Crawl', backref='star', cascade='all, delete, delete-orphan')
    # user = relationship( "User", backref=backref("addresses", order_by=id))

    def __init__(self, user_id, hero_id ):
        self.user_id = user_id
        self.hero_id = hero_id

    def __repr__(self):
        return '<user_hero %r:%r>' % ( self.user_id, self.hero_id)



class UserSquad(Base):
    __tablename__ = 't_user_squad'
    user_id = Column(Integer, ForeignKey(User.user_id), primary_key=True)
    hero_id = Column(Integer, primary_key=True)
    pos_x = Column(Integer)
    pos_y = Column(Integer)

    def __init__(self, user_id, hero_id, pos_x, pos_y ):
        self.user_id = user_id
        self.hero_id = hero_id
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __repr__(self):
        return '<user_squad user_id:%r, hero_id:%r, pos_x:%r,  pos_y:%r>' % ( self.user_id, self.hero_id, self.pos_x, self.pos_y )


class Match(Base):
    __tablename__ = 't_match'
    match_id = Column(Integer, primary_key=True)
    host_user_id = Column(Integer, ForeignKey(User.user_id))
    guest_user_id = Column(Integer, ForeignKey(User.user_id))
    channel_id = Column(Integer)

    def __init__(self, host_user_id, guest_user_id, channel_id ):
        self.host_user_id = host_user_id
        self.guest_user_id = guest_user_id
        self.channel_id = channel_id

    def __repr__(self):
        return '<user_squad host_user:%r, guest_user:%r, channel_id:%r>' % ( self.host_user_id, self.guest_user_id, self.channel_id )



if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print("Creating database tables...")
    # db.create_all()
    init_db()
