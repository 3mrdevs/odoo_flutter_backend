from odoo import fields, models, api


class Books (models.Model):
    _name = 'flutter.book'
    _description = 'Model for storing books and do CRUD operations.'

    name = fields.Char()
    number = fields.Integer()


