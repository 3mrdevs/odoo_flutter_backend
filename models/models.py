from odoo import fields, models, api


class Books (models.Model):
    _name = 'flutter.book'
    _description = 'Model for storing books and do CRUD operations.'

    name = fields.Char()
    number = fields.Integer()
    description = fields.Text()
    image = fields.Binary()
    publish_date = fields.Date()
    language = fields.Selection([
        ('ar','Arabic'),
        ('en','english')
    ],default='en')


