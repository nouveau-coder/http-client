# HTTP Client

## Overview

This project is a Python-based HTTP client built using Python's standard `socket` library. It resolves a hostname, establishes a TCP connection to port 80, sends a raw HTTP/1.1 GET request, and receives the server's response.

The project is designed to provide hands-on experience with DNS, TCP, and HTTP fundamentals without relying on high-level HTTP libraries.

## Features

* Resolves a hostname to its IPv4 address.
* Establishes a TCP connection to port 80.
* Constructs and sends HTTP/1.1 GET requests manually.
* Includes the target hostname in the HTTP request.
* Receives and displays up to 1024 bytes of the server's response.
* Provides a command-line interface using `argparse`.
* Handles DNS, connection, timeout, and socket errors.

## Requirements

* Python 3.10+

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone ...
cd http-client
```

## Usage

Run the client using:

```bash
python client.py <host_name>
```

### Arguments

* `host_name` – Hostname of the target server.

### Example

```bash
python client.py example.com
```

This command resolves `example.com`, establishes a TCP connection to port 80, sends an HTTP GET request for the root resource, and displays the beginning of the server's response.

## Example Output

```text
>>> python client.py example.com connection successfully established HTTP/1.1 200 OK Date: Fri, 31 Jul 2026 10:25:12 GMT Content-Type: text/html Transfer-Encoding: chunked Connection: keep-alive Server: cloudflare Last-Modified: Mon, 20 Jul 2026 07:16:20 GMT Allow: GET, HEAD Accept-Ranges: bytes Age: 10794 cf-cache-status: HIT CF-RAY: a23be5d80e3b3c01-BLR 22f <!doctype html><html lang="en"><head><title>Example Domain</title><link rel="icon" href="data:,"><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{background:#eee;width:60vw;margin:15vh auto;font-family:system-ui,sans-serif}h1{font-size:1.5em}div{opacity:0.8}a:link,a:visited{color:#348}</style></head><body><div><h1>Example Domain</h1><p>This domain is for use in documentation examples without needing permission. Avoid use in operations.</p><p><a href="https://iana.org/domains/example">Learn more</a></p></div></body></html> 0
```

## Project Structure

```text
http-client/
│
├── client.py
├── README.md
└── LICENSE
```

## Future Improvements

* Read responses larger than the current 1024-byte limit.
* Separate and parse the HTTP status line, headers, and body.
* Add support for methods such as POST, PUT, and DELETE.
* Allow users to specify additional HTTP headers.
* Accept complete URLs instead of only hostnames.
* Add HTTPS support using Python's `ssl` module.
* Display and interpret HTTP status codes such as 200, 404, and 500.
* Follow HTTP redirects such as 301 and 302.
* Extend hostname resolution and connections to IPv6.
* Add optional arguments for ports, paths, methods, headers, and timeouts.

## What I Learned

* How DNS resolution converts hostnames into IP addresses.
* How to establish TCP connections using Python's `socket` library.
* How HTTP requests are structured and transmitted over TCP.
* How to construct and send raw HTTP/1.1 requests without high-level libraries.
* How to send and receive bytes through sockets and encode/decode data.
* How to use `argparse` to build a command-line interface.
* How to structure a networking project using modular functions and exception handling.
* How DNS, TCP, and HTTP work together to enable web communication.

## License

MIT License
