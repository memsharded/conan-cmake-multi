from conans import ConanFile, CMake
import os


channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "memsharded")


class CMakeMultiGenTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "Boost/1.60.0@lasote/stable", "Poco/1.7.2@lasote/stable", "CMakeMultiGen/0.1@%s/%s" % (username, channel)
    generators = "cmakemulti"
    default_options="""Boost:shared=False
Poco:shared=False"""

    def imports(self):
        self.copy("*.dll", "bin", "bin")
        self.copy("*.dylib", "bin", "bin")

