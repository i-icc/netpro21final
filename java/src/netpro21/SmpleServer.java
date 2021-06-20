package netpro21;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class SmpleServer {
	public static void main(String[] args)
    {
	try {
		int port=8888;
	    ServerSocket srvSock = new ServerSocket(port);
	    
	    Socket socket = srvSock.accept();
      System.out.println("Address:" + socket.getInetAddress());

	    BufferedReader reader = new BufferedReader
	    	(new InputStreamReader(socket.getInputStream()));
	    String line = reader.readLine();
	    System.out.println("Rsv Message from Client at Server:" + line);
	    reader.close();
	    socket.close();
	    srvSock.close();
	}
	catch (IOException e) {
	    e.printStackTrace();
	}
    }
}
