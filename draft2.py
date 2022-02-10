from datetime import datetime
from typing import List, Optional, Union, Tuple
from collections import Counter


def sum_light(els: List[Union[datetime, Tuple[datetime, int]]],
              start_watching: Optional[datetime] = None,
              end_watching: Optional[datetime] = None):
    for i in els:
        if isinstance(i, datetime):
            els[els.index(i)] = (i, 1)

    if start_watching:
        for i in els:
            if start_watching > i[0]:
                els[els.index(i)] = (start_watching, els[els.index(i)][1])

    if end_watching:
        if len(els) % 2 == 1:
            els.append((end_watching, [k for k, v in Counter([i[1] for i in els]).items() if v % 2 == 1][0]))
        for i in els:
            if end_watching < i[0]:
                els[els.index(i)] = (end_watching, els[els.index(i)][1])

    result = [els[0][0].replace(microsecond=0), ]
    bulb_numbers_started = [els[0][1]]
    for i in els[1:]:
        bulb_numbers_started.append(i[1])
        if bulb_numbers_started.count(i[1]) % 2 == 1 and isinstance(result[-1], float):
            result.append(i[0].replace(microsecond=0))
        elif bulb_numbers_started.count(i[1]) % 2 == 0\
                and all(j % 2 == 0 for j in Counter(bulb_numbers_started).values()):
            result[-1] = (i[0].replace(microsecond=0) - result[-1]).total_seconds()

    if isinstance(result[-1], datetime):
        result[-1] = (els[-1][0].replace(microsecond=0) - result[-1]).total_seconds()
    return int(sum(result))
    # return result


print(sum_light([
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
        datetime(2015, 1, 12, 10, 0, 40),
        (datetime(2015, 1, 12, 10, 0, 50), 2),
    ], datetime(2015, 1, 12, 10, 0, 50)))

print(sum_light([
        (datetime(2015, 1, 12, 10, 0, 10), 3),
        datetime(2015, 1, 12, 10, 0, 20),
        (datetime(2015, 1, 12, 10, 0, 30), 3),
        (datetime(2015, 1, 12, 10, 0, 30), 2),
    ], datetime(2015, 1, 12, 10, 0, 10), datetime(2015, 1, 12, 10, 0, 20)))
