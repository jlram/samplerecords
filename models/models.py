# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Album(models.Model):
    _name = 'samplerecords.album'
   
    name = fields.Char(string="Titulo", required=True)
    
    amount = fields.Integer(string="Cantidad")
    
    worker_id = fields.Many2one('samplerecords.worker',ondelete='cascade', string="Mezclado por", required=True)

    band_id = fields.Many2one('samplerecords.band',ondelete='cascade', string="Artista", required=True)

    description = fields.Text(string="Descripción")


class Worker(models.Model):
	_name = 'samplerecords.worker'

	name = fields.Char(string="Nombre", required=True)

	edad = fields.Integer(string="Edad")

	album_ids = fields.One2many('samplerecords.album', 'worker_id', string="Album(es)")

	description = fields.Text(string="Descripción")


class Band(models.Model):
	_name = 'samplerecords.band'

	name = fields.Char(string="Nombre", required=True)

	miembros = fields.Integer(string="Número de Miembros")

	album_ids = fields.One2many('samplerecords.album', 'band_id', string="Album(es)")

	description = fields.Text(string="Descripción")