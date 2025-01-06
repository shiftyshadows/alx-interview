#!/usr/bin/python3
import sys
import signal
import re

# Initialize metrics
file_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0


def print_metrics():
    """Print the metrics collected so far."""
    print(f"File size: {file_size}")
    for status_code in sorted(status_counts):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")


def process_line(line):
    """Process a single line to extract metrics."""
    global file_size

    # Regex to match the required format
    pattern = r'^(\S+) - \[(.*?)\] \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)$'
    match = re.match(pattern, line)

    if not match:
        return

    # Extract status code and file size
    status_code = int(match.group(3))
    size = int(match.group(4))

    # Update metrics
    file_size += size
    if status_code in status_counts:
        status_counts[status_code] += 1


def signal_handler(sig, frame):
    """Handle the keyboard interruption to print metrics."""
    print_metrics()
    sys.exit(0)

# Register signal handler for Ctrl + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        process_line(line.strip())
        line_count += 1

        # Print metrics after every 10 lines
        if line_count % 10 == 0:
            print_metrics()

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)

# Print final metrics on EOF
print_metrics()
