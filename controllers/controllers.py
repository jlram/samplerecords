# -*- coding: utf-8 -*-
from odoo import http

# class Samplerecords(http.Controller):
#     @http.route('/samplerecords/samplerecords/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/samplerecords/samplerecords/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('samplerecords.listing', {
#             'root': '/samplerecords/samplerecords',
#             'objects': http.request.env['samplerecords.samplerecords'].search([]),
#         })

#     @http.route('/samplerecords/samplerecords/objects/<model("samplerecords.samplerecords"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('samplerecords.object', {
#             'object': obj
#         })