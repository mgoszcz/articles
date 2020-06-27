import os


class Environment:

    def __init__(self):
        self.database_file_name = 'database.dat'
        self.database_file_path = '..\\..'
        self._test_data_path = '..'

    def is_database_file_present(self):
        return os.path.exists(os.path.join(self.database_file_path, self.database_file_name))

    def is_database_backup_file_present(self):
        return os.path.exists(os.path.join(self.database_file_path, f'_{self.database_file_name}'))

    @property
    def test_data_path(self):
        return os.path.join(self._test_data_path, 'test_data')

    @property
    def database_file(self):
        path = os.path.join(self.database_file_path, self.database_file_name)
        return os.path.join(self.database_file_path, self.database_file_name)