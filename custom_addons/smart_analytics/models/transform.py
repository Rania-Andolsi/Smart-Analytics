def transform_sales_data(sales_data):
    transformed_data = []
    for record in sales_data:
        transformed_data.append({
            'report_name': record['report_name'],
            'total_sales': record['total_sales'] * 1.1,  # Exemple de transformation
            'date': record['date']
        })
    return transformed_data
