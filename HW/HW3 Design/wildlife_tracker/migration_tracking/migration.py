from typing import Any

class Migration:

    def __init__(self, 
                current_date: str,
                current_location: str,
                start_date: str) -> None:
        self.currend_date = current_date
        self.current_location = current_location
        self.start_date = start_date