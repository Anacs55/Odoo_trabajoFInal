# -*- coding: utf-8 -*-
# from odoo import http


# class Ernon2(http.Controller):
#     @http.route('/ernon2/ernon2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ernon2/ernon2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ernon2.listing', {
#             'root': '/ernon2/ernon2',
#             'objects': http.request.env['ernon2.ernon2'].search([]),
#         })

#     @http.route('/ernon2/ernon2/objects/<model("ernon2.ernon2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ernon2.object', {
#             'object': obj
#         })
