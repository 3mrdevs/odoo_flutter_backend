import json

from odoo import http
from odoo.http import request


class Api (http.Controller):

    @http.route(['/api/books'], type="http", auth="public", website=True, method=['POST'], csrf=False)
    def get_books(self):
        values = {}

        data = request.env['flutter.book'].sudo().search_read([],fields=[
            "name",
            "description",
            "state",
        ])

        if data:
            values['success'] = True
            values['data'] = data
        else:
            values['success'] = False
            values['error_code'] = 1
            values['error_data'] = 'No data found!'

        return json.dumps(values)