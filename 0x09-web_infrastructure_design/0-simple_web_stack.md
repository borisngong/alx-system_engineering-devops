![0-simple_web_stack png](https://github.com/borisngong/alx-system_engineering-devops/assets/67687796/be01329a-b8b7-4000-9d12-4e5024b4aaa4)

The user wishes to visit the www.foobar.com website within this single server
web infrastructure. 

The components that comprise the infrastructure are as follows:

1. Server: This is the actual computer that houses each and every web
   infrastructure component.
2. The web server (Nginx) is in charge of responding to incoming requests for
   HTTP arriving from
   the user's browser. JavaScript, HTML, CSS, and other static files are
   served by it.
3. Application Server: This one handles requests that need to be processed
   server-side. To save or retrieve data, it exchanges messages with the 
   database.
4. Application Files (Code Base): The application server uses these files to
   run code in order to process user requests.
5. Database (MySQL): This one handles data retrieval and storage.
6. Domain Name (foobar.com): To visit the website, a user enters this URL
   into their browser.
7. DNS Record (www): This DNS record links the IP address of the server to
   the domain name.
   
=> TCP/IP is used by the server and the user's machine to communicate.
   The DNS converts the domain name to the IP address of the server when a user
   types www.foobar.com into their browser. After that, the browser contacts
   the server via an HTTP request. After receiving the request, the web server
   either sends it to the application server or delivers a static file. After
   processing the request, the application server replies to the web server by
   retrieving or storing data from the database. The user's browser receives
   the response from the web server after that.

=> There exist multiple concerns regarding this infrastructure:

1. Single Point of Failure (SPOF): The entire website becomes unreachable in
   the event of a server failure. Redundancy can be used by having numerous
   servers to lessen this.
2. Downtime: The web server must be restarted when maintenance is required,
   such as the deployment of new code. The website may experience outages
   as a result. You can lessen this by using a load balancer to split up
   incoming traffic among several servers.
3. Scalability: The server might not be able to manage an excessive amount
   of incoming traffic. You can use auto-scaling to automatically add or
   remove servers in response to the traffic load in order to handle this.

