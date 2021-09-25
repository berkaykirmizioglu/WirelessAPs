old_ssids = [""]
new_ssids = [""]


def __find_ssid_diffs(previous, current):
    if len(previous) != len(current):
        print("----------There are some adds/removes!----------")
    for x in previous:
        old_ssids.append(x["ssid"])
    for y in current:
        new_ssids.append(y["ssid"])
    return set(new_ssids) - set(old_ssids)


def __print_deleted_ssid(previous, current):
    deleted = set(previous) - set(current)
    if deleted != set():
        print(deleted, "is removed from the list!")


def __detect_access_points_changes(previous, current, diffs):
    for y in current:
        old_ssids.append(y["ssid"])
        if y["ssid"] in diffs:
            print(y["ssid"], "is added to the list with SNR", y["snr"], "and channel", y["channel"])
        for x in previous:
            if x["ssid"] == y["ssid"]:
                new_ssids.append(x["ssid"])
                if x["snr"] != y["snr"]:
                    print(x["ssid"] + "'s SNR changed", x["snr"], " to ", y["snr"])
                if x["channel"] != y["channel"]:
                    print(x["ssid"] + "'s Channel changed", x["channel"], " to ", y["channel"])


def alert_changes(dict1: dict, dict2: dict):
    previous_access_points = dict1.get("access_points")
    current_access_points = dict2.get("access_points")

    diffs = __find_ssid_diffs(previous_access_points, current_access_points)

    __print_deleted_ssid(previous=old_ssids, current=new_ssids)
    __detect_access_points_changes(previous_access_points, current_access_points, diffs)
