# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Adreca(models.Model):

    _name = 'hospital.adreca'

    ciutat = fields.Char(string= 'Ciutat', required= False, size= 15)

    codiPostal = fields.Integer(string='Codi postal', required= False, size= 10)

    carrer = fields.Char(string= 'Carrer', required= False, size= 20)

    numero = fields.Integer(string= 'Número', required= False, size= 4)

    planta = fields.Char(string= 'Planta', required= True, size= 3)

    porta = fields.Char(string= 'Porta', required= False, size= 3)