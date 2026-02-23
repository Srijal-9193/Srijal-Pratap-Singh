try:
	import importlib
	plt = importlib.import_module("matplotlib.pyplot")
except ImportError:
	import sys
	import subprocess
	subprocess.check_call([sys.executable, "-m", "pip", "install", "matplotlib"])
	import importlib
	plt = importlib.import_module("matplotlib.pyplot")

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [30, 32, 31, 33, 34, 35, 36]

plt.plot(days, temperature)
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature Report")
plt.show()

