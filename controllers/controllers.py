# -*- coding: utf-8 -*-
# from odoo import http


# class DentalCare(http.Controller):
#     @http.route('/dental_care/dental_care', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dental_care/dental_care/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dental_care.listing', {
#             'root': '/dental_care/dental_care',
#             'objects': http.request.env['dental_care.dental_care'].search([]),
#         })

#     @http.route('/dental_care/dental_care/objects/<model("dental_care.dental_care"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dental_care.object', {
#             'object': obj
#         })

