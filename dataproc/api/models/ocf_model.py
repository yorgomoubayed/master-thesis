from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo

from api.models.reflectionstructurefactors_model import RefelctionStructureFactors
from api.models.coordinates_model import Coordinates

class OCF(StructuredNode):
	
	# Relationships
	has_rsf=RelationshipTo(RefelctionStructureFactors, 'HAS')
	has_coordinates=RelationshipTo(Coordinates, 'HAS')

	@property
	def serialize(self):

		"""
		Serializer for node properties
		"""
		
	    return {
	        'node_properties': {
	            # 'uuid': self.uuid,
	            # 'coordinates_filetype': self.coordinates_filetype,
	        },
	    }