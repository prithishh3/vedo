"""Mouse click and other type of events
will trigger a call to a custom function"""
from vedo import printc, Plotter, Mesh, datadir

printc("Click object to trigger a function call", invert=1)

# callback functions
def onLeftClick(event):
    if not event.actor:
        return
    printc("Left button pressed on", [event.actor], c=event.actor.color())
    # printc('full dump of event:', event)

def onEvent(event):
    printc(event.name, 'happened at mouse position', event.picked2d)

######################
tea = Mesh(datadir+"teapot.vtk").c("gold")
mug = Mesh(datadir+"mug.ply").rotateX(90).scale(8).pos(2,0,-.7).c("silver")

plt = Plotter(axes=11)
plt.addCallback('LeftButtonPress', onLeftClick)
plt.addCallback('Interaction', onEvent) # mouse dragging triggers this
plt.show(tea, mug, __doc__)
