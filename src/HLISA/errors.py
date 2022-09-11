class HLISAException(Exception):
  """ Base class of all exception classes used by HLISA.
  """
  pass
        
class OutOfViewportException(HLISAException):
  """ Indicates failing interaction due to leaving of the viewport
  """
  pass

class ElementBoundariesWereZeroException(HLISAException):
  """ Indicates that either the height or width of an element was zero
  """
  pass

class UnscrollableElementException(HLISAException):
  """ Indicates failing interaction due to leaving of the viewport
  """
  pass

class IllegalArgumentException(HLISAException):
  """ Indicates failing to provide legal arguments to a function
  """
  pass

class NoCursorCoordinatesException(HLISAException):
  """ An exception occured while retrieving the cursor location. 
      This should not happen, please file an issue if it did: https://github.com/droefs/HLISA/issues
  """
  pass
