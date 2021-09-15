# 01_FastAPI

## Watch the introduction lesson on Leho
The theoretical session is recorded and put on Leho for you to find.

## Installation
- Clone this repository from GitHub Classrooms.
- Create a new folder called `api`.
- Create a `.env` file in the root of your directory, containing real values based on the `.env.example`.

- Create a new virtual environment on your PC / VM, where you will run your Python code.
`conda create -n 01_fastapi` if you use Conda.
- Activate the conda environment in a terminal.
`conda activate 01_fastapi`.
- `pip install -r api/requirements.dev.txt`

**You do not need to install it in a seperate virtual environment, but take the consequences then!**

## Setup the project
- Add a `main.py` script in your `api > app` folder. Place this inside.
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```