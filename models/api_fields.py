from odoo import fields, models, _


class ApiFields(models.Model):
    _name = 'api.chat'

    called_number = fields.Char(string='Called Number')
    caller_number = fields.Char(string='Caller Number')
    call_u_uid = fields.Char(string='CallUUid')
    agent_number = fields.Char(string='Agent Number')
    total_call_duration = fields.Integer(string='Total Call Duration')
    call_date = fields.Datetime(string='Call Date')
    call_status = fields.Char(string='Call Status')
    recording_url = fields.Char(string='Recording URL')
    call_start_time = fields.Datetime(string='Call Start Time')
    call_end_time = fields.Datetime(string='Call End Time')
    conversation_duration = fields.Integer(string='Conversation Duration')
    dtmf = fields.Integer(string='Dtmf')
    extension = fields.Char(string='Extension')
    destination = fields.Char(string='Destination')
    date = fields.Date(string='Date')
    duration = fields.Integer(string='Duration')
    transferred_number = fields.Char(string='Transferred Number')
