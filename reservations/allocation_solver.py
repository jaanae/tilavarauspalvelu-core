from applications.models import ApplicationEvent
from reservation_units.models import ReservationUnit


class AllocationSolver(object):

    def __init__(self, application_events: [ApplicationEvent], reservation_unit: ReservationUnit):
        self.__reservation_unit = reservation_unit
        self.__application_events = application_events


