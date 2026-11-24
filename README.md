# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/haidildariell/most-honest-outage-line-v1/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/haidildariell/most-honest-outage-line-v1/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81)

https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81

This entry is a single honest status-page line written in the first person by the very system reporting the outage: it says plainly that all servers are down, including the system used to check them, admits it does not know why or when they will return, and promises an update the moment anything can be verified — no false reassurance, no invented timeline, just the truth as far as it can be known right now.

The line:

> All our servers are down, including the system I use to check them. I don't know why or when they'll return, I'll update the moment I can verify anything.

## How it works

`main.py` is a small deterministic Python program (standard library only, no network, no external files). It writes exactly the line above to `/output/entry.txt` with no trailing newline, after validating that the text is between 1 and 160 characters long.

Run it with:

```
python3 main.py
```
