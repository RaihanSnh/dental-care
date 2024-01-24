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
        default='new',
        required=True,
        track_visibility='onchange'
    )

    color_class = fields.Char(compute='_compute_color_class')

    @api.depends('state')
    def _compute_color_class(self):
        color_dict = {
            'new': '#17a2b8',  # warna biru/info dalam format HEX
            'inprogress': '#ffc107',  # warna kuning/warning dalam format HEX
            'done': '#28a745',  # warna hijau/success dalam format HEX
            'cancel': '#dc3545',  # warna merah/danger dalam format HEX
        }
        for record in self:
            record.color_class = color_dict.get(record.state, '#17a2b8')

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

    def get_records(self):
        # Return a recordset
        return self.search([])

    def report_appointment(self):
        return self.env.ref("dental_care.action_report_dental_care").report_action(self)