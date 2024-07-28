# CSV Anonymizer and Fixed Width File Parser

## Project Overview
This project addresses two data engineering problems:

1. **Fixed Width File Parser**: Parses a fixed width file using a given specification and generates a CSV file.
2. **Data Anonymizer**: Anonymizes specific columns in a CSV file.

## Setup and Execution

### Prerequisites
- Docker installed on your system.
- Python 3 installed on your system (for local development and testing).

### Steps to Run the Project

#### Using Docker

1. **Build the Docker Image**:
    ```sh
    docker build -t csv-anonymizer .
    ```

2. **Run the Fixed Width File Parser**:
    ```sh
    docker run -it --rm csv-anonymizer
    ```

3. **Run the Data Anonymizer**:
    - First, ensure the parsed CSV (`sample_output.csv`) is generated.
    - Modify the Dockerfile CMD to run the anonymizer:
        ```dockerfile
        CMD ["python", "data_processing/run_anonymizer.py"]
        ```
    - Rebuild and run the Docker image:
        ```sh
        docker build -t csv-anonymizer .
        docker run -it --rm csv-anonymizer
        ```

#### Local Development

1. **Create a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements-docker.txt
    ```

3. **Run the Fixed Width File Parser**:
    ```sh
    python fixed_width_parser/run_parser.py
    ```

4. **Run the Data Anonymizer**:
    ```sh
    python data_processing/run_anonymizer.py
    ```

## Example Files

- `specs.txt`: Contains the field names and their lengths.
- `sample_data.txt`: Contains the fixed width data to be parsed.
- `sample_output.csv`: The generated CSV file from the fixed width parser.
- `anonymized_output.csv`: The CSV file with anonymized data.

## Notes
- Ensure the `specs.txt` and `sample_data.txt` are correctly formatted and placed in the project directory.
- Modify the paths in the scripts as necessary to match your directory structure.
