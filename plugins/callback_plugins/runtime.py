from __future__ import (absolute_import, division, print_function)
from datetime import datetime
from ansible.plugins.callback import CallbackBase
__metaclass__ = type


class CallbackModule(CallbackBase):
    """
    Shows current time and how long your each play ran for.
    """
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'aggregate'
    CALLBACK_NAME = 'runtime'
    CALLBACK_NEEDS_WHITELIST = False

    def __init__(self):
        super(CallbackModule, self).__init__()
        self.start_time = datetime.now()

    def time_hours_minutes_seconds(self, runtime):
        minutes = (runtime.seconds // 60) % 60
        r_seconds = runtime.seconds - (minutes * 60)
        current_time = datetime.now()
        return current_time, runtime.seconds // 3600, minutes, r_seconds

    def v2_on_any(self, *args, **kwargs):
        end_time = datetime.now()
        runtime = end_time - self.start_time
        self._display.display("[%s] - %sh %sm %ss" % (self.time_hours_minutes_seconds(runtime)))
