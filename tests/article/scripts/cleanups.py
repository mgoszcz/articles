from shutil import move
import os

from tests.article.scripts.environment import Environment

ENVIRONMENT = Environment()


def cleanup_save_test():
    if os.path.exists(ENVIRONMENT.database_file):
        os.remove(ENVIRONMENT.database_file)
    if ENVIRONMENT.is_database_backup_file_present():
        existing_file = os.path.join(ENVIRONMENT.database_file_path, f'_{ENVIRONMENT.database_file_name}')
        new_file = os.path.join(ENVIRONMENT.database_file_path, ENVIRONMENT.database_file_name)
        move(existing_file, new_file)
