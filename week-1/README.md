# Mentoring Coding Challenges

This is a series of coding challenges to be used as part of some guided mentoring sessions. They are designed to be done in paired programming sessions, taking time to discuss the problems as well as the solutions. Starting out quite easily, they ramp up in difficulty and cover a number of techniques.

## Setup

Part of the process is designed to see what the mentee's workflow is. As part of this, it is preferable to observe how they setup their session:
- Do they use shortcuts?
- Are they thinking of tests before they start coding?
- Do they use Git?

## Testing

These are designed to be tested with `pytest` with no need for any additional config. It might be useful to include `pytest-cov` so they can see the bits of code that they miss in their testing.

As such, the challenges should be tested with the following where `examples` is the name of the file that is being tested:

```bash
pytest --cov examples --cov-report html tests/
```

The report can then be opened with the following into a browser window:

```bash
open htmlcov/examples_py.html
```

## Topics for discussion
- Workflow
- Using tests for debugging
- How to research

## ~/.zshrc

I recommend sharing useful workflow techniques such as this bit of script from the `~/.zshrc` file:

```bash
# Python Shortcuts

# Highlight colors
function bold_green {
  echo -e "\033[1;32m$1\033[0m"
}

function bold_blue {
  echo -e "\033[1;34m$1\033[0m"
}

# Activates a virtual environment
alias act="source venv/bin/activate"

# Creates a new virtual environment, updates Pip, adds a .gitignore to the virtual environment
function virtual {
  bold_green "Creating new enviromnent"
  python -m venv venv
  act
  bold_green "Updating pip"
  python -m pip install --upgrade pip
  bold_green "*" > venv/.gitignore
}

# Installs python packages from the requirements.txt file. Useful for existing repos
function pir {
  virtual
  bold_green "Installing python packages"
  python -m pip install -r requirements.txt
  bold_green "Reactivating venv"
  deactivate
  act
}

# Installs a list of python packages
function pin {
  if [[ "$1" == "--help" ]]; then
    bold_blue "Usage: pin <package1> <package2> <package3>..."
    bold_blue "Shortcut for installing the specified Python packages. Deactivates and reactivates venv to ensure correct version of package is used."
    return
  fi

  bold_green "Installing packages: $@"

  for arg in "$@"; do
    python -m pip install "$arg"
  done
    
  bold_green "\nReactivating environment"

  deactivate
  act
}

# Useful for starting new projects
function start {
  if [[ "$1" == "--help" ]]; then
    bold_blue "Usage: start <folder_name> <package1> <package2> ..."
    bold_blue "Create a new directory with the specified name and install the specified Python packages."
    return
  fi

  local folder_name="$1"  # First argument is the name of the folder
  shift  # Shift the arguments to remove the folder name from the argument list

  bold_green "Making new directory"
  mkdir "$folder_name" # Makes a new directory
  cd "$folder_name" # Changes into new directory

  virtual # Creates new virtual environment

  pin "$@" # Installs packages
    
  bold_green "Finishing setup"
  touch api.py # Makes generic start file

  export PYTHONPATH=. # Sets Python Path to the root directory (useful for pytest)

  code . # Opens VSCode
  bold_green "Done"
}
```

This adds the following benefits:
- `bold_green` and `bold_blue` are for highlighting colors
- `act` activates existing virtual environments created with the above command
- `virtual` creates a new virtual environment with the latest version of `pip`
- `pir` installs from the requirements.txt. Useful for existing repos
- `pin` is a shortcut for installing multiple packages, for instance `pin pytest pytest-cov` will install both packages
- `start` does all of the above but also creates a new directory complete with a start file `api.py` and opens everything in VSCode