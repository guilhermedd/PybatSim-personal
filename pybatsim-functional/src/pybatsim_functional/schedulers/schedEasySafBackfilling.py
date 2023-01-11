"""
    schedEasySafBackfill
    ~~~~~~~~~~~~~~~~~~~~

    Shortest-job-first backfilling algoritihm using the pre-defined algorithm
    of the new scheduler api.
"""

from pybatsim_functional.algorithms.backfilling import backfilling_sched
from pybatsim_functional.algorithms.utils import consecutive_resources_filter
from pybatsim_functional.scheduler import as_scheduler, adapt_functional_scheduler


def _func_SchedEasySafBackfill(scheduler):
    kwargs = {}

    kwargs["reservation_depth"] = scheduler.options.get(
        "backfilling_reservation_depth", 1)

    strategy = scheduler.options.get("backfilling_strategy", "Saf")
    if strategy == "Saf":
        kwargs["backfilling_sort"] = lambda j: j.requested_time * j.requested_resources
    else:
        raise NotImplementedError(
            "Unimplemented backfilling strategy: {}".format(strategy))

    backfilling_sched(
        scheduler,
        resources_filter=consecutive_resources_filter,
        **kwargs)


SchedEasySafBackfill = adapt_functional_scheduler(
    as_scheduler()(
        _func_SchedEasySafBackfill
    )
)
