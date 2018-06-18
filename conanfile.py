from conans import ConanFile, CMake, tools


class AddConan(ConanFile):
    name = "Add"
    version = "0.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Add here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    scm = {
        "type": "git",
        "subfolder": "src",
        "url": "auto",
        "revision": "auto"
    }

#    def source(self):
#        self.run("git clone https://github.com/memsharded/hello.git")
#        self.run("cd hello && git checkout static_shared")
#        # This small hack might be useful to guarantee proper /MT /MD linkage
#        # in MSVC if the packaged project doesn't have variables to set it
#        # properly
#        tools.replace_in_file("hello/CMakeLists.txt", "PROJECT(MyHello)",
#                              '''PROJECT(MyHello)
#include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
#conan_basic_setup()''')
#
    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["add"]

