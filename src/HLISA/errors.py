class HLISAException(Exception):
  """ Base class of all exception classes used by HLISA.
  """
  pass
        
class OutOfViewportException(HLISAException):
  """ Indicates failing interaction due to leaving of the viewport
  """
  pass
