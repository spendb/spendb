from babbage.manager import CubeManager

from spendb.core import db
from spendb.model.dataset import Dataset


class SpendingCubeManager(CubeManager):
    """ This enables the babbage API to find and query SpenDB datasets """

    def __init__(self):
        pass

    def has_cube(self, name):
        dataset = Dataset.by_name(name)
        if dataset is None:
            return False
        return dataset.model is not None

    def get_cube_model(self, name):
        dataset = Dataset.by_name(name)
        if dataset is None or dataset.model is None:
            return None
        return dataset.model.to_dict()

    def get_engine(self):
        return db.engine

    def list_cubes(self):
        # TODO: authz, failing conservatively for now.
        for dataset in Dataset.all_by_account(None):
            if dataset.model is not None:
                yield dataset.name
