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