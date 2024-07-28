import csv

def parse_specification(spec_file):
    with open(spec_file, 'r') as f:
        spec = f.readlines()
    
    field_names = []
    field_lengths = []
    
    for item in spec:
        parts = item.split()
        if len(parts) < 2:
            print(f"Skipping invalid specification line: {item}")
            continue

        field_names.append(parts[0])
        try:
            field_lengths.append(int(parts[1]))
        except ValueError:
            print(f"Invalid length value in specification line: {item}")
            continue
    
    return field_names, field_lengths

def parse_fixed_width_file(input_file, field_lengths, delimiter=","):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    parsed_data = []
    for line in lines:
        parsed_line = []
        start = 0
        for length in field_lengths:
            parsed_line.append(line[start:start+length].strip())
            start += length
        parsed_data.append(delimiter.join(parsed_line))
    
    return parsed_data

def write_to_csv(parsed_data, output_file, field_names):
    with open(output_file, 'w') as f:
        f.write(",".join(field_names) + "\n")
        for line in parsed_data:
            f.write(line + "\n")
