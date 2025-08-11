"""Platform for light integration."""
from __future__ import annotations

from homeassistant.components.light import (
    LightEntity,
    ColorMode,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the light platform."""
    async_add_entities([TestLight()])


class TestLight(LightEntity):
    """Representation of a test light."""

    def __init__(self) -> None:
        """Initialize the light."""
        self._attr_name = "Test Light"
        self._attr_unique_id = "test_light_unique_id"
        self._attr_color_mode = ColorMode.ONOFF
        self._attr_supported_color_modes = {ColorMode.ONOFF}
        self._attr_is_on = False

    def turn_on(self, **kwargs) -> None:
        """Turn the light on."""
        self._attr_is_on = True
        self.schedule_update_ha_state()

    def turn_off(self, **kwargs) -> None:
        """Turn the light off."""
        self._attr_is_on = False
        self.schedule_update_ha_state()