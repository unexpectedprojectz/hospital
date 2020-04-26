# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Adreca(models.Model):

    _name = 'hospital.adreca'
    _rec_name = 'carrer'

    ciutat = fields.Char(string= 'Ciutat', required= False, size= 15)

    codiPostal = fields.Integer(string='Codi postal', required= False, size= 10)

    carrer = fields.Char(string= 'Carrer', required= True, size= 20)

    numero = fields.Integer(string= 'Número', required= False, size= 4)

    planta = fields.Char(string= 'Planta', required= False, size= 3)

    porta = fields.Char(string= 'Porta', required= False, size= 3)


    # ONE TO ONE: HOSPITAL
    hospital_id = fields.Many2one('hospital.hospital', ondelete='cascade', string='Hospital')


    # ONE TO ONE: METGE
    metge_id = fields.Many2one('hospital.metge', ondelete='cascade', string='Metge')


    # ONE TO ONE: PACIENT
    pacient_id = fields.Many2one('hospital.pacient', ondelete='cascade', string='Pacient')