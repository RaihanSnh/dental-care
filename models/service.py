from odoo import api, fields, models

class Service(models.Model):
    _name = 'dental.care.service'
    _description = 'Data Service'

    name = fields.Char(string='Name')

    floor = fields.Integer(string='Floor')

    room = fields.Char(string='Room')    

    total_doctor = fields.Integer(
        string='Doctor Count',
        compute='_compute_total_doctor'
    )

    doctor_ids = fields.One2many(
        
        comodel_name='dental.care.doctor',
        inverse_name='service_id',
        string = 'Doctors'
    )

    @api.depends('doctor_ids')
    def _compute_total_doctor(self):
        doctor_group = self.env['dental.care.doctor'].read_group(domain=[], fields=['service_id'], groupby=['service_id'])
        
        for doctor in doctor_group:
            service_id = doctor.get('service_id')[0]
            service_rec = self.browse(service_id)
            service_rec.total_doctor = doctor['service_id_count']
            self -= service_rec
        self.total_doctor = 0
            
            
    def action_view_service(self):
        return {
            'name': ('Doctors'),
            'res_model': 'dental.care.doctor',
            'view_mode': 'list,form',
            'context': {'default_service_id' : self.id},
            'domain': [('service_id', '=', self.id)],
            'target': 'current',
            'type': 'ir.actions.act_window'
        }