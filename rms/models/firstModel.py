from odoo import models, fields, api

class owner(models.Model):
	_name = "training.owner"
	_description = "owner record"
	_rec_name="owner_name"


	owner_id = fields.Char(String="owner_id")
	owner_name = fields.Char(String="owner_name")
	email = fields.Text(String="owner_email")
	password = fields.Text(String="owner_password")

class tenant(models.Model):
	_name="training.tenant"
	_description="tenant table"
	_rec_name="tenant_name"

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

	# @api.onchange('roomNumber')
	# def set_Hostel_name(self):
	# 	if self.roomNumber:
	# 		self.Hostelname=self.roomNumber.name

	hostelId=fields.Many2one("training.hostel",String="Many Rooms")
	roomNumber=fields.Integer(String="room Numbers")
	# Hostelname=fields.Char(string="HostelName")



class hostel(models.Model):
	_name="training.hostel"
	_description="hostel table"

	roomID=fields.One2many("training.room","hostelId",String="One Hostel")
	name=fields.Char(string="HostelName")
	
			
class roomfeature(models.Model):
	_name="training.roomfeature"
	_description="room feature table"
	_rec_name="featurename"

	#Compute Example
	# @api.depends('t_age')
	# def set_age_group(self):
	# 	if self.t_age:
	# 		if self.t_age < 18:
	# 			self.age_group='miner'
	# 		else:
	# 			self.age_group='major'



	featurename=fields.Char(String="fname")
	dess=fields.Char(String="Description")
	hostelIds=fields.Many2many("training.hostel",String="hostelIds")
	# age_group=fields.Selection([
	# 	('major','Major'),
	# 	('miner','Miner')
	# 	],string="age_group",compute="set_age_group")
	# t_age=fields.Integer(String="age")

class roomAllotment(models.Model):
	_name="training.roomAllotment"
	_description="room Allotment"

	#Compute Example
	@api.depends('Total_rent')
	def set_rent_month(self):
		if self.Paymnent:
	 		if self.Paymnent = 1:
	 			self.Total_rent= 1*5500
	 		elif self.Paymnent = 3:
	 			self.Total_rent= 3*5500
	 		elif self.Paymnent = 6:
	 			self.Total_rent= 6*5500
	 		elif self.Paymnent = 12:
	 			self.Total_rent=12*5500

	allot_id=fields.Integer(String="Allotment ID")
	allot_date=fields.date(String="Allotment Date")
	Paymnent=fields.Selection([('1','1'),('3','3'),('6','6'),('12','12')],String="Paymnent Months",compute="set_rent_month")
	Total_rent=fields.Integer(String="Total Rent")





	
		


