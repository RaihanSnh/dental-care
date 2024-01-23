from odoo import api, fields, models

from datetime import timedelta

class Appointment(models.Model):
    _name = 'dental.care.appointment'
    _inherit = 'mail.thread'
    _description = 'Data Appointments'

    patient_id = fields.Many2one(
        string='Patient',
        comodel_name='res.partner',
        domain="[('is_patient', '=', True)]",
        required=True,
        track_visibility='onchange'
    )

    doctor_id = fields.Many2one(
        string='Doctor',
        comodel_name='res.partner',
        domain="[('is_doctor', '=', True)]",
        required=True,
        track_visibility='onchange'
    )

    service_id = fields.Many2one(
        string='Service',
        comodel_name='dental.care.service',
        ondelete='restrict',
        track_visibility='onchange'
    )

    date_start = fields.Datetime(
        'Start', required=True, tracking=True, default=fields.Date.today, track_visibility='onchange',
        help="Start Date Appointment")
    
    
    date_end = fields.Datetime(
        'End', required=True, tracking=True, default=lambda self: fields.Datetime.today() + timedelta(hours=0.5),
        compute='_compute_stop', readonly=False, store=True, track_visibility='onchange',
        help="End Date Appointment")
    
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('inprogress', 'InProgress'), ('done', 'Done'), ('cancel', 'Cancel')],
        readonly=True,
        default='new',
        required=True,
        track_visibility='onchange'
    )

    def action_inprogress(self):
        self.write({'state':'inprogress'})

    def action_done(self):
        self.write({'state':'done'})

    def action_cancel(self):
        self.write({'state':'cancel'})

    def action_reset(self):
        self.write({'state':'new'})

    def change_state(self, new_state):
        self.ensure_one()
        self.state = new_state

    def report_appointment(self):
        return self.env.ref("dental_care.action_report_dental_care").report_action(self)