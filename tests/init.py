import re

from spec import Spec, eq_

import invoke
import invoke.tasks
import invoke.runner


class Init(Spec):
    "__init__"
    def dunder_version_info(self):
        assert hasattr(invoke, '__version_info__')
        ver = invoke.__version_info__
        assert isinstance(ver, tuple)
        assert all(isinstance(x, int) for x in ver)

    def dunder_version(self):
        assert hasattr(invoke, '__version__')
        ver = invoke.__version__
        assert isinstance(ver, basestring)
        assert re.match(r'\d+\.\d+\.\d+', ver)
    
    def dunder_version_looks_generated_from_dunder_version_info(self):
        # Meh.
        ver_part = invoke.__version__.split('.')[0]
        ver_info_part = invoke.__version_info__[0]
        eq_(ver_part, str(ver_info_part))

    def exposes_task_decorator(self):
        assert invoke.task is invoke.tasks.task

    def exposes_run_function(self):
        assert invoke.run is invoke.runner.run
