from adi.stepbystep.helpers import getNextId

#IObjectInitializedEvent
def setNextId(obj, event):
    id_ = getNextId(obj)
    obj.setId(id_)
    obj.reindexObject()

