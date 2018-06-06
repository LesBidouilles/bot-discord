import re


_time_regex = re.compile(
    r'(?:(?P<hours>\d+)h)? *(?:(?P<minutes>\d+)m)? *(?:(?P<seconds>\d+)s)?$')


def parseTime(content):
    """
    Returns the specified time in seconds

    The time must be specified at the end of the content
    """
    parsed = _time_regex.search(content)

    time = 0

    if parsed:
        hours, minutes, seconds = parsed.group('hours', 'minutes', 'seconds')

        hours = int(hours) if hours else 0
        minutes = int(minutes) if minutes else 0
        seconds = int(seconds) if seconds else 0

        time = 60 * 60 * hours + 60 * minutes + seconds

    return time
