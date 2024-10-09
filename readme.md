# Zipboard Tests

## Framework used: Selenium

### Reasons

- **Cross-browser Compatibility**: Supports a wide range of browsers, making it ideal for comprehensive testing.
- **Mature and Reliable**: A well-established tool with extensive community support, plugins, and documentation for resolving issues.
- **Scalability**: Selenium Grid enables parallel testing across multiple environments, improving test efficiency.

## Design Pattern used: Page Object Model (POM) pattern

### Reasons

- Enhanced Code Reusability.
- Improved Readability.
- Easier Maintenance.
- Scalability.
- Reduced Duplication.
- Better Abstraction.

## Tests Setup

- Download [Python](https://www.python.org/downloads/) for your operating system.
- Clone the repository from GitHub:
```commandline
git clone https://github.com/Awaish-prog/zipboard-assignment.git
```
- Navigate into the directory
```commandline
cd zipboard-assignment
```
- Create python virtual environment
```commandline
python -m venv venv
```
- Activate the virtual environment:
    - For windows:
    ```commandline
    venv\Scripts\activate
    ```
    - For windows(if above command gives error):
    ```commandline
    venv\Scripts\activate.bat
    ```
    - On macOS/Linux:
    ```commandline
    source venv/bin/activate
    ```
- Install project dependencies:
```commandline
pip install -r requirements.txt
```

- Run below command to start tests for login page(recommended to test a particular section in the testnet):
```commandline
pytest --log-cli-level=INFO test_annotations_markups.py
```

- Deactivate virtual environment:
```commandline
deactivate
```