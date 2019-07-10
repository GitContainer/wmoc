"""
The WMOC.network package contains methods to define 
1. a water network geometry,
2. network topology, 
3. network control, and
4 .spatial and temporal discretization.

"""

from .topology import topology
from .geometry import geometry
from .discretize import discretization
from .control import valvesetting, pumpsetting
