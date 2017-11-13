from Acquisition import aq_inner, aq_parent
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.browser.navtree import getNavigationRoot
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from adi.commons.commons import htmlToText
from adi.devgen.helpers.times import getAge
from adi.devgen.helpers.users import getCurrentUser
from adi.stepbystep.helpers import getActiveTime
from adi.stepbystep.helpers import getActiveTimes
from adi.stepbystep.helpers import getActivitiesReport
from adi.stepbystep.helpers import getActivityReport
from adi.stepbystep.helpers import getStepOverdues
from zope.publisher.browser import TestRequest
from zope.site.hooks import getSite as portal


class View(BrowserView):

    def getActiveTime(self):
        item = self.context
        return getActiveTime(item)

    def getActiveTimes(self):
        item = self.context
        return getActiveTimes(item)

    def getActivitiesReport(self):
        item = self.context
        return getActivitiesReport(item)

    def getActivityReport(self):
        item = self.context
        return getActivityReport(item)

    def getAge(self):
        item = self.context
        return getAge(item)

    def getChildSteps(self, context=None):
        if not context: context = self.context
        return context.listFolderContents(
            contentFilter={'portal_type':'Step'})

    def getPlainText(self):
        item = self.context
        text = item.getText()
        text = htmlToText(text)
        return text

    def getReporter(self, context=None):
        if not context: context = self.context
        reporter = context.getOwner()
        return reporter

    def getStepPosNr(self, step=None):
        """
        Like self.getPosNr(), but only count steps, no other content-types.
        """
        # If no obj is passed, default to context:
        if not step: step = self.context
        if step.Type() == 'Step':
            step = step.aq_inner
            nr = 0
            parent = step.aq_parent
            siblings = parent.listFolderContents(
                        contentFilter={"portal_type" : "Step"})
            for sibling in siblings:
                nr += 1
                if sibling['id'] == step.id:
                    return nr
        return None

    def getStepPosNrs(self, obj=None):
        """
        Like self.getPosNrs(), but only as long as step is a child of step,
        breaks when other portal_type is detected as parent. Return a nr-path
        like: '2.4.1'.
        """
        nrs = None
        if not obj: obj = self.context
        if obj.Type() == 'Step':
            nrs = str( self.getStepPosNr(obj) )
            parent = obj.aq_parent
            while parent is not portal():
                nrs = str( self.getStepPosNr(parent) ) + '.' + nrs
                parent = parent.aq_parent
                if parent.Type() != 'Step':
                    break
            nrs = '.'.join(nrs.split('.')[1:]) # omit nr for root-step
        return nrs

    def getStepOverdues(self):
        return getStepOverdues(self.context)

    def hasChildren(self, obj=None):
        HAS_CHILDREN = False
        if not obj: obj = self.context
        if len(obj.getFolderContents()) > 0: HAS_CHILDREN = True
        return HAS_CHILDREN

    def hasChildSteps(self, obj=None):
        HAS_CHILDSTEPS = False
        if not obj: obj = self.context
        if len(self.getChildSteps(obj)) > 0: HAS_CHILDSTEPS = True
        return HAS_CHILDSTEPS

    def isRootStep(self):
        """
        A step which is not a child of a step, is ragarded to be a root-step.
        """
        parent = self.context.aq_parent
        if parent == portal() or parent.Type() != 'Step': return True
        else: return False

    def my_activetimes(self):
        context = aq_inner(self.context)
        current_user = getCurrentUser(self)
        result = getActiveTimes(context, current_user)
        return result

    def my_stepbystep(self):
        """
        Return all stepbystep where the current
        logged-in user is the responsible person.
        """
        records = []
        criteria = {}
        context = aq_inner(self.context)
        current_user = getCurrentUser(self)
        searchpath = getNavigationRoot(context)

        criteria['path'] = searchpath
        criteria['Type'] = 'Step'
        criteria['Creator'] = current_user

        brains = self.context.queryCatalog(criteria)

        for brain in brains:
            obj = brain.getObject()
            records.append(obj)

        return records

