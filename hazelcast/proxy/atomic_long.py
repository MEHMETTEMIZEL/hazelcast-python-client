from hazelcast.protocol.codec import atomic_long_add_and_get_codec, atomic_long_compare_and_set_codec, \
    atomic_long_decrement_and_get_codec, atomic_long_get_and_add_codec, atomic_long_get_and_increment_codec, \
    atomic_long_get_and_set_codec, atomic_long_get_codec, atomic_long_increment_and_get_codec, atomic_long_set_codec
from hazelcast.proxy.base import PartitionSpecificProxy


class AtomicLong(PartitionSpecificProxy):
    def add_and_get(self, delta):
        return self._encode_invoke_on_partition(atomic_long_add_and_get_codec, name=self.name, delta=delta)

    def compare_and_set(self, expected, updated):
        return self._encode_invoke_on_partition(atomic_long_compare_and_set_codec, name=self.name, expected=expected,
                                                updated=updated)

    def decrement_and_get(self):
        return self._encode_invoke_on_partition(atomic_long_decrement_and_get_codec, name=self.name)

    def get(self):
        return self._encode_invoke_on_partition(atomic_long_get_codec, name=self.name)

    def get_and_add(self, delta):
        return self._encode_invoke_on_partition(atomic_long_get_and_add_codec, name=self.name, delta=delta)

    def get_and_set(self, new_value):
        return self._encode_invoke_on_partition(atomic_long_get_and_set_codec, name=self.name, new_value=new_value)

    def increment_and_get(self):
        return self._encode_invoke_on_partition(atomic_long_increment_and_get_codec, name=self.name)

    def get_and_increment(self):
        return self._encode_invoke_on_partition(atomic_long_get_and_increment_codec, name=self.name)

    def set(self, new_value):
        return self._encode_invoke_on_partition(atomic_long_set_codec, name=self.name, new_value=new_value)

    def __str__(self):
        return "AtomicLong(name=%s)" % self.name
