import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename="../output/test.log")   
def extract_data(file_path):
    try:
        logging.info(f"starting data extraction from {file_path}")
        data = pd.read_csv(file_path, encoding='latin-1')
        logging.info(f"Loaded {len(data)} rows")
        logging.info(f"Data extracted successfully from {file_path}")
        return data
    except Exception as e:
        logging.error(f"Error occurred while extracting data from {file_path}: {str(e)}")
        return None
def transform_data(data):
    try:
        logging.info("Starting data transformation")
        data = data.rename(columns={
        'Quantity': 'quantity',
        'UnitPrice': 'price',
        'CustomerID': 'customer_id',
        'InvoiceDate': 'order_date',
        'InvoiceNo': 'order_id'})
        required_cols = ['quantity', 'price', 'customer_id', 'order_date', 'order_id']
        missing = [col for col in required_cols if col not in data.columns]
        if missing:
            raise ValueError(f"Missing columns: {missing}")
        data = data.dropna(subset=['quantity', 'price', 'customer_id']).copy()
        data = data[(data['quantity']>0) & (data['price']>0)]
        data['order_date'] = pd.to_datetime(data['order_date'], errors='coerce')
        data = data.dropna(subset=['order_date'])
        data = data.drop_duplicates()
        data['linerevenue'] = data['quantity'] * data['price']
        data['total_revenue'] = data.groupby('order_id')['linerevenue'].transform('sum')
        data['Year'] = data['order_date'].dt.year
        data['Month'] = data['order_date'].dt.month
        logging.info("Data transformation completed successfully")
        logging.info(f"Rows after cleaning: {len(data)}")
        return data
    except Exception as e:
        logging.error(f"Error occurred while transforming data: {str(e)}")
        return None
def load_data(data, output_path):
    try:
        logging.info(f"Starting data loading to {output_path}")
        data.to_csv(output_path, index=False)
        logging.info(f"Data loaded successfully to {output_path}")
    except Exception as e:
        logging.error(f"Error occurred while loading data to {output_path}: {str(e)}")
def main():
    input_file = "../Data/ecommerce_data.csv"
    output_file = "../output/cleaned_data.csv"
    data = extract_data(input_file)
    if data is not None:
        data = transform_data(data)
        if data is not None:
            load_data(data, output_file)
            
if __name__ == "__main__":
    main()