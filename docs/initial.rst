=================
Initial Condition
=================

WMOC employed WNTRSimulators_ for simulating the steady state
in the network to establish the initial flow conditions for
the upcoming transient simulations.

.. _WNTRSimulators: https://wntr.readthedocs.io/en/latest/index.html

**WNTRSimulators** can be used to run demand-driven (DD) or 
pressure dependent demand (PDD) hydraulics simulations. The 
default simulation engine is DD. The initial condition simulation
can be run using the following code::

.. literalinclude:: ../examples/Tnet1_valve_closure.py
    :lines: 25-27

:math:`t0` stands for the time when the initial condition will be 
calculated.