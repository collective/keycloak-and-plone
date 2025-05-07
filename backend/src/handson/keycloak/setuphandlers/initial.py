from handson.keycloak import logger
from pathlib import Path
from plone import api
from plone.exportimport import importers
from Products.GenericSetup.tool import SetupTool


EXAMPLE_CONTENT_FOLDER = Path(__file__).parent / "examplecontent"


def update_keycloak(portal):
    """Set keycloak information on acl_users."""
    plugin = portal.acl_users.oidc
    payload = {
        "issuer": "http://sso.localhost/realms/plone",
        "client_id": "plone",
        "client_secret": "12345678",  # nosec B105
        "scope": ("openid", "profile", "email"),
        "create_restapi_ticket": True,
        "redirect_uris": ("http://localhost:3000/login-oidc/oidc",),
    }
    for key, value in payload.items():
        setattr(plugin, key, value)


def create_example_content(portal_setup: SetupTool):
    """Import content available at the examplecontent folder."""
    portal = api.portal.get()
    importer = importers.get_importer(portal)
    for line in importer.import_site(EXAMPLE_CONTENT_FOLDER):
        logger.info(line)
    update_keycloak(portal)
