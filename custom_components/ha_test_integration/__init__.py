"""The ha_test_integration Integration."""
from homeassistant.core import HomeAssistant

DOMAIN = "ha_test_integration"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the ha_test_integration integration."""
    hass.data[DOMAIN] = {}
    return True