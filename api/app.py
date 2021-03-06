from flask import Blueprint
from flask_restful import Api
from resources.Entry import EntryResource
from resources.Organisation import OrganisationResource


api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# Route
api.add_resource(EntryResource, '/Entry')
api.add_resource(OrganisationResource, '/Org')
