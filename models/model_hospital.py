# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Hospital(models.Model):

    _name = 'hospital.hospital'

    nom = fields.Char(string= 'Nom hospital', required= False, size= 20)

    metge_ids = fields.One2many('hospital.metge', 'hospital_id', string='Metges')

    historial_ids = fields.One2many('hospital.historial', 'hospital_id', string='Historials')

    malaltia_ids = fields.One2many('hospital.malaltia', 'hospital_id', string='Malalties')

    pacient_ids = fields.One2many('hospital.pacient', 'hospital_id', string='Pacients')