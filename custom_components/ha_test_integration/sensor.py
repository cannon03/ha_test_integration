"""Sensor platform for ha_test_integration."""
from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the sensor platform."""
    async_add_entities([TestSensor()])

class TestSensor(SensorEntity):
    """Representation of a Test Sensor."""
    
    _attr_name = "Test Sensor"
    _attr_native_value = "Hello World"
    
    @property
    def unique_id(self):
        return "test_sensor_unique_id"