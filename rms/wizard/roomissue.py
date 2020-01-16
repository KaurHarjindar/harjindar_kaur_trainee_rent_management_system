from odoo import models, fields, api
from openerp.exceptions import UserError, ValidationError, Warning

class roomissue(models.TransientModel):
    _name="training.roomissue"
    _description="roomissue table"

    issueType=fields.Char(String="issueType")
    issuedes=fields.Char(String="issue detail")

    def create_request(self):
        print ("You click finish")
        return True