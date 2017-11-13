import time
from adi.devgen.helpers.workflow import setState
from adi.devgen.helpers.workflow import switchState
from DateTime import DateTime
from helpers import getNextId


def addStep(parent):
    id_ = getNextId(parent)
    typ = 'Step'
    title = 'Sample title of ' + id_ 
    text = 'Sample text of ' + id_ + '.'
    parent.invokeFactory(typ, id_, title=title, text=text)
    step = parent[id_]
    step.reindexObject()
    return step

def addSteps(context, n=3):
    while n > 0:
        if n == 1:
            context = addStep(context)
        else: addStep(context)
        n -= 1
    return context

def createContent(context):
    context = addStep(context)
    context.reindexObject()
    context = addSteps(context)
    addSteps(context)
    context = addSteps(context)
    addSteps(context)
    return context

def createHistory(context):
    switchState(context, 'start')
    time.sleep(2)
    switchState(context, 'pause')
    switchState(context, 'start')
    time.sleep(2)
    switchState(context, 'stop')
 
def setupVarious(context):
    portal = context.getSite()
    if context.readDataFile('adi.stepbystep.marker.txt') is None:
        return
    tellStory(portal)

def tellStory(portal):
    context = portal
    context = createContent(context)
    context.setExpirationDate(DateTime())
    context.setTitle('I am an expired step')
    createHistory(context)

