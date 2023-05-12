from feast import (
    Entity,
)

# Define an entity for the driver. You can think of an entity as a primary key used to
# fetch features.
driver = Entity(
    name="driver",
    join_keys=["driver_id"],
    description="driver id",
)
