import requests
from odoo import http
from odoo.http import request
from ..models.transform import transform_sales_data

class DataVisualizationController(http.Controller):
    @http.route('/data/visualization', type='json', auth='public')
    def get_visualization_data(self, start_date, end_date):
        sales_report_model = request.env['sales.report']
        sales_data = sales_report_model.get_sales_data_json(start_date, end_date)
        transformed_data = transform_sales_data(sales_data)
        success = self.send_to_powerbi(transformed_data)
        return {'status': 'success' if success else 'failed'}

    def send_to_powerbi(self, transformed_data):
        powerbi_url = 'https://api.powerbi.com/v1.0/myorg/groups/{group_id}/datasets/{dataset_id}/rows'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {access_token}'
        }
        response = requests.post(powerbi_url, headers=headers, json=transformed_data)
        return response.status_code == 200
