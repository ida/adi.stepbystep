What
====

"StepByStep" is a Plone-addon for managing processes, including
collaboration, setting priority, track time (start, pause, stop),
assign responsibilities and get overviews and reports.


Why
===

A lot of ticket-systems have difficulties when it comes to
representing priority, cluster tickets as subtickets of a ticket,
and assigning user-permissions. The latter is Plone's strength, let's
take advantage of it.

Because multi-tasking is a myth, as it is provenly not
possible to focus on several things at once. Provide a tool, helping to
enforce doing things step by step and focus with devotion on each step,
one at a time, by inhibiting to be active on several steps at once.


Goals
=====

Be able to navigate very quickly through items by using the tab-key and when
hitting a selected item, show children and also grand-children, if tabbing
further. Tabbing backwards after page-load, will focus the edit-buttons at
bottom, immediately. You can also use the mouse and click your way, of course.

Don't reinvent the wheel, take what Plone has already, be as less intrusive as
possible, follow the usual conventions, so users can instantly understand what
is going on. Avoid unnecessary complexity.

Be fully functional also when Javascript is not available or disabled in the
browser. Enhance progressively, mobile-devices first. That guarantees most
possible robustness and is the best foundation for providing a good
accessibility after the W3C-recommendations.


How
===

Add a step, name it after a project or anything you like, it is then the
root-step for containing all substeps. A step conatining child-steps is
regarded to be a process.


Responsibility
--------------

By default the creator of a step will be the reponsible person. You can
edit the step and change the person in the responsibles-field of the
'persons'-tab, or even add several persons. If so, the first person is
regarded to be the main responsible one.


Prioritisation
--------------

Simply change the order of steps in the folder-contents-view, according to
their importance. The order rules, work on one step after the other.
If a step contains children-steps, they have to be finished one after the
other before you can step further to the parent-step's next sibling.


Collaboration
-------------

To work together on a step and its substeps, we can use Plone's usual
way to set permissions: Click the sharing-tab on a step, select users
or groups and tick the boxes on 'Can add, 'Can edit' and 'Can view',
as wanted. The 'Can review'-permission is not relevant here, anyone
who can edit a step can also change its workflow-state.


Cluster steps
-------------

Add substeps in step, e.g. you have a main-step 'Make coffee' and it has
child-steps 'Cook water', 'Crush beans', 'Pour water over', etc.


Time tracking
-------------

Click the 'Play'-button when starting to work on a step, click 'Pause' when
making a break and click 'Stop', when the finishing a step.


Time planning
-------------

You can use the 'effective'-date-field for defining when a step is supposed to
be started and the 'expiration'-date-field, when a step is supposed to be
finished. If a step is expired or contains expired child-steps, a warning in
its header-area is shown.


Attach files
------------

In step's folder-contents-view click 'Add new' and select 'File'.


Create a report
---------------

Create your own reports (predefined searchresults) by adding collections and
setting their criteria as you wish.


Email-notifications
-------------------
[To do]


Stepbystep ID's
-----------
A stepbystep index-number is stored in the registry, 
it is increased by one (+1) on each creation of 
a stepbystep and sets this number as the identifier (id)
of a stepbystep.

This is a convention to ease referencing stepbystep.

If a user enters an Integer as the Title in any other 
ATContentType, its Id gets 'n' as prefix, to exclude
ambiguity.
