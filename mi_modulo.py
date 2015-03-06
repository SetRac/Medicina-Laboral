# -*- coding: utf-8 -*-
from osv import fields, osv
from random import randint, random
from datetime import datetime
import urllib

class mi_modulo_mi_tabla(osv.osv):
    _name = "mi_modulo.mi_tabla"
    _order= 'name'
    _columns = {
        'name': fields.many2one('res.partner', required=True, help='Datos del paciente', select=1, string="Paciente"),
        'active': fields.boolean('Activo'),
        'quantity': fields.integer('cantidad'),
	'forma': fields.char('Componente',size=64 ,  help='Forma Almacenatmiento'),
        'date': fields.date('fecha'),
        'datetime': fields.datetime('fecha y hora'),
        'description': fields.text('descripcion'),
        'price': fields.float('precio', digits = (10,4)),
        'tabla_relacionada_id': fields.many2one('mi_modulo.mi_tabla_relacionada', 'Tabla Relacionada', domain="[('state','=','active')]", ondelete='set null'),
        'partner_ids': fields.many2many('res.partner', 'mi_modulo_partner_rel', 'mi_tabla_id', 'partner_id', 'Proveedores'),
        'state': fields.selection([('draft','borrador'),('active','Activo'),('cancelled','Cancelado')], 'estado', required=True),
                #Datos del Paciente

        'empresa': fields.many2one('res.partner', required=True, size=100 ,  help='Nombre de la Empresa de donde Viene', string='Empresa'),
        'nombres': fields.char('Nombres y Apellidos',size=128 ,  help='Nombres y Apellidos'),
        'cedula': fields.char('C.I.',size=10 ,  help='Cedula de Identidad'),
        'edad': fields.integer('Edad',size=2,  help='Edad del Paciente'),
        'edocivil': fields.selection([('Casado(a)','Casado(a)'),('Soltero(a)','Soltero(a)')],'Estado Civil', help='Edad del Paciente'),
        'direccion': fields.char('Direccion',size=150 ,  help='Direccion del Paciente'),
        'telefono': fields.char('Telefono',size=30 ,  help='Telefono del Paciente'),
        'celular': fields.char('Celular',size=30 ,  help='Celular del Paciente'),
        'aspiracargo': fields.char('Aspirante al Cargo',size=64 ,  help='Aspirante al Cargo'),
        'ocupacargo': fields.char('Cargo que ocupa',size=64 ,  help='Cargo que Ocupa'),
        'fechaegreso': fields.date('Fecha de Ingreso',  help='Fecha de egreso'),
        'fechadia': fields.date('Fecha',  help='Fecha del Dia'),

        #Antecedentes familiares
        'papavive': fields.selection([('si','si'),('no','no')],'Padre Vive',  help='El Padre Vive?'),
        'mamavive': fields.selection([('si','si'),('no','no')],'Madre Vive',  help='La madre Vive?'),
        'papacondicion': fields.char('Condicion Padre',size=64 ,  help='Condicion Padre'),
        'mamacondicion': fields.char('Condicion Madre', digits=64 ,  help='Condicion Madre'),
        'nrohermanos': fields.integer('Nro Hermanos total',  help='Nro Hermanos'),
        'nrohermanosvarones': fields.integer('Nro Hermanos',  help='Nro Hermanos hombres'),

        'nrohermanoshembras': fields.integer('Nro Hermanas',  help='Nro Hermanas'),
        'hermanoscondicion': fields.char('Condicion Hermanos',size=64 ,  help='Condicion Hermanos'),

        'nrohijos': fields.integer('Nro Hijos Total' ,  help='Nro Hijos Total'),
        'nrohijosvarones': fields.integer('Nro Hijos' ,  help='Nro Hijos'),
        'nrohijoshembras': fields.integer('Nro Hijas' ,  help='Nro Hijas'),
        'hijoscondicion': fields.char('Condicon Hijos',size=64 ,  help='Condicion Hijos'),
        #Antecedentes Medicos
        'eci': fields.selection([('si','si'),('no','no')], 'ECI',  help='ECI elija si o no'),
        'lechina': fields.selection([('si','si'),('no','no')], 'Lechina',  help='Elija si o no'),
        'sarampion': fields.selection([('si','si'),('no','no')],'sarampion',  help='Elija si o no'),
        'paperas': fields.selection([('si','si'),('no','no')],'Paperas',  help='Elija si o no'),
        'rubiola': fields.selection([('si','si'),('no','no')],'Rubiola',  help='Elija si o no'),
        'mujeresotros': fields.char('OTROs',size=64 ,  help='Otras enfermedades'),
        'otras': fields.char('OTRAS',size=64 ,  help='Otras enfermedades'),
        'dengue': fields.selection([('si','si'),('no','no')],'Dengue',  help='Elija si o no'),
        'mononucleosis': fields.selection([('si','si'),('no','no')],'Mononucleosis',  help='Elija si o no'),
        'hepatitis': fields.selection([('si','si'),('no','no')],'Hepatitis',  help='Elija si o no'),
        'inmunizaciones': fields.char('inmunizaciones',size=64 ,  help='Elija si o no'),
        'quirurgicos': fields.selection([('si','si'),('no','no')],'Quirurgicos',  help='Elija si o no'),
        'quirurgicoscual': fields.char('Decriba Cual',size=64 ,  help='Describa cual'),
        #Antecedentes Medicos Alergias
        'alimentos': fields.char('Alimentos',size=64 ,  help='Alergia a alimentos'),
        'oloresfuertes': fields.char('Olores Fuertes',size=64 ,  help='Alergia a Olores Fuertes'),
        'polvos': fields.char('Polvos',size=64 ,  help='Alergias a Polvos'),
        
                #Uso de  Medicamentos

        'medicamentos': fields.selection([('si','si'),('no','no')], 'Medicamentos',  help='Toma Algun Medicamento'),
        'medicamentoscuales': fields.char('Cual Medicamento',size=64 ,  help='Describa Cuales Medicamentos'),
        'gastricos': fields.char('Gastricos',size=64 ,  help='Medicamentos Gastricos'),
        'respiratorios': fields.char('Respiratorios',size=64 ,  help='Medicamentos Respiratorios'),
        'cardiovasculares': fields.char('Cardiovasculares',size=64 ,  help='Medicamentos Cardiovascular'),
        'neurologicos': fields.char('Neurologicos',size=64 ,  help='Medicamentos Neurologicos'),
        'osteomuscular': fields.char('Osteomuscular',size=64 ,  help='Medicamentos Osteomuscular'),
        'orl': fields.char('ORL',size=64 ,  help='Medicamentos ORL'),
        'urinarios': fields.char('Urinarios',size=64 ,  help='Medicamentos Urinarios'),
        'endocrinos': fields.char('Endocrinos',size=64 ,  help='Medicamentos Endocrinos'),
        'psicosocial': fields.char('Psicosocial',size=64 ,  help='Medicamentos Psicosocial'),
                        #Solo  para mujeres
                        
        'menarquia': fields.char('Menarquia',size=64 ,  help='Menarquia'),
        'fur': fields.char('FUR',size=64 ,  help='FUR'),
        'disminorrea': fields.char('Disminorrea',size=64 ,  help='Disminorrea'),
        'mujeresotros': fields.char('OTROs',size=64 ,  help='Otras enfermedades'),
        'gestas': fields.char('Gestas',size=64 ,  help='Gestas'),
        'para': fields.char('Para',size=64 ,  help='Para'),
        'cesarea': fields.char('Cesarea',size=64 ,  help='Cesarea'),
        'abortos': fields.char('Abortos',size=64 ,  help='Abortos'),
        'ultimacitologia': fields.char('Ultima Citologia',size=64 ,  help='Ultima Citologia'),
        'patologia': fields.char('Patologia',size=64 ,  help='Patologia'),
        'secrecionotumaroacionsiono': fields.selection([('si','si'),('no','no')],'secresion tumoracion',  help='Secrecion o Tumoracion?'),
        
        #Antecedentes Laborales
        'empresaantigua': fields.many2one('res.partner', required=True,size=64 ,  help='Empresa donde trabajo anteriormente', string='Empresa Anterior'),
        'cargo': fields.char('Cargo que Ocupo',size=64 ,  help='Cargo que Ocupo'),
        'tiempoenempresa': fields.char('Tiempo en la Empresa',size=64 ,  help='Tiempo en la Empresa en Meses'),
        'implementosdeseguridad': fields.char('Implementos de Seguridad',size=64 ,  help='Utilizaba Implementos de Seguridad'),
        
        #Antecedentes Habitos
        'actividadfisica': fields.char('Actividad Fisica',size=64 ,  help='Actividad Fisica'),
        'tabaco': fields.selection([('si','si'),('no','no')],'Tabaco',  help='TABACO'),
        'alcohol': fields.selection([('si','si'),('no','no')],'Alcohol',  help='Alcohol'),
        'cafe': fields.selection([('si','si'),('no','no')],'Cafe',  help='Cafe'),
        'micciones': fields.selection([('si','si'),('no','no')],'Micciones',  help='Micciones'),
        'intestinales': fields.selection([('si','si'),('no','no')],'Intestinales',  help='Intestinales'),
        'otroshabitos': fields.char('Otros Habitos',size=64 ,  help=' Otros Habitos'),
        
         #Sintomas
        'dolordecabeza': fields.selection([('si','si'),('no','no')],'Dolor de Cabeza',  help='Dolor de Cabeza'),
        'dificultadparaver': fields.selection([('si','si'),('no','no')],'Dificultad para ver',  help='Dificultad para ver'),
        'usodelentes': fields.selection([('si','si'),('no','no')],'Usa Lentes',  help='Usa Lentes'),
        'escuchar': fields.selection([('si','si'),('no','no')],'Dificultad para Escuchar',  help='Dificultad para Escuchar'),
        'asma': fields.selection([('si','si'),('no','no')],'Asma',  help='Asma'),
        'cansancio': fields.selection([('si','si'),('no','no')],'Cansancio',  help='Cansancio'),
        'opresion': fields.selection([('si','si'),('no','no')],'Opresion',  help='Opresion'),
        'hipertension': fields.selection([('si','si'),('no','no')],'Hipertension',  help='Hipertension'),
        'diarrea': fields.selection([('si','si'),('no','no')],'Diarrea',  help='Diarrea'),
        'problemasorinar': fields.selection([('si','si'),('no','no')],'Prob. Orinar',  help='Problemas para orinar'),
        'lesiongenital': fields.selection([('si','si'),('no','no')],'Lesion Genital',  help='Lesion Genital'),
        'enfermedadsexual': fields.selection([('si','si'),('no','no')],'Enfermedad Sexual',  help='Enfermedad Sexual'),
        'insomnio': fields.selection([('si','si'),('no','no')],'Insomnio',  help='Insomnio'),
        'cambiodepeso': fields.selection([('si','si'),('no','no')],'Cambio de Peso',  help='Cambio de Peso'),
        'dolordeespalda': fields.selection([('si','si'),('no','no')],'Dolor de Espalda',  help='Dolor de Espalda'),
        'fracturas': fields.selection([('si','si'),('no','no')],'Fracturas',  help='Fracturas'),
        'lesionespiel': fields.selection([('si','si'),('no','no')],'Lesion Piel',  help='Lesion Piel'),
        'trabajaporturnos': fields.selection([('si','si'),('no','no')],'Trabajo por Turnos',  help='Trabajo por Turnos'),
        'usaequiposproteccion': fields.selection([('si','si'),('no','no')],'Equipos de Proteccion',  help='Usa Equipos de Proteccion'),
        'accidentelaboral': fields.selection([('si','si'),('no','no')],'Accidente Laboral',  help='Ha sufrido Algun Accidente Laboral'),
        
        #Examen Fisico
        'peso': fields.float('Peso', digits=(3,2),  help='Peso del Paciente'),
        'talla': fields.float('Talla', digits=(3,2),  help='Talla del Paciente'),
        'fc': fields.float('FC', digits=(3,2),  help='Frecuencia Cardiaca del Paciente'),
        'pulso': fields.float('Pulso', digits=(3,2),  help='Pulso del Paciente'),
        'fr': fields.float('FR', digits=(3,2),  help='FR del Paciente'),
        'ta': fields.float('TA', digits=(3,2),  help='TA del Paciente'),
        'piel': fields.char('Piel',size=4 ,  help='Piel'),
        'cabezacuello': fields.char('Cabeza Cuello',size=4 ,  help='Cabeza Cuello'),
        'orl': fields.char('ORL',size=4 ,  help='ORL'),
        'visioncercana': fields.selection([('si','si'),('no','no')],'Vision Cercana', help='Forma Almacenatmiento'),
        'visionlejana': fields.selection([('si','si'),('no','no')],'Vision Lejana',  help='Forma Almacenatmiento'),
        'visiondecolore': fields.selection([('si','si'),('no','no')],'Vision de Color',  help='Forma Almacenatmiento'),
        'visionborro': fields.selection([('si','si'),('no','no')],'Vision Borrosa',  help='Forma Almacenatmiento'),
        'visionusalentes': fields.selection([('si','si'),('no','no')],'Usa Lentes',  help='Forma Almacenatmiento'),
        'torax': fields.char('Torax',size=64 ,  help='Forma Almacenatmiento'),
        'toraxsimetrico': fields.char('Torax Simetrico',size=64 ,  help='Forma Almacenatmiento'),
        'abdomen': fields.char('Abdomen',size=64 ,  help='Forma Almacenatmiento'),
        'herniasumbilicares': fields.selection([('si','si'),('no','no')],'Hernias Umbilicares', help='Forma Almacenatmiento'),
        'herniasinguinoescrotales': fields.selection([('si','si'),('no','no')],'Hernias Quinoescrotales', help='Forma Almacenatmiento'),
	'columnacervical': fields.char('Columna Vertical',size=64 ,  help='Forma Almacenatmiento'),
        'columnatoraxica': fields.char('Columna Toraxica',size=64 ,  help='Forma Almacenatmiento'),
        'columnalumbosacra': fields.char('Columna Lumbosacra',size=64 ,  help='Forma Almacenatmiento'),
        'miembrossuperiores': fields.char('Miembros Sueriores',size=64 ,  help='Forma Almacenatmiento'),
        'miembrosinferiores': fields.char('Miembros Inferiores',size=64 ,  help='Forma Almacenatmiento'),
        'neurologicos': fields.char('Neurologicos',size=4 ,  help='Forma Almacenatmiento'),

#Exame compleentario
        'hematologia': fields.char('Hematologia',size=25 ,  help='Forma Almacenatmiento'),
        'exudadofaringeo': fields.char('Exudado Faringeo',size=12 ,  help='Forma Almacenatmiento'),
        'glisemia': fields.char('Glisemia',size=15 ,  help='Forma Almacenatmiento'),
        'acidourico': fields.char('Acido Urico',size=20 ,  help='Forma Almacenatmiento'),
        'colesterol': fields.char('Colesterol',size=10 ,  help='Forma Almacenatmiento'),
        'orina': fields.char('Orina',size=8 ,  help='Forma Almacenatmiento'),
        'hdl': fields.char('HDL',size=4 ,  help='Forma Almacenatmiento'),
        'especiales': fields.char('Especiales',size=4 ,  help='Forma Almacenatmiento'),
        'ldl': fields.char('LDL',size=4 ,  help='Forma Almacenatmiento'),
        'rnmcolumnalumbosacra': fields.char('rnmcolumnalumbosacra',size=4 ,  help='Forma Almacenatmiento'),
        'trigliceridos': fields.char('Trigliceridos',size=4 ,  help='Forma Almacenatmiento'),
        'audiometria': fields.char('Audiometria',size=4 ,  help='Forma Almacenatmiento'),
        'heces': fields.char('Heces',size=4 ,  help='Forma Almacenatmiento'),
        'espirometria': fields.char('Espirometria',size=4 ,  help='Forma Almacenatmiento'),
        'vdrl': fields.char('VDRL',size=4 ,  help='Forma Almacenatmiento'),
        'hiv': fields.char('HIV',size=4 ,  help='Forma Almacenatmiento'),

#Diagnostico
        'elegible': fields.char('elegible',size=25 ,  help='Forma Almacenatmiento'),
        'elegibleconlimitaciones': fields.char('elegibleconlimitaciones',size=12 ,  help='Forma Almacenatmiento'),
        'noelegible': fields.char('noelegible',size=15 ,  help='Forma Almacenatmiento'),
        'sugerencias': fields.char('sugerencias',size=20 ,  help='Forma Almacenatmiento'),
        'idx': fields.text('idx',  help='Forma Almacenatmiento'),
        
        #
        #prevacacional
        #Edo General
        'resultadosexamencomplementario': fields.text('Resultados Examen Complementario',  help='Resultados Examen Complementario'),
        'peso2': fields.char('Peso',size=25 ,  help='Peso Pre-Vacacional'),
        'talla2': fields.char('Talla',size=12 ,  help='Talla Pre-Vacacional'),
        'ta2': fields.char('T.A.',size=15 ,  help='T.A.  Pre-Vacacional'),
        'fr2': fields.char('FR',size=12 ,  help='FR Pre-Vacacional'),
        'fc2': fields.char('FC',size=15 ,  help='FC Pre-Vacacional'),
        'condicionantesde': fields.selection([('Buenas Condiciones','Buenas Condiciones'),('Regulares Condiciones','Regulares Condiciones'),('Malas Condiciones','Malas Condiciones')],'Condiciones Fisicas', help='Condiciones antes de las vaciones del Paciente'),
#El traajador cumplio con
        #El traajador debe cumplir con
#sus actuales condiciones de salud hacen  necesario

        #
        #postvacacional
        
        #
        #Postempleo
        







        
    }


    def _check_date(self, cr, uid, ids, context = None):
        is_valid_data = True
        present = datetime.now()
        for obj in self.browse(cr,uid,ids,context=None):
            if not obj.date or not obj.datetime:
                continue

            date = datetime.strptime(obj.date, '%Y-%m-%d')
            date_time = datetime.strptime(obj.datetime, '%Y-%m-%d %H:%M:%S')
            if(date < present or date_time < present):
                is_valid_data = False

        return is_valid_data

    _constraints = [
        (_check_date,'Fecha debe ser en el futuro',['date','datetime']),
    ]

    def _random_quantity(self, cr, uid, context = None):
        return randint(5,100)

    _defaults = {
         'active': True,
         'state': 'draft',
         'price': lambda *a: random(),
         'quantity': _random_quantity,
    }

    def onchange_active(self, cr, uid, ids, active):
        if not active:
            return {'value': {'state': 'cancelled'} }
        return {
            'warning': {'message': 'Cambiando el estado a "activo"'},
            'value': {'state': 'active'},
        }

    def next_monday_date(self, cr, uid, ids, context=None):
        url = "http://www.timeapi.org/pdt/next+monday?\Y-\m-\d"
        next_monday_date = urllib.urlopen(url).read()
        self.write(cr, uid, ids, {'date': next_monday_date})

