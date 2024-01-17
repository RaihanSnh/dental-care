from odoo import api, fields, models

from datetime import timedelta

class Appointment(models.Model):
    _name = 'dental.care.appointment'
    _description = 'Data Appointments'

    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='res.partner',
        domain="[('is_patient', '=', True)]",
        required=True
    )

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

    date_start = fields.Datetime(
        'Start', required=True, tracking=True, default=fields.Date.today,
        help="Start Date Appointment")
    
    
    date_end = fields.Datetime(
        'End', required=True, tracking=True, default=lambda self: fields.Datetime.today() + timedelta(hours=0.5),
        compute='_compute_stop', readonly=False, store=True,
        help="End Date Appointment")