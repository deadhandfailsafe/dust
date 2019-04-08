import random

entity_id_max = 99999


class Entity():
    def __init__(self, box):
        eid = Entity.create_eid()
        eid_taken = False
        while eid_taken is False:
            check = Entity.check_eid(eid, box)
            if check is True:
                eid = Entity.create_eid()
            else:
                break
        self.eid = eid

    @staticmethod
    def check_eid(eid, box):
        check_eid_i = 0
        while check_eid_i < len(box):
            if eid == box[check_eid_i].eid:
                return True
            check_eid_i += 1
        return False

    @staticmethod
    def create_eid():
        return random.randint(0, entity_id_max)
