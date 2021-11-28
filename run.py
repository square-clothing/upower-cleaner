# Parse Arguments

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('upower_device')

parser.add_argument('--host', default='127.0.0.1')
parser.add_argument('--port', type=int, default=80)

args = parser.parse_args()

# Routing

import util
import sanic

app = sanic.Sanic(__name__)

@app.get('/')
def info(request:sanic.Request):
    upower_output = util.get_battery_output(args.upower_device)

    parsed_output = util.parse_battery_output(upower_output)
    parsed_output['upower-output'] = upower_output

    return sanic.json(parsed_output)

# Run

if __name__ == '__main__':
    app.run(
        host=args.host,
        port=args.port
    )