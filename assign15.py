import gc
import time
import tracemalloc


class Node:
    def __init__(self, value):
        self.value = value
        self.ref = None


def create_cycles(count):
    nodes = []
    for i in range(count):
        node = Node(i)
        node.ref = node
        nodes.append(node)
    return nodes


print("Garbage collection thresholds:", gc.get_threshold())

collected = gc.collect()
print("Objects collected at start:", collected)

tracemalloc.start()
start_snapshot = tracemalloc.take_snapshot()

nodes = create_cycles(1000)
print("Created 1000 reference cycles.")

del nodes

end_snapshot = tracemalloc.take_snapshot()
memory_before = sum(stat.size for stat in end_snapshot.compare_to(start_snapshot, "filename"))
print("Memory held by unreachable cycles (bytes):", memory_before)

collected = gc.collect()
print("Objects collected by manual garbage collection:", collected)

final_snapshot = tracemalloc.take_snapshot()
memory_after = sum(stat.size for stat in final_snapshot.compare_to(start_snapshot, "filename"))
print("Memory difference after collection (bytes):", memory_after)
tracemalloc.stop()

gc.disable()
start_time = time.time()
nodes = create_cycles(100000)
del nodes
disabled_time = time.time() - start_time
print("Time to allocate 100000 cycles with garbage collection disabled:", round(disabled_time, 4), "seconds")

gc.enable()
collected = gc.collect()
print("Objects collected after re-enabling garbage collection:", collected)

start_time = time.time()
nodes = create_cycles(100000)
del nodes
gc.collect()
enabled_time = time.time() - start_time
print("Time to allocate and collect 100000 cycles with garbage collection enabled:", round(enabled_time, 4), "seconds")
