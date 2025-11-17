import logging

from wordlift_client import WebPageImportResponse
from wordlift_sdk.protocol import WebPageImportProtocolInterface

logger = logging.getLogger(__name__)


class WebPageImportProtocol(WebPageImportProtocolInterface):
    async def callback(self, web_page_import_response: WebPageImportResponse) -> None:
        pass
