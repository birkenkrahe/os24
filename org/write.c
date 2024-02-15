#include <stdio.h>
#include <unistd.h>






int main() {
const char *msg = "Hello World!\n"; // msg has 13 bytes
ssize_t bytes written;

// write message to stdout (file descriptor 1)
bytes_written = write(1, msg, 13));

if (bytes_written == -1) {
  // if write returns -1, an error occurred
  write(2, "An error occurred\n", 18); // error message to stderr
  exit(1); // exit with error code
 }

return 0; // exit normally
}
return 0;
}
