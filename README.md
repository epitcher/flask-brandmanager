# flask-brandmanager

[![pytest](https://github.com/epitcher/flask-brandmanager/actions/workflows/pytest.yml/badge.svg)](https://github.com/epitcher/flask-brandmanager/actions/workflows/pytest.yml)

**todo**

## Prerequisites

- Python 3+
- Docker (optional)
- pyenv (optional)
- npm (optional)

## Stack
- Flask
- VueJs
- Tailwindcss

## Getting Started

There are two ways to set up and run this project:

### Option 1: Using Docker Compose

1. Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/), if not already installed.

2. Clone the repository:
```bash
git clone https://github.com/epitcher/flask-brandmanager.git
```

3. Change to the project directory:
```bash
cd flask-brandmanager
```

4. Run the application with Docker Compose:
```bash
docker-compose up
```


### Option 2: Running Locally

1. Ensure you have Python 3+ installed. You can check the Python version by running:

```bash
python --version
```

If you don't have Python 3, you can download it from the [official website](https://www.python.org/downloads/).

2. Clone the repository:
```bash
git clone https://github.com/epitcher/flask-brandmanager.git
```

3. Change to the project directory:
```bash
cd flask-brandmanager
```

4. Install the required packages:
```bash
python -m pip install -r requirements.txt
```

5. Install the required npm packages:
```bash
npm install
```

6. Generate CSS files:
```bash
npm run styles
```

7. Run the application:
```
python run.py
```

## Using VueJs

1. Navigate to frontend
    ```bash
    cd frontend
    ```

2. Build from vuejs files
    ```bash
    npm run build
    ```

## Helpful Stuff

- `npm run coverage`  Runs test coverage analysis on the codebase and calculates the percentage of code covered by tests.


## Usage

Open your web browser and navigate to `http://localhost:5000`. 
