import json

from odoo import http
from odoo.http import request


class Api (http.Controller):

    @http.route(['/api/books'], type="http", auth="public", website=True, method=['POST'], csrf=False)
    def get_books(self):

        data = request.env['flutter.book'].sudo().search_read([])
