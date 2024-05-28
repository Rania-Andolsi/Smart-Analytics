from odoo import models, fields, api

class SalesReport(models.Model):
    _name = 'sales.report'
    _description = 'Sales Report'

    name = fields.Char(string='Report Name')
    total_sales = fields.Float(string='Total Sales')
    date = fields.Date(string='Date')

    @api.model
    def get_sales_data(self, start_date, end_date):
        records = self.search([('date', '>=', start_date), ('date', '<=', end_date)])
        return records

    @api.model
    def get_sales_data_json(self, start_date, end_date):
        records = self.get_sales_data(start_date, end_date)
        data = []
        for record in records:
            data.append({
                'report_name': record.name,
                'total_sales': record.total_sales,
                'date': record.date.isoformat()
            })
        return data
