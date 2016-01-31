Cute
====

Cross-Qt compatibility module for IDAPython.

What is it?
-----------

Cute is a tiny compatibility module, to allow IDAPython code to use
PySide/Qt4 and PyQt/Qt5 seamlessly.

Motivation
----------

Cute was originally a part of
`Sark <https://github.com/tmr232/Sark/blob/master/sark/qt.py>`__
(``sark.qt``). Since no-one likes dependencies, especially for things
this small, no-one used it. So I decided to release it as a separate
module as well, so that people can just take the file as-is and use it
in their own code.

Usage
-----

Qt Modules
~~~~~~~~~~

Importing ``QtCore``, ``QtGui`` and ``QtWidgets`` works for all Qt
versions. For Qt4, ``QtWidgets`` is an alias for ``QtGui``, so Qt5 code
with ``QtWidgets`` / ``QtGui`` separation will work on Qt4 as well.

::

    from cute import QtCure, QtGui, QtWidgets

Connecting to Signals
~~~~~~~~~~~~~~~~~~~~~

Cute offers a ``cute.connect(...)`` method to mitigate the difference
between Qt4 and Qt5.

::

    # Qt4 Code:
    QtCore.QObject.connect(my_object, QtCore.SIGNAL('error(QProcess::ProcessError)'), my_callback)

    # Qt5 Code:
    my_object.error.connect(my_callback)

    # Cute Code:
    cute.connect(my_object, 'error(QProcess::ProcessError)', my_callback)

The API for disconnecting is the same, just use the
``cute.disconnect(...)`` function.

Form to Widget
~~~~~~~~~~~~~~

IDA has 2 APIs for getting the widget associated with a TForm. One for
PyQt and one for PySide. Cute wraps them both in one function.

::

    my_widget = cute.form_to_widget(my_tform)

Which Qt Should I Use?
~~~~~~~~~~~~~~~~~~~~~~

Sometimes, you *do* need to to know the Qt version your code uses. For
those cases, ask the ``use_qt5`` variable.

::

    if cute.use_qt5:
        print 'Use Qt5'
    else:
        print 'Use Qt4'

In a Project
~~~~~~~~~~~~

The recommended way to use Cute is to copy it into your own project.

Licensing
---------

Cute is released under the MIT license, so you are free to use it in any
project whatsoever.

FAQ
---

**Q:** Why is this not on PyPI? Why is there no ``setup.py``?

**A:** This project was separated from Sark to enable dependency-free
usage. It is meant to be used in a copy-paste fashion (yes, this is
evil. But a necessary evil.)

**Q:** Why did you name it "cute"?

**A:** For years I was sure "Qt" is pronounced "Q T". This is my effort
to remind myself it is not.
