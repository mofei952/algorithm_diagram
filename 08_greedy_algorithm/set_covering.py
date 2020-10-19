# 要覆盖的州
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# 可供选择的广播台清单
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# 存储最终选择的广播台
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    states_needed -= states_covered
    stations.pop(best_station)

print(final_stations)
