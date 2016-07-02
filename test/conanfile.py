from conans import ConanFile, CMake
import os


channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "memsharded")


class CMakeMultiGenTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "Hello/0.1@memsharded/testing", "CMakeMultiGen/0.1@%s/%s" % (username, channel)
    generators = "cmakemulti"

    def imports(self):
        self.copy("*.dll", "bin", "bin")
        self.copy("*.dylib", "bin", "bin")

