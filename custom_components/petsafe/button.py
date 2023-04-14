from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady

from . import ButtonEntities, PetSafeCoordinator
from .const import DOMAIN


async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry, add_entities):
    coordinator: PetSafeCoordinator = hass.data[DOMAIN][config.entry_id]

    feeders = None
    litterboxes = None
    try:
        feeders = await coordinator.get_feeders()
        litterboxes = await coordinator.get_litterboxes()
    except Exception as ex:
        raise ConfigEntryNotReady("Failed to retrieve PetSafe devices") from ex

    entities = []
    for feeder in feeders:
        entities.append(
            ButtonEntities.PetSafeFeederButtonEntity(
                hass=hass,
                name="Feed",
                device_type="feed",
                device=feeder,
                coordinator=coordinator,
            )
        )
    for litterbox in litterboxes:
        entities.append(
            ButtonEntities.PetSafeLitterboxButtonEntity(
                hass=hass,
                name="Clean",
                device_type="clean",
                device=litterbox,
                coordinator=coordinator,
            )
        )
        entities.append(
            ButtonEntities.PetSafeLitterboxButtonEntity(
                hass=hass,
                name="Reset",
                device_type="reset",
                device=litterbox,
                coordinator=coordinator,
            )
        )
    add_entities(entities)
