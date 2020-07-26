from .CATH import Cath


def load(manager, params):
    """
    Create an launch a new instance of CATH.
    """
    # default position
    pos = (-15, -15)

    if params is not None and len(params) > 0:
        pos = params[0]
    try:
        
        Cath(pos, manager)
    except: Exception    
