from odoo import models, fields, api
from odoo.exceptions import ValidationError

class owner(models.Model):
    _name = "training.owner"
    _description = "owner record"

    name = fields.Char(String="First name")
    lastname =fields.Char(String="Last name")
    number=fields.Char(String="Contact Number",size=10)
    email=fields.Char(String="Email")
    address=fields.Char(String="Current Address")
    city=fields.Char(String="City")
    state=fields.Char(String="State")

class property(models.Model):
    _name = "training.property"
    _description = "property record"

    name=fields.Char(String="Property Name")
    ptype=fields.Selection([('Apartment', 'Apartment'),('Flate','Flate')],String="Property Type")
    address=fields.Char(String="Current Address")
    city=fields.Char(String="City")
    state=fields.Char(String="State")
    location=fields.Char(String="Location/Area")
    ownername=fields.Many2one("training.owner",String="Owner Name")
    policies=fields.Char(String="Policies")


class Rooms(models.Model):
    _name = "training.rooms"
    _description = "Room record"

    propertyname=fields.Many2one("training.property",String="Property Name")
    block=fields.Integer(String="No. of Block")
    floor=fields.Integer(String="Floor")
    roomnumber=fields.Integer(String="No. of Rooms")
    Bothroom=fields.Integer(String="Bothroom")
    ownername=fields.Many2one("training.owner",String="Owner Name")
    status=fields.Selection([('Vacant','Vacant'),('Booked','Booked'),('Renovate','Renovate')],String="Status")


class tenants(models.Model):
    _name = "training.tenants"
    _description = "tenants record"

    name=fields.Char(String="tenant Name")
    dob=fields.Date(String="date of birth")
    phone=fields.Char(String="Contact Number",size=10)
    gender=fields.Selection([('Male','Male'),('Female','Female')],String="gender")
    email = fields.Text(String="tenant_email")
    Occupation=fields.Selection([('Study', 'Study'),('Job','Job')],String="Occupation")
    Marital_status=fields.Selection([('Single','Single'),('Married','Married')],String="Marital_status")
    Religion = fields.Text(String="Religion")
    Home_address = fields.Text(String="Parmanet Address")
    Father_name=fields.Text(String="Parmanet Address")
    Fphone=fields.Char(String="Father's Contact",size=10)
    # Joining_date=fields.Date(String="Check-In date")

class tenantroomselection(models.Model):
    _name="training.tenantroomselection"
    _description="tenants room selection"

    name=fields.Many2one("training.tenants",String="Tenant Name")
    propertyname=fields.Many2one("training.property",String="Property Name")
    ownername=fields.Many2one("training.owner",String="Owner Name")
    Joining_date=fields.Date(String="Check-In date")

class tenantroomallocate(models.Model):
    _name="training.tenantroomallocate"
    _description="tenant room allocation"

    propertyname=fields.Many2one("training.property",String="Property Name")
    roomnumber=fields.Integer(String="Room Number")
    tenantname=fields.Many2many("training.tenants",String="Tenant Name")
    rent=fields.Integer(String="Rent",help="Per Month of one room" )
    status=fields.Selection([('Paid','Paid'),('Not Paid','Not Paid')],String="Payment Status")
    Joining_date=fields.Date(String="Check-In date")