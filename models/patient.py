from odoo import api, fields, models

class Patient(models.Model):
    _name = 'dental.care.patient'
    _description = 'Data Patient'

    
    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='res.partner',
        domain="[('is_patient', '=', True)]",
        required=True
    )

    emergency_number = fields.Char(
        string='Emergency Number',
        related='patient_id.phone',
        readonly=False
    )

    date_of_birth = fields.Date(
        string='Date Of Birth'
    )

    
    blood_type = fields.Selection(
        string='Blood Type',
        selection=[
            ('a', 'A'),
            ('b', 'B'),
            ('ab', 'AB'),
            ('o', 'O'),
        ],
    )
    
    height = fields.Float(
        string='Height',
    )

    
    weight = fields.Float(
        string='Weight',
    )

    
    is_vaccinated = fields.Boolean(
        string='Is Vaccinated',
    )
    
    
    vaccine_name = fields.Char(
        string='Vaccine Name',
    )

    image = fields.Binary(string="", attachment=True)