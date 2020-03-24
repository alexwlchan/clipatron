#!/usr/bin/env python3
"""
This is a script for splitting video clips using ffmpeg.

It takes a path to a video and a CSV file as input.  The CSV must have
at least three (named) columns:

    filename,start_time,duration
    scene_1.mp4,01:00,00:30         # creates a clip starting at 01:00, 30 seconds long
    scene_2.mp4,02:31,00:25         # creates a clip starting at 02:31, 25 seconds long

Any extra columns in the CSV will be ignored.

"""

from __future__ import print_function

import argparse
import subprocess
import csv
import sys


def ffmpeg(*args):
    try:
        subprocess.check_call(["ffmpeg"] + list(args))
    except subprocess.CalledProcessError as err:
        print("Something went wrong: %r" % err, file=sys.stderr)
        print("Do you have ffmpeg installed?", file=sys.stderr)
        sys.exit(1)


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="A script for clipping videos using ffmpeg."
    )
    parser.add_argument(
        "--input", dest="VIDEO", help="Path to the video file to clip", required=True
    )
    parser.add_argument(
        "--manifest",
        dest="CSV_MANIFEST",
        help="Path to the CSV file describing the clips to create",
        required=True,
    )
    return parser.parse_args(argv)


def get_rows(csv_manifest_path):
    with open(csv_manifest_path) as infile:
        reader = csv.DictReader(infile)

        # Start at 2 because spreadsheet programs number their rows starting at 1,
        # and then the header is row 1
        for row_number, row in enumerate(reader, start=2):
            try:
                start_time = row["start_time"]
                duration = row["duration"]
                filename = row["filename"]
            except KeyError as err:
                print(
                    "Row %d in your CSV is missing a required column: %r" %
                    (row_number, err), file=sys.stderr
                )
                sys.exit(1)

            for (value, column_name) in [
                (start_time, "start_time"),
                (duration, "duration"),
                (filename, "filename")
            ]:
                if not value:
                    print(
                        "Row %d in your CSV has an empty value for %s!" %
                        (row_number, column_name), file=sys.stderr
                    )
                    sys.exit(1)

            yield (start_time, duration, filename)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])

    for (start_time, duration, filename) in get_rows(args.CSV_MANIFEST):
        ffmpeg(
            "-ss", start_time,
            "-i", args.VIDEO,
            "-t", duration,
            "-vcodec", "copy",
            "-an", filename
        )
