import os


class Environment:

    def __init__(self):
        self.database_file_name = 'database.dat'
        self.database_file_path = '../..'

    def is_database_file_present(self):
        return os.path.exists(os.path.join(self.database_file_path, self.database_file_name))

    def is_database_backup_file_present(self):
        return os.path.exists(os.path.join(self.database_file_path, f'_{self.database_file_name}'))
