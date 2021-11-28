sample_output = \
"""  native-path:          /sys/devices/pci0000:00/0000:00:14.0/usb1/1-3/1-3:1.0/usbmisc/hiddev0
  vendor:               American Power Conversion
  model:                Back-UPS NS 1500M2
  serial:               3B2001X20153  
  power supply:         yes
  updated:              Sun 28 Nov 2021 12:43:25 AM UTC (37 seconds ago)
  has history:          yes
  has statistics:       yes
  ups
    present:             yes
    state:               fully-charged
    warning-level:       none
    time to empty:       38.8 minutes
    percentage:          100%
    icon-name:          'battery-full-charged-symbolic'"""


import util

parsed = util.parse_battery_output(sample_output)

assert parsed['charge'] == 1.0
assert parsed['time-remaining'] == 2328