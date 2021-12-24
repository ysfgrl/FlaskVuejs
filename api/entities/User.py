import mongoengine as me
class User(me.Document):
    name = me.StringField()
    surname = me.StringField()
    username = me.StringField(required=True)
    password = me.StringField(required=True)
    profile = me.StringField()

