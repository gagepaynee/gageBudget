# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
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
    first_name = models.CharField(max_length=30)
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


class Expense(models.Model):
    expenseid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=13, decimal_places=2)  # Field name made lowercase.
    startduedate = models.DateField(db_column='StartDueDate')  # Field name made lowercase.
    active = models.IntegerField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    expensefrequencyid = models.ForeignKey('Expensefrequency', models.DO_NOTHING, db_column='ExpenseFrequencyId')  # Field name made lowercase.
    expensetypeid = models.ForeignKey('Expensetype', models.DO_NOTHING, db_column='ExpenseTypeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'expense'


class Expensefrequency(models.Model):
    expensefrequencyid = models.AutoField(primary_key=True)
    expensefrequencyname = models.CharField(db_column='ExpenseFrequencyName', max_length=30)  # Field name made lowercase.
    payperiodid = models.ForeignKey('Payperiod', models.DO_NOTHING, db_column='PayPeriodId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'expensefrequency'


class Expensetype(models.Model):
    expensetypeid = models.AutoField(primary_key=True)
    expensetypename = models.CharField(db_column='ExpenseTypeName', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'expensetype'


class Goal(models.Model):
    goalid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=0)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=80)  # Field name made lowercase.
    remainingamount = models.DecimalField(db_column='RemainingAmount', max_digits=13, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    currentamount = models.DecimalField(db_column='CurrentAmount', max_digits=13, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paychecksremaining = models.IntegerField(db_column='PaychecksRemaining', blank=True, null=True)  # Field name made lowercase.
    paychecksused = models.IntegerField(db_column='PaychecksUsed', blank=True, null=True)  # Field name made lowercase.
    isprimarygoal = models.IntegerField(db_column='IsPrimaryGoal', blank=True, null=True)  # Field name made lowercase.
    duedate = models.DateField(db_column='DueDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goal'


class Incomesource(models.Model):
    incomesourceid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=40)  # Field name made lowercase.
    isprimary = models.IntegerField(db_column='IsPrimary', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'incomesource'


class Paycheck(models.Model):
    paycheckid = models.AutoField(primary_key=True)
    incomesourceid = models.ForeignKey(Incomesource, models.DO_NOTHING, db_column='IncomeSourceId')  # Field name made lowercase.
    payperiodid = models.ForeignKey('Payperiod', models.DO_NOTHING, db_column='PayPeriodId')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=13, decimal_places=2)  # Field name made lowercase.
    datereceived = models.DateField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paycheck'


class Payperiod(models.Model):
    payperiodid = models.AutoField(primary_key=True)
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    day = models.CharField(db_column='Day', max_length=2)  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length=2, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payperiod'


class Payperiodexpense(models.Model):
    payperiodid = models.ForeignKey(Payperiod, models.DO_NOTHING, db_column='PayPeriodId', primary_key=True)  # Field name made lowercase.
    expenseid = models.ForeignKey(Expense, models.DO_NOTHING, db_column='ExpenseId')  # Field name made lowercase.
    payperioddate = models.DateField(db_column='PayPeriodDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payperiodexpense'
        unique_together = (('payperiodid', 'expenseid', 'payperioddate'),)


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    firstname = models.CharField(db_column='FirstName', max_length=30)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=30)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
