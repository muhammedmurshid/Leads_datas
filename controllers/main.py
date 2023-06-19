from odoo import http
from odoo.http import request


class MyController(http.Controller):
    @http.route('/my_route', type='http', auth='public', methods=['POST'])
    def handle_post_request(self, **post):
        # Access the POST data
        field_value = post.get('field_name')

        # Process the data as needed
        # ...

        # Return a response if necessary
        return 'Success'
