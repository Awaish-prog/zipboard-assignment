# Zipboard Tests Setup

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