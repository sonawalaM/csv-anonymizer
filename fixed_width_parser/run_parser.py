import os
from parser import parse_specification, parse_fixed_width_file, write_to_csv

# Specify paths
base_dir = os.path.dirname(os.path.dirname(__file__))
spec_file = os.path.join(base_dir, 'specs.txt')
input_file = os.path.join(base_dir, 'sample_data.txt')
output_file = os.path.join(base_dir, 'sample_output.csv')

# Parse the specification
field_names, field_lengths = parse_specification(spec_file)

# Parse the fixed width file
parsed_data = parse_fixed_width_file(input_file, field_lengths)

# Write the parsed data to CSV
write_to_csv(parsed_data, output_file, field_names)
