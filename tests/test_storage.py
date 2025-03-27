import json
from pathlib import Path

from kanbanpy.storage import Storage


class TestStorage:
    def test_file_creation(self, tmp_path: Path):
        """Test that a data file is created when creating a new object.
        """
        data_file = tmp_path / 'data.json'
        Storage(data_file)

        assert data_file.exists()
        assert data_file.is_file()

    def test_data_read(self, tmp_path: Path):
        """Test that the data retrieved from the file is parsed as JSON.
        """
        data_file = tmp_path / 'data.json'
        with open(data_file, 'w') as fp:
            json.dump({'item': 'value'}, fp)

        s = Storage(data_file)
        result = s.read()

        assert isinstance(result, dict)
        assert result['item'] == 'value'

    def test_data_write(self, tmp_path: Path):
        """Test that the JSON written by the storage object is persisted in the
        file.
        """
        data_file = tmp_path / 'data.json'
        s = Storage(data_file)
        s.write({'item': 0})

        with open(data_file) as fp:
            content = json.load(fp)

        assert isinstance(content, dict)
        assert content['item'] == 0
