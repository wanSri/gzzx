from zx.models import Equ


class EquController(object):
    @classmethod
    def get_querySet(cls, params):
        results = Equ.objects.all()
        return results
