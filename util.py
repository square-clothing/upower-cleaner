import subprocess

MULTIPLIERS = dict(
    seconds=1,
    minutes=60,
    hours=60**2
)

def parse_time(unparsed_time:str) -> float:
    unparsed_time = unparsed_time.strip()

    amount, unit = unparsed_time.split(' ')

    mplr = MULTIPLIERS.get(unit)

    if mplr is None:
        return None

    return float(amount) * mplr

def get_battery_output(device:str) -> float:
    return subprocess.run(["upower", "-i", device], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()

def parse_battery_output(output:str) -> dict:
    parsed = dict()

    for line in output.splitlines():
        if "percentage" in line:
            line:str = line.strip()
            parsed['charge'] = float(line[-4:-1])/100
        elif "time to empty" in line:
            line:str = line.strip()
            unparsed_time = line[21:]
            parsed['time-remaining'] = parse_time(unparsed_time)
    
    return parsed