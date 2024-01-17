from odoo import api, fields, models

class Service(models.Model):
    _name = 'dental.care.service'
    _description = 'Data Service'

    name = fields.Char(string='Name')

    floor = fields.Integer(string='Floor')

    room = fields.Char(string='Room')    