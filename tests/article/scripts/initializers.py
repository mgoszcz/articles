import os
from shutil import move

from tests.article.scripts.environment import Environment

ENVIRONMENT = Environment()


def initialize_save_test():
    if Environment().is_database_file_present():
        existing_file = os.path.join(ENVIRONMENT.database_file_path, ENVIRONMENT.database_file_name)
        new_file = os.path.join(ENVIRONMENT.database_file_path, f'_{ENVIRONMENT.database_file_name}')
        move(existing_file, new_file)