mi_modulo_mi_tabla()


class mi_modulo_mi_tabla_relacionada(osv.osv):
    _name = "mi_modulo.mi_tabla_relacionada"
    _columns = {
        'name': fields.many2one('res.partner', required=True, help='Datos del paciente', select=1, string="Paciente"),
        'active': fields.boolean('activo'),
        'state': fields.selection([('draft','borrador'),('active','Activo'),('cancelled','Cancelado')], 'estado', required=True),
        'related': fields.one2many('mi_modulo.mi_tabla', 'tabla_relacionada_id', 'Objetos relacionados'),
    }
    _defaults = {
         'active': True,
         'state': 'draft',
    }

mi_modulo_mi_tabla_relacionada()

class res_partner(osv.osv):
    _name = "res.partner"
    _inherit = "res.partner"

    _columns = {
        'mi_tabla_ids': fields.many2many('mi_modulo.mi_tabla', 'mi_modulo_partner_rel', 'partner_id', 'mi_tabla_id', 'Historia Medica Del Paciente'),
        'cedula': fields.char('C.I.',size=10 ,  help='Cedula de Identidad'),
        'edad': fields.integer('Edad',size=2,  help='Edad del Paciente'),
        'edocivil': fields.selection([('Casado(a)','Casado(a)'),('Soltero(a)','Soltero(a)')],'Estado Civil', help='Edad del Paciente'),

    }
res_partner()

