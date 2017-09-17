from unit6.plugins.keys import get_key_class
from unit6.models import db, Keys

class BaseChallenge(object):
    id = None
    name = None

class unit6StandardChallenge(BaseChallenge):
    id = 0
    name = "standard"

    @staticmethod
    def solve(chal, provided_key):
        chal_keys = Keys.query.filter_by(chal=chal.id).all()
        for chal_key in chal_keys:
            if get_key_class(chal_key.key_type).compare(chal_key.flag, provided_key):
                return True
        return False


CHALLENGE_CLASSES = {
    0 : unit6StandardChallenge
}

def get_chal_class(class_id):
    cls = CHALLENGE_CLASSES.get(class_id)
    if cls is None:
        raise KeyError
    return cls