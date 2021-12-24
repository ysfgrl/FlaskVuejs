import mongoengine as me
class Person(me.Document):
    name = me.StringField()
    surname = me.StringField()
    tckn = me.StringField(required=True, max_length=11, min_length=11)
    username = me.StringField(required=True)
    password = me.StringField(required=True)
    profile = me.StringField()

