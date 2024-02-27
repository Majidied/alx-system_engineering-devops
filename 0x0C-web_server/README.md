**0x0C-web_server** is a simple and lightweight web server written in C. It is designed to be easy to use and understand, and it can be used to serve static content or to proxy requests to another server.

**Features:**

* Serves static content from a specified directory
* Proxies requests to another server
* Supports GET and HEAD methods
* Handles 404 Not Found and 405 Method Not Allowed errors
* Customizable port number and root directory

**Usage:**

To use the web server, simply compile the source code using a C compiler and run the executable. By default, the server listens on port 8080 and serves content from the current working directory. You can customize the port number and root directory by modifying the source code.

**Example:**

```
$ gcc 0x0C-web_server.c -o 0x0C-web_server
$ ./0x0C-web_server
```

This will start the web server on port 8080 and serve content from the current working directory.

**Customization:**

You can customize the port number and root directory by modifying the following lines in the source code:

```
#define PORT 8080
#define ROOT_DIR "."
```

**Limitations:**

This web server is intended for educational purposes only and may not be suitable for production environments. It lacks many features found in modern web servers, such as support for dynamic content generation, HTTPS encryption, and advanced security features.

**Feedback:**

If you encounter any issues or have any feedback, please feel free to open an issue on the GitHub repository. Thank you for using 0x0C-web_server!