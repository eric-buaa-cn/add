cmake_minimum_required(VERSION 2.6)
project(add)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(add add.cpp)
