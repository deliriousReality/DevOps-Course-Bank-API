# Bank API

This is a standalone exercise to practice writing tests and engaging in Test Driven Development (TDD).

## Setup

This project requires Python 3.7 and uses Poetry for Python to handle dependencies. Follow the instructions 
[here](https://python-poetry.org/docs/#installation) to set up Poetry.

Run the following command (run from the project root) to install project dependencies:

`$ poetry install`

You should get a prompt from VSCode to use the newly added virtual environment. Agree to it.

If you do not see a prompt, press `Cmd/Ctrl + Shift + P` and run `Python: Select Interpreter`. Select the python.exe in the newly created `.venv` directory.

To launch the API, run the following:

```bash
$ cd bank_api
$ poetry run flask run
```

The API should be live with swagger docs visible at http://localhost:5000/.

## Tests

You can run both unit and integration tests suites using pytest. Run this from the root directory:

`$ poetry run pytest`

Or you can run them from VSCode:

Click the conical flask icon on the activity bar on the left edge of VSCode. Click the refresh icon at the top of the panel to rediscover tests. Click the play icon at the top to run all tests. Click the play icon next to a file or test name to run that file or test individually.
* Intellisense annotations for running/debugging each test should also appear above the test functions in the code.
* If test discovery fails, check that Poetry has installed your dependencies and that the Python interpreter is selected correctly - you should be using the executable from the .venv folder.0