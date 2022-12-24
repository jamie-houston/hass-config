from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.entity import DeviceInfo
import petsafe
from .const import DOMAIN, MANUFACTURER
from . import PetSafeData
from typing import Any


class PetSafeSwitchEntity(CoordinatorEntity, SwitchEntity):
    def __init__(
        self,
        hass,
        api_name,
        name,
        coordinator,
        device_type,
        icon=None,
        device_class=None,
        entity_category=None,
    ):
        super().__init__(coordinator)
        self._attr_name = name
        self._attr_device_class = device_class
        self._attr_has_entity_name = True
        self._coordinator = coordinator
        self._api_name = api_name
        self._attr_should_poll = True
        self._attr_unique_id = api_name + "_" + device_type
        self._attr_icon = icon
        self._device_type = device_type
        self._attr_entity_category = entity_category


class PetSafeLitterboxSwitchEntity(PetSafeSwitchEntity):
    def __init__(
        self,
        hass,
        name,
        coordinator,
        device_type,
        device: petsafe.devices.DeviceScoopfree,
        icon=None,
        device_class=None,
        entity_category=None,
    ):
        self._litterbox = device

        super().__init__(
            hass,
            device.api_name,
            name,
            coordinator,
            device_type,
            icon,
            device_class,
            entity_category,
        )

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device.api_name)},
            manufacturer=MANUFACTURER,
            name=device.friendly_name,
            model=device.data["productName"],
            sw_version=device.data["shadow"]["state"]["reported"]["firmware"],
        )

    def _handle_coordinator_update(self) -> None:
        data: PetSafeData = self.coordinator.data
        litterbox: petsafe.devices.DeviceScoopfree = next(
            x for x in data.litterboxes if x.api_name == self._api_name
        )

        self.async_write_ha_state()
        return super()._handle_coordinator_update()


class PetSafeFeederSwitchEntity(PetSafeSwitchEntity):
    def __init__(
        self,
        hass,
        name,
        coordinator,
        device_type,
        device: petsafe.devices.DeviceSmartFeed,
        icon=None,
        device_class=None,
        entity_category=None,
    ):
        self._feeder = device

        super().__init__(
            hass,
            device.api_name,
            name,
            coordinator,
            device_type,
            icon,
            device_class,
            entity_category,
        )

        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, device.api_name)},
            manufacturer=MANUFACTURER,
            name=device.friendly_name,
            sw_version=device.data["firmware_version"],
            model=device.data["product_name"],
        )
        self._device = device

    def _handle_coordinator_update(self) -> None:
        data: PetSafeData = self.coordinator.data
        feeder: petsafe.devices.DeviceSmartFeed = next(
            x for x in data.feeders if x.api_name == self._api_name
        )
        if self._device_type == "child_lock":
            self._attr_is_on = feeder.child_lock
        elif self._device_type == "feeding_paused":
            self._attr_is_on = feeder.paused

        self.schedule_update_ha_state(True)
        return super()._handle_coordinator_update()

    async def async_update(self) -> None:

        if self._attr_device_class == "timestamp":
            data: PetSafeData = self.coordinator.data
            feeder: petsafe.devices.DeviceSmartFeed = next(
                x for x in data.feeders if x.api_name == self._api_name
            )
            feeding = await self.hass.async_add_executor_job(feeder.get_last_feeding)

        return await super().async_update()

    def turn_on(self, **kwargs: Any) -> None:
        if self._device_type == "child_lock":
            self._device.child_lock = True
        elif self._device_type == "feeding_paused":
            self._device.paused = True

    def turn_off(self, **kwargs: Any) -> None:
        if self._device_type == "child_lock":
            self._device.child_lock = False
        elif self._device_type == "feeding_paused":
            self._device.paused = False
