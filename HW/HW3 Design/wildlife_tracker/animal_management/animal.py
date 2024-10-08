from typing import Any, Optional

class Animal:

    def __init__(self,
                animal_id: int,
                age: Optional[int] = None,
                health_status: Optional[str] = None) -> None:
        self.animal_id = animal_id
        self.age = age or 0
        self.health_status = health_status or ""
        
