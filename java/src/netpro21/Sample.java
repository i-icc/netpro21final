package netpro21;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.Socket;

import javax.swing.AbstractAction;
import javax.swing.Action;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;


public class Sample  extends JFrame {
	JButton upButton, downButton, rightButton, leftButton;
	JPanel pane;
	PrintWriter writer;

	public static void main(String[] args) {
		JFrame w = new Sample("Title");
		w.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		w.setSize(300, 300);
		w.setVisible(true);
	}

	public Sample(String title) {
		super(title);
		
		try {
			InetSocketAddress socketAddress = new InetSocketAddress("localhost", 8888);
		    Socket socket = new Socket();
		    socket.connect(socketAddress, 10000);
		    InetAddress inetadrs;
		    if ((inetadrs = socket.getInetAddress()) != null) {
				System.out.println("address:" + inetadrs);
			    }
			    else {
				System.out.println("Connection fail");
				return;
			    }
		    writer = new PrintWriter(socket.getOutputStream());
		}
		catch (IOException er) {
		    er.printStackTrace();
		}
		
		pane = (JPanel) getContentPane();

		JPanel buttons = new JPanel();
		buttons.setLayout(new GridLayout(2, 2));
		upButton = new JButton(new SendComand("up",writer));
		buttons.add(upButton);
		downButton = new JButton(new SendComand("down",writer));
		buttons.add(downButton);
		rightButton = new JButton(new SendComand("right",writer));
		buttons.add(rightButton);
		leftButton = new JButton(new SendComand("left",writer));
		buttons.add(leftButton);
		pane.add(buttons, BorderLayout.SOUTH);
	}
	
	class SendComand extends AbstractAction {
		String comand;
		PrintWriter writer;
		
		SendComand(String comand, PrintWriter writer) {
			this.comand = comand;
			this.writer = writer;
			putValue(Action.NAME, comand);
			putValue(Action.SHORT_DESCRIPTION, comand);
		}

		public void actionPerformed(ActionEvent e) {
			System.out.println(comand);
			writer.println(comand);
		}
	}
}