from odoo import models, fields, api
from odoo.exceptions import ValidationError


class inquiry(models.Model):
    _name="training.inquiry"
    _description="tenant training inquiry"

    name=fields.Char(string="Name")
    email=fields.Char(string="E-mail")
    phone=fields.Char(string="Contact Number",size=10)
    CheckIn=fields.Date(string="CheckIn Date")
    Checkout=fields.Date(string="Checkout Date")
    Intrestin=fields.Selection([('site visit','site visit'),('Direct Rent','Direct Rent')],string="Intrest in")
    state = fields.Selection([
            ('concept', 'Concept'),
            ('started', 'Started'),
            ('progress', 'In progress'),
            ('finished', 'Done'),
            ],default='concept')

    def concept_progressbar(self):
        self.write({
            'state': 'concept',
        })
    def started_progressbar(self):
        self.write({
        'state': 'started'
        })
    def progress_progressbar(self):
        self.write({
        'state': 'progress'
        })
    def done_progressbar(self):
        self.write({
        'state': 'finished',
        })




class propertyregi(models.Model):
    _name="training.propertyregi"
    _description="training property registration"

    #basic Information
    ptype=fields.Selection([('Apartment', 'Apartment'),('Flate','Flate')],string="Property Type")
    pgfor=fields.Selection([('Girls','Girls'),('Boys','Boys')],string="PG is available for")
    share=fields.Selection([('Shared','Shared'),('Private','Private')],string="PG is")
    address=fields.Char(string="Current Address")
    city=fields.Char(string="City")
    state=fields.Char(string="State")
    location=fields.Char(string="Location/Area")

    #property detail
    rentPerBed=fields.Integer(string="Expected Rent Per Bed")
    maintance=fields.Integer(string="Maintenance Charges")
    maintype=fields.Selection([
        ('Monthly','Monthly'),
        ('Annually','Annually'),
        ('one Time','one Time'),
        ],string="Maintenance Type")
    deposite=fields.Integer(string="Deposite")

    include=fields.Many2many('training.features',string="Which included in rent")
    hide=fields.Boolean(string="hide",compute="check")
    weekday=fields.Many2many('training.food',string="WeekDay")

    foodtype=fields.Selection([
        ('Veg','Veg'),
        ('Veg and NonVeg','Veg and NonVeg')
        ])
    bedrooms=fields.Integer(string="Total Room")
    furnish=fields.Selection([
        ('UnFurnished','UnFurnished'),
        ('SemiFurnished','SemiFurnished'),
        ('FullyFurnished','FullyFurnished')
        ],string="Room Furnishing")
    beds=fields.Integer(string="Beds Availblein PG")
    tenants=fields.Integer(string="Max tenants in PG")
    Propertyfloor=fields.Selection([
        ('Ground','Ground'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')
        ],string="Property Floor")
    Totalfloor=fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5')],string="Total Floor")
    AvialbleFrom=fields.Date(string="Avialble From")
    rules=fields.Selection([
        ('visitors','visitors Allowed'),
        ('smoking','Smoking Allowed'),
        ],string="House Rules")
    lentry=fields.Char(string="Last Entry Time")
    image = fields.Binary(string="Image",attachment=True)

    @api.onchange('include')
    def check(self):
        self.hide=False
        # print('\n\n\n\n : : ', self.include)
        for i in self.include:
            result = self.env['training.features'].browse([i.id])
            if result.name == 'Food':
                self.hide = True


class features(models.Model):
    _name="training.features"
    _description="training features"

    name=fields.Char(string="name")  

class food(models.Model):
    _name="training.food"
    _description="training food"

    name=fields.Char(string="name")  


class tenant(models.Model):
    _name="training.tenants"
    _description="tenant registration"

    name=fields.Char(string="tenant Name")
    dob=fields.Date(string="date of birth")
    phone=fields.Char(string="Contact Number",size=10)
    gender=fields.Selection([('Male','Male'),('Female','Female')],string="gender")
    email = fields.Char(string="tenant_email")
    Occupation=fields.Selection([('Study', 'Study'),('Job','Job')],string="Occupation")
    Home_address = fields.Text(string="Parmanet Address")
    Father_name=fields.Text(string="Father's Name")
    Fphone=fields.Char(string="Father's Contact",size=10)
    status = fields.Selection([
            ('Paid', 'Paid'),
            ('Not', 'Not Paid'),
            ],string='Status',default="Not")

    @api.depends('status')
    def checkstatus(self):
        if self.status != 'Paid':
            self.write({'status': 'Paid'})
        else:
            self.write({'status': 'Not'})

class bill(models.Model):
    _name="training.bill"
    _description="tenant total bill"

    billtype=fields.Selection([
        ('Electricity','Electricity Bill'),
        ('Food','Food Bill'),
        ('Water','Water Bill'),
        ('internet','Internet Bill'),
        ('Maintenance','Maintenance'),('Rent','Rent')
        ],string="Select Bill Type",default="Electricity")
    
    hide=fields.Boolean(string="hide",compute="check")
    tenantname=fields.Many2one('training.tenants',string="Tenant Name")
    bdate=fields.Date(string="date of bill")
    payment=fields.Float(string="Total Amount")

    @api.depends('billtype')
    def check(self):
        self.hide=False
        if self.billtype == 'Rent':
            self.hide = True





        