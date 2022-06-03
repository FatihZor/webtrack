from resources.website_resources import WebsiteResource

def routes_config(api):
    api.add_resource(WebsiteResource, "/website")