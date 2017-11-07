# HTTP

## List of HTTP Status Codes (Selected Few)

### 1xx Informational Responses

### 2xx Success
**200 OK**
Standard response for successful HTTP requests. The actual response will depend on the request method used. In a GET request, the response will contain an entity corresponding to the requested resource. In a POST request, the response will contain an entity describing or containing the result of the action.

### 3xx Redirection

### 4xx Client Errors
**400 Bad Request**
The server cannot or will not process the request due to an apparent client error (e.g., malformed request syntax, too large size, invalid request message framing, or deceptive request routing).

**401 Unauthorized**
Similar to 403 Forbidden, but specifically for use when authentication is required and has failed or has not yet been provided. 

**403 Forbidden**
The request was valid, but the server is refusing action. The user might not have the necessary permissions for a resource.

**404 Not Found**
The requested resource could not be found but may be available in the future. Subsequent requests by the client are permissible.

### 5xx Server Error