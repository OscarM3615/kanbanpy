# kanbanpy

A console-based Kanban task manager created in Python.

Create and manage tasks visually in your terminal using simple commands.

## Features

- Simple CLI commands
- ASCII based kanban board
- Easy setup
- Stores tasks in a readable format (JSON).

## Installation

Install using pip running the following command in the terminal:

```sh
pip install kanbanpy
```

## Configuration

kanbanpy requires a config file located in the user's home directory. This file
can be generated using the `setup` command:

```sh
# Run the setup wizard
kanbanpy setup

# Or use the defaults
kanbanpy setup -y
```

## Usage

If you installed the library, you can use the CLI as a system command:

```sh
kanbanpy [...args]
```

Or call it as a Python import:

```sh
python -m kanbanpy [...args]
```

### Examples

Here are some examples of the commands available:

```sh
# Just display the kanban board
kanbanpy

# Create a new task
kanbanpy create "A new todo"

# Move task with id 1 to the next status
kanbanpy next 1

# Revert a task with id 1 to the previous status
kanbanpy prev 1

# Remove task with id 1
kanbanpy remove 1
```

Commands also have convenient aliases:

- `create`: `c`
- `next`: `n`
- `prev`: `p`
- `remove`: `r`

To explore the full list of commands, run:

```sh
kanbanpy --help
```

## Contributing

Thank you for considering contributing to my project! Any pull requests are
welcome and greatly appreciated. If you encounter any issues while using
the project, please feel free to post them on the issue tracker.

To contribute to the project, please follow these steps:

1. Fork the repository.
2. Add a new feature or bug fix.
3. Commit them using descriptive messages, using
   [conventional commits](https://www.conventionalcommits.org/) is recommended.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file
for more details.
