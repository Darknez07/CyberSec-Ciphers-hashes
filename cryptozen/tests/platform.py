import sys

plt = sys.platform
if plt.startswith("linux"):
    sys.path.insert(0, "/".join(sys.path[0].split("/")[:-1]) + "/cryptozen")
elif plt.startswith("win"):
    sys.path.insert(0, "\\".join(sys.path[0].split("\\")[:-1]) + "\\cryptozen")
