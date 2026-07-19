import click
import datetime
import sys
import time
import zoneinfo


@click.command(name="live-clock", help="Live, constantly updating clock. Close with Ctrl+C or Ctrl+\\ (as you would to exit any other command).")
@click.option("--format", "-f", type=str, default="%Y/%m/%d %H:%M:%S.%f %z", help="Time format, as you would do with Python's time.strftime() function. For advanced users. The default option already shows everything you need.")
@click.option("--timezone", "-z", type=str, default="America/New_York", help="Time zone key. Uses codes like 'UTC' and 'America/New_York'.")
@click.option("--update-interval", "-i", type=float, default=0.1, help="Number of seconds between updates. Sometimes you may need to pick a higher number on older computers. Default is 0.1 seconds.")
def main(format, timezone, update_interval):
    while True:
        sys.stdout.write("\r")
        sys.stdout.write(datetime.datetime.now(zoneinfo.ZoneInfo(timezone)).strftime(format))
        sys.stdout.flush()
        time.sleep(update_interval)


if __name__ == "__main__":
    sys.exit(main())
