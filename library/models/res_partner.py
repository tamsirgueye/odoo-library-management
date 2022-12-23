from odoo import models, fields

class ResPartner(models.Model):
    _inherit = ["res.partner"]

    is_author = fields.Boolean('is_author')
    is_publisher = fields.Boolean('is_publisher')