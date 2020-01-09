from odoo import models, fields, api
from odoo.exceptions import ValidationError

class owner(models.Model):
    _name = "training.owner"
    _description = "owner record"
    _rec_name="owner_name"

    owner_name = fields.Char(String="owner_name")
    email = fields.Text(String="owner_email")
    password = fields.Text(String="owner_password")
    state=fields.Selection([
        ('Start','Start'),
        ('Running','Running'),
        ('Complete','Complete'),
        ],string="state",default="Start",readonly=True)

    def button_start(self):
       for rec in self:
           rec.write({'state': 'Start'})

    def button_running(self):
        for rec in self:
            rec.write({'state': 'Running'})

    def button_Stop(self):
        for rec in self:
            rec.write({'state': 'Complete'})

class tenant(models.Model):
    _name="training.tenant"
    _description="tenant table"  
    _rec_name="tenant_name"

    @api.constrains('phone')
    def _check_number(self):
        if self.phone:
            print(self.phone)
            if self.phone > 10:
                raise ValidationError("please, enter only 10 digit")

    tenant_id = fields.Char(String="tenant_id")
    tenant_name=fields.Char(String="tenant_name")
    dob=fields.Date(String="date of birth")
    phone=fields.Integer(String="number")
    gender=fields.Selection([('Male','Male'),('Female','Female')],String="gender")
    email = fields.Text(String="tenant_email")
    Marital_status=fields.Selection([('Single','Single'),('Married','Married')],String="Marital_status")
    Religion = fields.Text(String="Religion")
    Home_address = fields.Text(String="Parmanet Address")
    Father_name=fields.Text(String="Parmanet Address")
    Fphone=fields.Integer(String="Father's Number")
    Occupation=fields.Selection([('Study', 'Study'),('Job','Job')],String="Occupation")
    Joining_date=fields.Date(String="Check-In date")
    room_ids=fields.Many2one("training.room",String="room ids")
    

class room(models.Model):
    _name="training.room"
    _description="room table"
    _rec_name="roomNumber"

    hostelId=fields.Many2one("training.hostel",String="Many Rooms")
    roomNumber=fields.Integer(String="room Numbers")
    allot_ids=fields.One2many("training.roomallotment","hostelIds",String="hostelIds")


class hostel(models.Model):
    _name="training.hostel"
    _description="hostel table"

    roomIDs=fields.One2many("training.room","hostelId",String="One Hostel")
    name=fields.Char(string="HostelName")
    featname=fields.Many2many("training.roomfeature",String="featname")
    
            
class roomfeature(models.Model):
    _name="training.roomfeature"
    _description="room feature table"
    _rec_name="featurename"

    featurename=fields.Char(String="featurename")
    dess=fields.Char(String="Description")

class roomallotment(models.Model):
    _name="training.roomallotment"
    _description="room Allotment"
    _rec_name="allot_id"
 
    @api.depends('Paymnent')
    def set_rent_month(self):
        if self.Paymnent:
            # print(type(self.Paymnent))
            # print(type(1))
            if self.Paymnent == '1':
                self.Total_rent = 1 * 5500
            elif self.Paymnent == '3':
                self.Total_rent = 3 * 5500
            elif self.Paymnent == '6':
                self.Total_rent= 6 * 5500
            elif self.Paymnent == '12':
                self.Total_rent= 12 * 5500

    allot_id=fields.Integer(String="Allotment ID")
    allot_date=fields.Date(String="Allotment Date")
    allotOut_date=fields.Date(String="Check-out Date")
    Total_rent=fields.Integer(String="Total Rent",compute="set_rent_month",store=True)
    Paymnent=fields.Selection([('1','1'),('3','3'),('6','6'),('12','12')],String="Paymnent Months")
    hostelIds=fields.Many2one("training.room",String="Many Rooms")







