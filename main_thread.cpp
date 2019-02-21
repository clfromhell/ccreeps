#include <iostream>
#include <thread>
#include <string>
using namespace std;

/*
 * Start point for ccreeps -> starts class threads and map
 * I thought of different classes, all handled by their own thread, while one
 * map handled by one thread but talking to the class threads
 *
 * different start modes possible:
 * - probably start with reduced threads
 * - etc.
 *
 */

int main(int argc, char *argv[]) { //args for future use
    cout << argv[1] << endl;
}