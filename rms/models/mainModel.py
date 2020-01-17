from odoo import models, fields, api
from odoo.exceptions import ValidationError

class owner(models.Model):
    _name = "training.owner"
    _description = "owner record"

    @api.constrains("number")
    def check_num(self):
        for rec in self:
            print(rec)
            if len(rec.number) > 10:
                raise ValidationError("enter right number")
        return True

    name = fields.Char(String="First name")
    lastname =fields.Char(String="Last name")
    number=fields.Char(String="Contact Number")
    email=fields.Char(String="Email")
    address=fields.Char(String="Current Address")
    city=fields.Char(String="City")
    state=fields.Char(String="State")

class property(models.Model):
    _name = "training.property"
    _description = "property record"
 
    name=fields.Char(String="PropertyName")
    ptype=fields.Selection([('Apartment', 'Apartment'),('Flate','Flate')],String="Property Type")
    address=fields.Char(String="Current Address")
    city=fields.Char(String="City")
    state=fields.Char(String="State")
    location=fields.Char(String="Location/Area")
    ownername=fields.Char(String="Owner Name")
    policies=fields.Char(String="Policies")


class Rooms(models.Model):
    _name = "training.rooms"
    _description = "Room record"

    @api.depends("propertyname")
    def oname(self):
        self.ownerName = self.propertyname.ownername
        
    propertyname=fields.Many2one("training.property",String="Property Name")
    block=fields.Char(String="No. of Block")
    floor=fields.Integer(String="Floor")
    roomnumber=fields.Char(String="No. of Rooms")
    # Bothroom=fields.Integer(String="Bothroom")
    ownerName=fields.Char(compute="oname",String="Owner Name")
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
      
    @api.depends('propertyname')
    def addr(self):
            self.address=self.propertyname.address
            self.city=self.propertyname.city
            self.state=self.propertyname.state

    @api.depends('rent')
    def calculate(self):
        if self.rent:
            if self.rent == '1':
                self.Total_rent= 1 * 5500
            elif self.rent == '3':
                self.Total_rent = 3 * 5500
            elif self.rent == '6':
                self.Total_rent= 6 * 5500
            elif self.rent == '12':
                self.Total_rent= 12 * 5500

    # @api.depends('Joining_date','leave_date')
    # def duration(self):
    #         date_format = "%m/%d/%Y"
    #         init_date = datetime.strptime(self.Joining_date, date_format)
    #         end_date = datetime.strptime(self.leave_date, date_format)
    #         print(init_date)

    name=fields.Many2one("training.tenants",String="Tenant Name")
    propertyname=fields.Many2one("training.property",String="Property Name")
    ownerName=fields.Char(String="Owner Name",related="propertyname.ownername")
    address=fields.Char(compute="addr",String="Address")
    city=fields.Char(compute="addr",String="City")
    state=fields.Char(compute="addr",String="State")
    Joining_date=fields.Date(String="Check-In date")
    leave_date=fields.Date(String="Check-out date")
    rent=fields.Selection([('1','1 Month'),('3','3 Months'),('6','6 Months'),('12','12 Months')],String="Paymnent Months")
    Total_rent=fields.Integer(String="Total Rent",compute="calculate",store=True)
    months=fields.Date(compute="duration",String="Days")

class tenantroomallocate(models.Model):
    _name="training.tenantroomallocate"
    _description="tenant room allocation"

    @api.depends("pname")
    def tent(self):
        self.tname=self.pname.name


    pname=fields.Many2one("training.rooms",String="property name")
    roomnumber=fields.Char(related="pname.roomnumber",String="Room Number")
    tenantname=fields.Many2many("training.tenants",String="Tenant Name")
    rent=fields.Integer(String="Rent",help="Per Month of one room" )
    status=fields.Selection([('Paid','Paid'),('Not Paid','Not Paid')],String="Payment Status")
    Joining_date=fields.Date(String="Check-In date")