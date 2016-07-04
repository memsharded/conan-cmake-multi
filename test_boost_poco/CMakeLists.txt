PROJECT(PackageTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo_multi.cmake)
conan_basic_setup()

ADD_EXECUTABLE(example example.cpp)
TARGET_LINK_LIBRARIES(example debug ${CONAN_LIBS_DEBUG}
                              optimized ${CONAN_LIBS_RELEASE})
