# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

@python_2_unicode_compatible
class BbrAddress(models.Model):
    addrid = models.IntegerField(primary_key=True)
    street = models.CharField(max_length=4000)
    city = models.CharField(max_length=4000)
    state = models.CharField(max_length=4000)
    zip = models.IntegerField()
    def __str__(self):
        return unicode(self.addrid)
    class Meta:
        managed = False
        db_table = 'bbr_address'


class BbrCage(models.Model):
    cageid = models.IntegerField(primary_key=True)
    statusid = models.ForeignKey('BbrStatus', models.DO_NOTHING, db_column='statusid')

    class Meta:
        managed = False
        db_table = 'bbr_cage'


class BbrCoachsession(models.Model):
    csid = models.IntegerField(primary_key=True)
    employeeid = models.ForeignKey('BbrEmployee', models.DO_NOTHING, db_column='employeeid')
    cageid = models.ForeignKey(BbrCage, models.DO_NOTHING, db_column='cageid')

    class Meta:
        managed = False
        db_table = 'bbr_coachsession'


class BbrCustomer(models.Model):
    custid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=4000)
    lname = models.CharField(max_length=4000)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=4000, blank=True, null=True)
    paymenttype = models.CharField(max_length=4000, blank=True, null=True)
    addressid = models.ForeignKey(BbrAddress, models.DO_NOTHING, db_column='addressid')

    class Meta:
        managed = False
        db_table = 'bbr_customer'


class BbrEmployee(models.Model):
    employid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=4000)
    lname = models.CharField(max_length=4000)
    addressid = models.ForeignKey(BbrAddress, models.DO_NOTHING, db_column='addressid')

    class Meta:
        managed = False
        db_table = 'bbr_employee'


class BbrMeetingroom(models.Model):
    meetid = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'bbr_meetingroom'


class BbrMembership(models.Model):
    memid = models.IntegerField(primary_key=True)
    purchaseddate = models.DateTimeField()
    type = models.CharField(max_length=4000)
    enddate = models.DateTimeField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    customerid = models.ForeignKey(BbrCustomer, models.DO_NOTHING, db_column='customerid')

    class Meta:
        managed = False
        db_table = 'bbr_membership'


class BbrMiscequipment(models.Model):
    miscid = models.IntegerField(primary_key=True)
    bat = models.CharField(max_length=4000, blank=True, null=True)
    helmet = models.CharField(max_length=4000, blank=True, null=True)
    glove = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bbr_miscequipment'


class BbrPitchingmachine(models.Model):
    pitchid = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=4000)

    class Meta:
        managed = False
        db_table = 'bbr_pitchingmachine'


class BbrRadar(models.Model):
    radid = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bbr_radar'


class BbrRentalagreement(models.Model):
    raid = models.IntegerField(primary_key=True)
    datecreated = models.DateTimeField()
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    rate = models.DecimalField(max_digits=12, decimal_places=2)
    customerid = models.ForeignKey(BbrCustomer, models.DO_NOTHING, db_column='customerid')
    misc_equipmentid = models.ForeignKey(BbrMiscequipment, models.DO_NOTHING, db_column='misc_equipmentid', blank=True, null=True)
    cageid = models.ForeignKey(BbrCage, models.DO_NOTHING, db_column='cageid', blank=True, null=True)
    coach_sessionid = models.ForeignKey(BbrCoachsession, models.DO_NOTHING, db_column='coach_sessionid', blank=True, null=True)
    pitching_machineid = models.ForeignKey(BbrPitchingmachine, models.DO_NOTHING, db_column='pitching_machineid', blank=True, null=True)
    radarid = models.ForeignKey(BbrRadar, models.DO_NOTHING, db_column='radarid', blank=True, null=True)
    meeting_roomid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bbr_rentalagreement'


class BbrStatus(models.Model):
    statusid = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=4000)

    class Meta:
        managed = False
        db_table = 'bbr_status'


class BbrUsers(models.Model):
    userid = models.FloatField(primary_key=True)
    uname = models.CharField(max_length=20)
    pass_field = models.CharField(db_column='pass', max_length=20)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'bbr_users'

class UserProfile(models.Model):
	user = models.OneToOneField(User)

	def __unicode__(self):
		return self.user.username


