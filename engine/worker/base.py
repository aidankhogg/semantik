from abc import ABC, abstractmethod
from typing import List
from uuid import uuid4


class Foreman:  # TODO: Turn to hostbased singleton?
    """
    Worker management
    """

    def __init__(self):
        self.worker_pool: List[BaseWorker] = []


class BaseWorker(ABC):
    """
    Base class for workers.
    """

    def __init__(self, **kwargs):
        """
        :param kwargs: meta: (optional) - Dictionary for metadata

        """
        # Establish Metadata
        self._meta = {
            "uid": str(uuid4()),
            "worker_type": "unknown"
        }

        if any(key in kwargs for key in ['meta', 'metadata', 'md']):
            matching_key = next((key for key in ['meta', 'metadata', 'md'] if key in kwargs.keys()), None)
            if matching_key:
                for key, value in kwargs[matching_key].items():
                    self._meta[key] = value

    @property
    def metadata(self):
        return self._meta


class Worker(BaseWorker):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._meta['worker_type'] = 'generic'


class BaseTask(ABC):
    pass


class Task(BaseTask):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._subtasks: List[SubTask] = []


class SubTask(Task):
    pass


class Job(ABC):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._tasks: List[Task] = []


class BaseWorkOrder(ABC):
    pass


class WorkOrder(BaseWorkOrder):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._jobs: List[Job] = []
