# Initialize the dict status
dictStatus = {
    "Requested": "Requested",
    "Missing info": "Missing info",
    "Processed": "Processed",
    "Activated": "Activated",
    "Canceled": "Canceled",
}


def status(*sub_status):
    """
    Returns the general status according to sub-status
    """

    if dictStatus["Missing info"] in sub_status:
        # If a subtask has a status of Missing info, the general task also has this status.
        return dictStatus["Missing info"]

    elif dictStatus["Processed"] in sub_status:
        # If a subtask has a status of Processed, the general task also has this status.
        return dictStatus["Processed"]

    elif len(set(sub_status)) == 1:
        # If all subtasks have the same status, the general task also has this status.
        return sub_status[0]

    elif all(
        i == dictStatus["Activated"] or i == dictStatus["Canceled"]
        for i in set(sub_status)
    ):
        # The general task state is Activated only if all sub-states are Activated or Canceled.
        return dictStatus["Activated"]

    else:
        # In all other cases, the general task status is Requested.
        return dictStatus["Requested"]


print(status("Requested", "Requested", "Requested"))
print(status("Activated", "Processed", "Canceled"))
print(status("Activated", "Missing info", "Canceled"))
print(status("Activated", "Activated", "Canceled"))
