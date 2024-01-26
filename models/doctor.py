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

    image = fields.Binary(string="", attachment=True)

    status = fields.Selection(
    string='Status',
    selection=[('available', 'Available'), ('on_leave', 'On Leave')],
    default='available',
    required=True,
    )

    active = fields.Boolean(string='Active', compute='_compute_active', store=True)

    @api.onchange('status')
    def _onchange_status(self):
        for record in self:
            if record.status == 'on_leave':
                record.active = False
            else:
                record.active = True

    @api.depends('status')
    def _compute_active(self):
        for doctor in self:
            doctor.active = doctor.status != 'on_leave'

    def toggle_status(self):
        for doctor in self:
            if doctor.status == 'available':
                doctor.status = 'on_leave'
            else:
                doctor.status = 'available'
