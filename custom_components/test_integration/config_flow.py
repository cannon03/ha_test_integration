"""Config flow for Test Integration."""
from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigFlow
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN


class TestIntegrationConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Test Integration."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Test Integration", data={})

        return self.async_show_form(step_id="user")