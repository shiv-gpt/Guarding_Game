# -*- coding: utf-8 -*-
# Written by Robin Burchell
# No licence specified or required, but please give credit where it's due,
# and please let me know if this helped you. Feel free to contact with corrections or suggestions.
#
# We're using PySide, Nokia's official LGPL bindings.
# You can however easily use PyQt (Riverside Computing's GPL bindings) by
# commenting these and fixing the appropriate imports.
from PySide.QtCore import *
from PySide.QtGui import *
#from PyQt4 import *
#from PyQt4.QtCore import *
#from PyQt4.QtGui import *
import sys

# As always, Qt allows us to subclass objects to override behaviour and generally monkey around
# with them how we want. This is the exact way that custom widget painting operates:
# you subclass the widget that you want as your base, and override paintEvent() to do your own painting.
class CustomWidget(QWidget):
 # We're taking a number and displaying it twice in different formats. Nothing complicated.
 def __init__(self, parent, anumber):
  QWidget.__init__(self, parent)

  # store the passed number
  self._number = anumber

 # This is where our custom painting happens. Qt calls paintEvent() whenever this widget needs
 # to repaint itself.
 #
 # If you ever need to force a widget to repaint, which you will if you e.g. change any data the widget
 # displays, you shouldn't invoke paintEvent manually: instead, you should use QWidget::update().
 # For more information on invoking a repaint, see:
 # http://doc.trolltech.com/4.6/qwidget.html#update
 #
 # For more information on paintEvent, see:
 # http://doc.trolltech.com/4.6/qwidget.html#paintEvent
 def paintEvent(self, ev):
  # We first need to create a painter. Think of the painter as the brains of the rendering operation:
  # they control the pen, and the brush, in order to do the actual drawing operations. More on them later.
  #
  # We pass 'self' to QPainter so it knows what it is painting on.
  # You can also use QPainter::begin() and QPainter::end(), but this method is easier since it will
  # automatically end() when it deallocates.
  # See also:
  # http://doc.trolltech.com/4.6/qpainter.html
  p = QPainter(self)

  # Simple operation here. Let's paint the background spotted red, so we can see that painting
  # is actually occuring. This will look hideous, but feel free to experiment.
  #
  # This demonstrates the first use of QBrush - QBrush is used for any fill operations performed
  # by QPainter. In terms of painting a picture, think of it like this: a painter will pick up a brush
  # to paint broad strokes of the background etc.
  #
  # QBrush is very versatile, you can do all sorts of things with it like drawing textures.
  # For more information on QBrush, see:
  # http://doc.trolltech.com/4.6/qbrush.html
  #
  # This also demonstrates another aspect of the painting system: that of rects. Painting in Qt is done
  # around the concept of small areas where painting occurs, we're using a convenience method here (QWidget::rect())
  # to get the entire area of the widget, but you can define and adjust rects yourself.
  # We'll go into more detail on that another time.
  # For more information on QRect, see:
  # http://doc.trolltech.com/4.6/qrect.html
  p.fillRect(self.rect(), QBrush(Qt.red, Qt.Dense2Pattern))

  # Now, we're going to draw the number we were passed. This won't be using the brush, but the
  # pen: more on that later. Let's just draw some text in the middle left of the widget for now.
  # Thankfully, Qt provides a way to do this for us, so we don't need to do any work on adjusting the rect.
  # For more information on drawing text, see:
  # http://doc.trolltech.com/4.6/qpainter.html#drawText
  p.drawText(self.rect(), Qt.AlignLeft | Qt.AlignVCenter, str(self._number))

  # Now, let's draw a different number (just for demonstration purposes) with a different colour.
  # To do this, we first need to set a new pen - but now you're probably wondering what that is.
  #
  # A pen is, like it's real world counterpart, used to draw fine detail, like text, lines, and outlines.
  # It is the emphasis, where the brush is the background.
  # For more information on QPen, see:
  # http://doc.trolltech.com/4.6/qpen.html
  #
  # QColor is fairly simplistic here, so I won't go into it. We're just using the RGB constructor to create
  # a grey color.
  # For more information, see:
  # http://doc.trolltech.com/4.6/qcolor.html#QColor-2
  p.setPen(QColor(220, 220, 220))

  # Now we've set our grey pen, let's take the value we have, multiply it by two, and draw it on the right hand
  # side of the widget.
  p.drawText(self.rect(), Qt.AlignRight | Qt.AlignVCenter, str(self._number * 2))

class MyMainWindow(QMainWindow):
 def __init__(self, parent):
  QMainWindow.__init__(self, parent)

  # Add content
  central = CustomWidget(self, 666)
  self.setCentralWidget(central)

if __name__ == '__main__':
 app = QApplication(sys.argv)
 sw = MyMainWindow(None)
 sw.show()
 app.exec_()