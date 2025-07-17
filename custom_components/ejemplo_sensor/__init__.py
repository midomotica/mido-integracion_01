from homeassistant.config_entries import ConfigEntry, async_forward_entry_setup, async_forward_entry_unload
from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: dict):
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    await async_forward_entry_setup(hass, entry, "binary_sensor")
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    return await async_forward_entry_unload(hass, entry, "binary_sensor")


