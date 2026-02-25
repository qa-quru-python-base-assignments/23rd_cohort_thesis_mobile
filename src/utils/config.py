import os
from enum import Enum
from typing import Optional

from dotenv import load_dotenv
from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Context(str, Enum):
    LOCAL_EMULATOR = 'local_emulator'
    LOCAL_REAL = 'local_real'
    BSTACK = 'bstack'


class Settings(BaseSettings):
    context: Context = Context.BSTACK

    # --- Appium ---
    remote_url: str = 'http://127.0.0.1:4723'
    platform_name: str = 'android'
    platform_version: str = '11.0'
    device_name: str = 'emulator-5554'
    appium_app: str = ''
    app_package: Optional[str] = None
    app_activity: Optional[str] = None
    appium_automation_name: Optional[str] = None

    # --- BrowserStack ---
    browserstack_username: Optional[str] = None
    browserstack_access_key: Optional[str] = None
    project_name: Optional[str] = None
    build_name: Optional[str] = None
    session_name: Optional[str] = None
    local: Optional[str] = None
    debug: Optional[str] = None
    network_logs: Optional[str] = None
    video: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file_encoding='utf-8',
        extra='ignore',
    )

    @model_validator(mode='after')
    def _set_automation_name(self):
        if not self.appium_automation_name:
            self.appium_automation_name = (
                'XCUITest' if self.platform_name.lower() == 'ios' else 'UiAutomator2'
            )
        return self

    @property
    def is_bstack(self) -> bool:
        return self.context == Context.BSTACK

    @property
    def is_local(self) -> bool:
        return self.context in (Context.LOCAL_EMULATOR, Context.LOCAL_REAL)

    @property
    def bstack_options(self) -> dict:
        return {
            'userName': self.browserstack_username,
            'accessKey': self.browserstack_access_key,
            'projectName': self.project_name,
            'buildName': self.build_name,
            'sessionName': self.session_name,
            'local': self.local,
            'debug': self.debug,
            'networkLogs': self.network_logs,
            'video': self.video,
        }


def create_config() -> Settings:
    context = os.getenv('CONTEXT', Context.BSTACK.value)
    env_file = f'.env.{context}'

    load_dotenv(env_file, override=True)

    if context == Context.BSTACK.value:
        load_dotenv('.env.credentials', override=False)

    return Settings(_env_file=env_file)


config = create_config()
