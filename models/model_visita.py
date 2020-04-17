# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Visita(models.Model):

    _name = 'hospital.visita'

    data = fields.Date(string= 'Data', required= False, size= 30)

    historial_id = fields.Many2one('hospital.hospital', ondelete='cascade', string='Hospital', required=True)