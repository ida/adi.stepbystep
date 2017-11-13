"""Definition of the Archetype-Contenttype 'Step'.
"""

from adi.stepbystep.interfaces import IStep
from adi.stepbystep.config import PROJECTNAME
from plone.app.folder import folder 
from zope.interface import implements
from Acquisition import aq_inner
from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata
from Products.Archetypes.public import DisplayList 


StepSchema = folder.ATFolderSchema.copy() + atapi.Schema((
    atapi.TextField('text',
        searchable = True,
        storage = atapi.AnnotationStorage(migrate=True),
        validators = ('isTidyHtmlWithCleanup',),
        default_output_type = 'text/x-html-safe',
        widget = atapi.RichWidget(
        ),
    ),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties:
StepSchema['title'].storage = atapi.AnnotationStorage()
StepSchema['description'].storage = atapi.AnnotationStorage()

# Hide description-field of the user in the edit-form or a base-view of a step:
StepSchema['description'].widget.visible = {'edit': 'hidden', 'view': 'invisible'}

schemata.finalizeATCTSchema(StepSchema, moveDiscussion=False)


class Step(folder.ATFolder):
	"""A contenttype named step for managing processes."""
	implements(IStep)
	meta_type = "Step"
	schema = StepSchema
	title = atapi.ATFieldProperty('title')
	description = atapi.ATFieldProperty('description')

atapi.registerType(Step, PROJECTNAME)
