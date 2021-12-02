from django.db import models

class Player(models.Model):
    login = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    nickname = models.CharField(unique=True, max_length=255)
    score = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'player'

class Developer(models.Model):
    login = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'developer'


class Post(models.Model):
    article = models.TextField(blank=True, null=True)
    developer = models.ForeignKey('Developer', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'

