## Overview of Socket Communication

**Sockets** serves as a fundamental interface for network communication in a client-server model. It allows processes on different computers, or within the same computer, to communicate over a network using IP addresses or through interprocess communication (IPC) mechanisms.

### Key Concepts:

- Sockets are endpoints in a network communication setup. They enable data exchange between a client process and a server process across different computers or within the same computer.
- TCP/IP Model: Sockets operate at the transport layer of the TCP/IP model. By using socket APIs, programmers can abstract away the implementation of lower network layers (below the transport layer), such as network routing and data packetization. This abstraction allows applications to send data through sockets without needing to manage the details of network protocols.

### Addressing:

- TCP sockets: Identified by a four-tuple key: (source IP, source port, destination IP, destination port), ensuring a unique connection identifier across the network.
- UDP sockets: As a connectionless protocol, there is no concept of connections or listening and accepting in the traditional sense used with TCP. Instead, data is received directly with recvfrom(), which also returns the sender’s address. Endpoints are identified by a two-tuple (IP address, port number).
- Unix sockets: They are similar to TCP in that they can be connection-oriented, but they use a pathname in the file system as an endpoint identifier and return an empty string when the address of the connecting entity is not specified.

### Pipe vs. Socket

**Sockets**

- Bidirectional Communication: Support two-way data transfer within the same connection, suitable for interactive applications.
- Network Overhead: Generally used for network communications, involving a protocol stack that handles data transmission, error detection, and more, which can introduce overhead especially in local communications.
- Flexibility: Can be used for both network communication across different machines and local IPC within the same machine. However, using them for local IPC can lead to unnecessary complexity and performance costs.


**Pipes**

- Unidirectional Communication: Only allow data flow in one direction, ideal for straightforward data streaming tasks.
- Optimized for Local IPC: Specifically designed for local inter-process communication, providing faster data transfer with minimal overhead compared to sockets.
- Simplex Communication: Natively support simplex (one-way) communication; require two pipes for full-duplex (two-way) communication, complicating bidirectional interactions.


### Managing Multiple Client Connections

When dealing with multiple client connections, a server has a few strategies:

1. Thread Per Client
2. Process Per Client
3. Non-blocking Sockets with Select

**Tips**

- Design protocols to clearly define message boundaries: Some of the options are using fixed-length messages, delimiters, or include a message length field (indicating how long they are) at the start.
