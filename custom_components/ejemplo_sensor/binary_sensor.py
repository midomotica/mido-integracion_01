from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.const import STATE_HOME
from homeassistant.core import callback

ENTITY_OBSERVADA = "person.javier_brard"

async def async_setup_entry(hass, config_entry, async_add_entities):
    sensor = CondicionSensor(hass, config_entry.data.get("name", "Estado Ejemplo"))
    async_add_entities([sensor])

class CondicionSensor(BinarySensorEntity):
    def __init__(self, hass, name):
        self._hass = hass
        self._attr_name = name
        self._attr_is_on = False

    async def async_added_to_hass(self):
        self._hass.helpers.event.async_track_state_change(
            ENTITY_OBSERVADA, self._estado_actualizado
        )
        estado_inicial = self._hass.states.get(ENTITY_OBSERVADA)
        if estado_inicial:
            self._actualizar_estado(estado_inicial.state)

    @callback
    def _estado_actualizado(self, entity_id, old_state, new_state):
        if new_state:
            self._actualizar_estado(new_state.state)

    def _actualizar_estado(self, nuevo_estado):
        self._attr_is_on = nuevo_estado == STATE_HOME
        self.async_write_ha_state()

