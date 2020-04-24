# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Historial(models.Model):

    _name = 'hospital.historial'

    codi = fields.Integer(string= 'Codi historial', required= False, size= 30)


    # MANY TO ONE
    hospital_id = fields.Many2one('hospital.hospital', ondelete= 'cascade', string='Hospital', required=True)


    # ONE TO MANY
    visita_ids = fields.One2many('hospital.visita', 'historial_id', string='Visites')


    # ONE TO ONE: PACIENT
    pacient_id = fields.Many2one('hospital.pacient', ondelete='cascade', string='Pacient')