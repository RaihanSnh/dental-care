from odoo import api, fields, models

class Doctor(models.Model):
    _name = 'dental.care.doctor'
    _description = 'Data Doctor'

    
    doctor_id = fields.Many2one(
        string='Doctor',
        comodel_name='res.partner',
        domain="[('is_doctor', '=', True)]",
        required=True
    )

    
    service_id = fields.Many2one(
        string='Service',
        comodel_name='dental.care.service',
        ondelete='restrict',
    )