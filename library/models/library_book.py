from odoo import models, fields, api


class Livre(models.Model):
    _name = 'library.library'
    _description ="Livre"

    name = fields.Char('Title', required=True) 
    isbn = fields.Char('ISBN')
    accessible = fields.Boolean('Accessible?', default=True)
    date_pub = fields.Date()
    image = fields.Binary('Cover')
    auteur = fields.Many2many('res.partner',string='Auteurs')
    publisher = fields.Many2one('res.partner', string='Publisher')

