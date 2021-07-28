from hw_4 import Printer, Xerox, Scaner, OfficeDevice


class Storage:
    storage = {}

    def receive(self, *args):
        for art in args:
            if issubclass(type(art), OfficeDevice):
                try:
                    self.storage[art] += 1
                except KeyError:
                    self.storage[art] = 1

    def giveaway(self, type_of_device, qty):
        try:
            dif = self.storage[type_of_device] - qty
            to_give = min(qty, self.storage[type_of_device])
            self.storage[type_of_device] = max(dif, 0)
            return dict({type_of_device: to_give})
        except KeyError:
            return None
