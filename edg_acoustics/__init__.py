"""Documentation about edg_acoustics (in init.py file)."""

import logging
from .acoustics_simulation import AcousticsSimulation
from .mesh import Mesh
from .boundary_condition import BoundaryCondition, AbsorbBC
from .initial_condition import InitialCondition, Monopole_IC
from .preprocessing import Flux, UpwindFlux
from .time_integration import TimeIntegrator, TSI_TI
from .postprocessing import Monopole_postprocessor

logging.getLogger(__name__).addHandler(logging.NullHandler())

__author__ = "Huiqing Wang, Artur Palha"
__email__ = "h.wang6@tue.nl, A.Palha@tudelft.nl"
__version__ = "1.0.0-alpha.1"
