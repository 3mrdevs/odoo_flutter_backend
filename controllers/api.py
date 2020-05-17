import json

from odoo import http
from odoo.http import request


class Api (http.Controller):

    @http.route(['/api/books'], type="http", auth="public", website=True, method=['POST'], csrf=False)
    def get_books(self):
        values = {}

        data = request.env['flutter.book'].sudo().search([])

        if data:
            books = []
            for book_data in data:
                book = {
                    "name": str(book_data.name),
                    "description": book_data.description,
                    "state": book_data.state,
                    "publish_date": str(book_data.publish_date),
                    "language": book_data.language,
                    "isbn": book_data.isbn,
                    "price": book_data.price,
                    "author": book_data.author.name,
                    "publisher": book_data.publisher.name,
                }
                categories = []
                for category in book_data.categories:
                    categories.append(category.name)
                book["categories"] = categories
                books.append(book)

            values['success'] = True
            values['data'] = books
        else:
            values['success'] = False
            values['error_code'] = 1
            values['error_data'] = 'No data found!'

        return json.dumps(values)