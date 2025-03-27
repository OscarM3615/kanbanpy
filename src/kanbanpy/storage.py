import json
from pathlib import Path
from typing import Any


class Storage:
    """This class is responsible for storing the app data in the filesystem.

    App data is stored as JSON.
    """

    def __init__(self, data_path: Path):
        """Initialise the storage instance.

        :param data_path: path to the data file
        """
        self.data_path = data_path

        if not data_path.exists():
            self._create_data_file()

    def _create_data_file(self):
        """Create an initial data file on the filesystem.
        """
        self.data_path.parent.mkdir(parents=True, exist_ok=True)
        self.write([])

    def read(self) -> Any:
        """Retrieve the data from the filesystem.

        :return: JSON structure
        """
        with open(self.data_path) as data_file:
            content = json.load(data_file)
        return content

    def write(self, data: Any):
        """Write data to the filesystem.

        :param data: _description_
        """
        with open(self.data_path, 'w') as data_file:
            json.dump(data, data_file, indent=2)
