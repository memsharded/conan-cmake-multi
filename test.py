import os, shutil
import platform

def run(command):
	ret = os.system(command)
	if ret != 0:
	    raise Exception("Command %s" % command)

run("conan export memsharded/testing")
"""os.chdir("test")
shutil.rmtree("build")
os.makedirs("build")
os.chdir("build")
run("conan install .. -s build_type=Debug --build=missing")
run("conan install .. -s build_type=Release --build=missing")
run('cmake .. -G "Visual Studio 14 Win64"')
run("cmake --build . --config Release")
run("cd bin && example")
run("cmake --build . --config Debug")
run("cd bin && example")
"""

os.chdir("test_boost_poco")
try:
	shutil.rmtree("build")
except:
	pass
os.makedirs("build")
os.chdir("build")
install_debug_options = '-s compiler="Visual Studio" -s compiler.runtime="MDd"' if platform.system() == "Windows" else ""
run("conan install .. -s build_type=Debug %s --build=missing" % install_debug_options)
run("conan install .. -s build_type=Release --build=missing")
run('cmake .. -G "Visual Studio 14 Win64"')
run("cmake --build . --config Release")
run("cd bin && example")
run("cmake --build . --config Debug")
run("cd bin && example")
