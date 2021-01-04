# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Championdto(models.Model):
    version = models.CharField(max_length=20)
    id = models.CharField(max_length=20, blank=True, null=True)
    key = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    blurb = models.CharField(max_length=1000, blank=True, null=True)
    info = models.JSONField(blank=True, null=True)
    image = models.JSONField(blank=True, null=True)
    tags = models.CharField(max_length=100, blank=True, null=True)
    partype = models.CharField(max_length=20, blank=True, null=True)
    stats = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'championdto'
        unique_together = (('key', 'version'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ElectionsCandidate(models.Model):
    name = models.CharField(max_length=10)
    introduction = models.TextField()
    area = models.CharField(max_length=15)
    party_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'elections_candidate'


class Leagueentrydto(models.Model):
    leagueid = models.CharField(db_column='leagueId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    summonerid = models.CharField(db_column='summonerId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    summonername = models.CharField(db_column='summonerName', primary_key=True, max_length=50)  # Field name made lowercase.
    queuetype = models.CharField(db_column='queueType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tier = models.CharField(max_length=50, blank=True, null=True)
    rank = models.CharField(max_length=5, blank=True, null=True)
    leaguepoints = models.IntegerField(db_column='leaguePoints', blank=True, null=True)  # Field name made lowercase.
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    hotstreak = models.IntegerField(db_column='hotStreak', blank=True, null=True)  # Field name made lowercase.
    veteran = models.IntegerField(blank=True, null=True)
    freshblood = models.IntegerField(db_column='freshBlood', blank=True, null=True)  # Field name made lowercase.
    inactive = models.IntegerField(blank=True, null=True)
    miniseries = models.JSONField(db_column='miniSeries', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'leagueentrydto'


class Matchreferencedto(models.Model):
    gameid = models.BigIntegerField(db_column='gameId', primary_key=True)  # Field name made lowercase.
    role = models.CharField(max_length=20, blank=True, null=True)
    season = models.IntegerField(blank=True, null=True)
    platformid = models.CharField(db_column='platformId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    champion = models.IntegerField(blank=True, null=True)
    queue = models.IntegerField(blank=True, null=True)
    lane = models.CharField(max_length=10, blank=True, null=True)
    timestamp = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matchreferencedto'


class Summonerdto(models.Model):
    accountid = models.CharField(db_column='accountId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    profileiconid = models.IntegerField(db_column='profileIconId', blank=True, null=True)  # Field name made lowercase.
    revisiondate = models.BigIntegerField(db_column='revisionDate', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(primary_key=True, max_length=50)
    id = models.CharField(max_length=100, blank=True, null=True)
    puuid = models.CharField(max_length=100, blank=True, null=True)
    summonerlevel = models.BigIntegerField(db_column='summonerLevel', blank=True, null=True)  # Field name made lowercase.
    apikey = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'summonerdto'
