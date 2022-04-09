import sys

import pytest

import software.python_bindings as tbots
from proto.primitive_pb2 import maxallowedspeedmode
from proto.tactic_pb2 import assignedtacticplaycontrolparams, chiptactic, tactic
from software.simulated_tests.robot_enters_region import *
from software.simulated_tests.ball_enters_region import *
from software.simulated_tests.ball_moves_forward import *
from software.simulated_tests.friendly_has_ball_possession import *
from software.simulated_tests.ball_speed_threshold import *
from software.simulated_tests.robot_speed_threshold import *
from software.simulated_tests.excessive_dribbling import *
from software.simulated_tests.simulated_test_fixture import tactic_runner

@pytest.mark.parametrize(
    "params go here",
    [
        # Write tests here 
    ]

)
def chip_testing("""params go here""", tactic_runner):
    # Setup Robot

    # Setup Tactic

    # Other stuff...
    pass

if __name__ == '__main__':
    sys.exit(pytest.main([__file__, "-svv"]))
