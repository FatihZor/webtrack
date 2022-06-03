from resources.base_resource import BaseResource

from services.website_service import WebsiteService

class WebsiteResource(BaseResource):
    def __init__(self):
        super().__init__()
        self.website_service = WebsiteService

    def get(self):
        website_name = self.website_service.fetch_website("website")
        return {'hello': website_name}
        