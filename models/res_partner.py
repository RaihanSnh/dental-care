from odoo import api, fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    is_doctor = fields.Boolean(
        string='Doctor',
        default=False
    )

    is_patient = fields.Boolean(
        string='Patient',
        default=False
    )

    phone = fields.Char(
        string='Emergency Number',
        help='Phone number to contact in case of emergency'
    )