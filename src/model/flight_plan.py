from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class FlightPlan:
    arrives_at: str
    created_at: str
    departure: str
    destination: str
    distance: int
    fuel_consumed: int
    fuel_remaning: int
    id: str
    ship_id: str
    ship_type: str
    terminated_at: Optional[Any]
    time_remaining_in_seconds: int
    username: str

    @staticmethod
    def from_json(json):
        return FlightPlan(
            arrives_at=json.get('arrivesAt'),
            created_at=json.get('createdAt'),
            departure=json.get('departure'),
            destination=json.get('destination'),
            distance=json.get('distance'),
            fuel_consumed=json.get('fuelConsumed'),
            fuel_remaning=json.get('fuelRemaning'),
            id=json.get('id'),
            ship_id=json.get('shipId'),
            ship_type=json.get('shipType'),
            terminated_at=json.get('terminatedAt'),
            time_remaining_in_seconds=json.get('timeRemainingInSeconds'),
            username=json.get('username')
        )
