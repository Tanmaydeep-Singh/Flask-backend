# Flask Backend Project

This is a Flask-based backend project. Follow the instructions below to set up and run the project locally.

## Prerequisites

Before you begin, make sure you have the following installed:

- [Python 3.7+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/) (Python package installer)

## Setting Up the Project

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone <your-repository-url>
cd <project-folder>
```

### 2. Create a Virtual Environment

Create a virtual environment to isolate project dependencies:

#### Windows:
```bash
python -m venv venv
```

#### macOS/Linux:
```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment

Activate the virtual environment to start using it.

#### Windows:
```bash
.\venv\Scripts\activate
```

#### macOS/Linux:
```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt once the environment is activated.

### 4. Install the Required Dependencies

With the virtual environment activated, install all the necessary dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install all the required libraries, including Flask, pandas, and any other dependencies needed to run the application.

### 5. Run the Flask Application

Once the dependencies are installed, you can run the Flask server with the following command:

```bash
flask run
```

By default, the Flask application will be accessible at `http://127.0.0.1:5000/`. You should see a message indicating that the server is running.

---

## Endpoints

- `GET /`: A simple endpoint to test if the server is running.
- `POST /upload`: Upload a CSV file for processing. You need to send the file as part of a form and include the necessary parameters.


---

## Deactivating the Virtual Environment

Once you are done working with the project, you can deactivate the virtual environment by simply running:

```bash
deactivate
```

This will return you to your system's global Python environment.

---

## Troubleshooting

- If you encounter any issues with missing dependencies, try running `pip install -r requirements.txt` again.
- Ensure your CSV file contains the required columns (`X`, `Y`, and `Z`) when making requests to the `/upload` endpoint.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---