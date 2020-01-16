from odoo import models,api,fields

# class owner(models.Model)
class owner(models.Model):
    _name = "training.owner"
    _description = "owner record"
    _rec_name="owner_name"

    owner_name = fields.Char(String="owner_name")
    RoomDetail=fields.Char(String="RoomDetail")
    RoomType=fields.Char(String="RoomType")

class room(models.Model):
    _name="training.room"
    _description="room table"

    hostelId=fields.Many2one("training.owner",String="Many Rooms")
    roomNumber=fields.Integer(String="room Numbers")
