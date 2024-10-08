from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath





class MigrationManager:

    def __init__(self,
                migration_path: MigrationPath,
                path_id: int,
                ) -> None:
        self.migration_path = migration_path
        self.path_id = path_id
        paths: dict[int, MigrationPath] = {}

    def get_migration_path_by_id(self, path_id: int) -> MigrationPath:
        pass

    def get_migration_paths(self) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_destination(self, destination: Habitat) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_species(self, species: str) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_start_location(self, start_location: Habitat) -> list[MigrationPath]:
        pass

    #Check again
    def get_migrations_by_migration_path(self, migration_path_id: int) -> list[Migration]:
        pass

    def get_migration_path_details(self, path_id) -> dict:
        pass

    def remove_migration_path(path_id: int) -> None:
        pass

    #Check again --> Pretty sure this is wrong
    def schedule_migration(self, migration_path: MigrationPath) -> None:
        pass

    def update_migration_path_details(self, path_id: int, **kwargs) -> None:
        pass

