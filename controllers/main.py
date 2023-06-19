from odoo import http
from odoo.http import request


class LeadsDatas(http.Controller):
    @http.route('/voxbayconnector', type='http', auth='public', methods=['POST'])
    def handle_post_request(self, **post):
        # Access the POST data
        called_number = post.get('called_number')
        caller_number = post.get('caller_number')
        call_u_uid = post.get('call_u_uid')
        agent_number = post.get('agent_number')
        total_call_duration = post.get('total_call_duration')
        call_date = post.get('call_date')
        call_status = post.get('call_status')
        recording_url = post.get('recording_url')
        call_start_time = post.get('call_start_time')
        call_end_time = post.get('call_end_time')
        conversation_duration = post.get('conversation_duration')
        dtmf = post.get('dtmf')
        extension = post.get('extension')
        destination = post.get('destination')
        date = post.get('date')
        duration = post.get('duration')
        transferred_number = post.get('transferred_number')

        # Process the data as needed
        # ...

        # Return a response if necessary
        return 'Success'
