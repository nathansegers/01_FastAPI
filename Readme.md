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

**I have tested all of this in a fresh VM, where I only installed pip: `sudo apt-get install python3-pip`.**

## Setup the project
- Add a `main.py` script in your `api > app` folder. Place this inside.
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Make sure you are inside your `api > app` folder, then execute `python3 -m uvicorn main:app --reload`. This will launch uvicorn, and make sure it auto-reloads on any change you make. If you are working with Visual Studio Code, you will get a message that there is a port running, and you can open this in the browser.
VSCode also port-forwards any ports running in a VM.

Visit your application on `127.0.0.1:8000`. You will get a default `{"message":"Hello World"}` if everything goes well.

The cool thing about FastAPI is that it automatically enables and runs a Swagger API as well. You can visit it at the `/docs` page. Check it out!

## Adding our first routes

As this API is all about Bird spotting, we will add a little bit of structure to our API in order to get started.

### Schemas

- Create a `schemas` directory under `app`. Add two empty Python files: `bird.py` and `user.py`. Here we will write `pydantic` code to define our models.

```python

# bird.py
from pydantic import BaseModel

class Bird(BaseModel):
    uuid: str
    id: str
    name: str
    short: str
    image: str
    recon: list
    food: dict
    see: str
```

- Create the `user.py` schema yourself. A User must have a `uuid`, name, locationOfResidence, age, gender and a registrationDate.

- Also make sure there is a method called `sayHello()` on the class which will say something base on the name of the bird or user.

### Adding routes
- In `main.py` add a few birds and a user. You can find the JSON of birds in the repo.