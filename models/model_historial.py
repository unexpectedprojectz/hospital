# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Historial(models.Model):

    _name = 'hospital.historial'

    codi = fields.Integer(string= 'Codi historial', required= False, size= 30)

    hospital_id = fields.Many2one('hospital.hospital', ondelete= 'cascade', string='Hospital', required=True)

    visita_ids = fields.One2many('hospital.visita', 'historial_id', string='Visites')