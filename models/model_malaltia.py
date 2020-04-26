# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Malaltia(models.Model):

    _name = 'hospital.malaltia'

    codi = fields.Integer(string= 'Codi malaltia', required= True, size= 15)

    nom = fields.Char(string= 'Nom', required= False, size= 20)

    causaBaixa = fields.Boolean(string= 'Causa baixa', required=False)

    tractament = fields.Char(string= 'Tractament', required=False, size= 20)

    duradaTractament = fields.Char(string= 'Durada tractament', required= True, size= 4)


    # MANY TO ONE
    hospital_id = fields.Many2one('hospital.hospital', ondelete='cascade', string='Hospital', required=True)


    # ONE TO ONE: VISITA
    visita_id = fields.Many2one('hospital.visita', ondelete='cascade', string='Visita')