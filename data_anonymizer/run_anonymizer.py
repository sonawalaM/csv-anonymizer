import os
from anonymizer import anonymize_csv

# Specify paths
base_dir = os.path.dirname(os.path.dirname(__file__))
input_file = os.path.join(base_dir, 'sample_output.csv')
output_file = os.path.join(base_dir, 'anonymized_output.csv')

# Columns to anonymize
columns_to_anonymize = ['first_name', 'last_name', 'address']

# Anonymize the CSV
anonymize_csv(input_file, output_file, columns_to_anonymize)
