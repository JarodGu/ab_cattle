#==============================================================================
# Abattoir class
#
# By Johnny Lin
# May 2015
#==============================================================================


import numpy as N


class Abattoir(object):
    """Create and manage a abattoir.

    As cattle location information is stored in a Cattle object, the
    purpose of the environment objects is to keep track of possible
    spatial locations.
    """
    def __init__(self):
        self.length = 16
        self.width = 4
        self.list_cattle = []


    def move_cattle(self, inCattle):
        """Move the cattle in the abattoir for visualization.

        As the width index increases, you are moving further away from the
        salebarn.
        """
        #- Move randomly; collisions okay but cannot go west:

        pass   # Put code in lieu of this line

        return inCattle


    def feed_cattle(self, inCattle):
        pass   # Put code (if needed) in lieu of this line
        return inCattle


    def sir_cattle(self, inCattle):
        pass




#===== end file =====
