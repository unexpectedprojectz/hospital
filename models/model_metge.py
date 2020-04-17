# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Metge(models.Model):

    _name = 'hospital.metge'

    _inherit = 'hospital.persona'

    numEmpleat = fields.Integer(string= 'Núm. empleat', required= False, size= 3)

    salariMensual = fields.Integer(string= 'Salari mensual', required= False, size= 5)

    codiCompteCorrent = fields.Char(string= 'Codi compte corrent', required= False, size= 20)

    hospital_id = fields.Many2one('hospital.hospital', ondelete= cascade, string='Hospital', required=True)