#include <iostream>
#include "hello.h"

int main() {
    hello();
    #if NDEBUG
        std::cout<<"*** RELEASE***\n";
    #else
       std::cout<<"*** DEBUG***\n";
    #endif
}
