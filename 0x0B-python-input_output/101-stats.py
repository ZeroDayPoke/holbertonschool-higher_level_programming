#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>]
"GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
Total file size: File size: <total size>
where is the sum of all previous (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""
import sys

"""init metrics"""
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    """read from STDINFILENO"""
    for line in sys.stdin:
        """tokenize, get size and status"""
        parts = line.split()
        size = int(parts[-1])
        status = int(parts[-2])

        """update counts"""
        total_size += size
        status_counts[status] += 1
        line_count += 1

        """print every 10 lines"""
        if line_count % 10 == 0:
            print(f'Total file size: {total_size}')
            for code in sorted(status_counts.keys()):
                if status_counts[code] > 0:
                    print(f'{code}: {status_counts[code]}')

except KeyboardInterrupt:
    """print balance after SIGINT"""
    print(f'Total file size: {total_size}')
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f'{code}: {status_counts[code]}')
