import allure
import requests
from selene import browser

from src.utils.config import config


def attach_video_from_browserstack():
    if not config.is_bstack:
        return

    session_id = browser.driver.session_id
    try:
        video_url = f"https://api.browserstack.com/app-automate/sessions/{session_id}.json"

        response = requests.get(video_url, auth=(config.browserstack_username, config.browserstack_access_key))
        response.raise_for_status()

        video_url = response.json()['automation_session']['video_url']
        allure.attach(
            '<html><body>'
            '<video width="100%" height="100%" controls autoplay>'
            f'<source src="{video_url}" type="video/mp4">'
            '</video>'
            '</body></html>',
            name='Test Execution Video',
            attachment_type=allure.attachment_type.HTML,
        )
    except requests.RequestException as e:
        print(f"Failed to retrieve video from BrowserStack: {e}")
