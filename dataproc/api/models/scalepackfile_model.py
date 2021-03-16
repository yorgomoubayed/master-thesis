from neomodel import StructuredNode, StringProperty, IntegerProperty,UniqueIdProperty, RelationshipTo
from uuid import uuid4

class ScalepackFile(StructuredNode):
	uuid=StringProperty(unique_index=True, default=uuid4)
	rsf_filetype=StringProperty()
