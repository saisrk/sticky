from datetime import datetime

from flask_login import UserMixin
from flask_bcrypt import generate_password_hash, check_password_hash
from peewee import *

DATABASE = SqliteDatabase("sticky.db")

CHOICES = [
    ('High', 'High'),
    ('Low', 'Low')
]

class Note(Model):
    nid = IntegerField(unique=True, primary_key=True)
    note = TextField()
    priority = CharField(choices=CHOICES)
    notedate = DateTimeField(default=datetime.now)

    class Meta:
        database = DATABASE

    @classmethod
    def create_note(cls, nid, note, priority, date):
        try:
            cls.create(
                nid=nid,
                note=note,
                priority=priority,
                notedate=date)
        except IntegrityError, e:
            raise ValueError("Note Already exists")


class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        database = DATABASE
        order_by = ('-joined_at',)

    @classmethod
    def create_user(cls, username, email, password, is_admin=False):
        try:
            cls.create(
                username=username,
                email=email,
                password=generate_password_hash(password),
                is_admin=is_admin)
        except IntegrityError, e:
            raise ValueError("User Already exists")