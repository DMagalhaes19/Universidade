package chat;
import java.io.*;
import java.net.*;
import java.awt.*;
import java.util.HashSet;
import java.util.Set;

public class socket extends Thread {
    InetAddress ER, IPr;
    DatagramSocket DS;
    byte bp[] = new byte[1024];
    TextArea ecran = new TextArea(10, 30);
    int port;
    Set<Integer> usedPorts = new HashSet<>();

    int destPort;

    boolean regUser = false;
    boolean confirm = false;

    socket(TextArea ta) {
        ecran = ta;
    }

    public void setPort(int p){
        port = p;
    }

    public int getPort(){
        return DS.getLocalPort();
    }
    public boolean getConfirm(){
        return confirm;
    }

    public int getdestPort(){
        return destPort;
    }

    public void setdestPort(int p){
        destPort = p;
    }

    public void receiveDP() {
        try {
            DatagramPacket DP = new DatagramPacket(bp, 1024);// create a new datagram packet
            DS.receive(DP);// receive the packet
            IPr = DP.getAddress();// get the address of the packet
            byte Payload[] = DP.getData();// get the data of the packet
            int len = DP.getLength();// get the length of the packet
            String res = new String(Payload, 0, 0, len);// convert the data to a string
            if (res.charAt(0) == '-' && res.charAt(1) == 'a'){// if the message starts with -a
                if (res.charAt(2) == 'm'){// if the message starts with -am
                    destPort = Integer.parseInt(res.substring(3));// get the port number
                }
                else{
                    destPort = Integer.parseInt(res.substring(2));// get the port number
                }
            }
            else{
                String [] resArray = res.split(",");// split the string by the comma
                String userSent = resArray[0].substring(2);// get the username
                userSent = userSent.substring(0, 1).toUpperCase() + userSent.substring(1);// capitalize the first letter
                String newRes = resArray[1];// get the message
                ecran.appendText("\n" + userSent + ": " + newRes);// display the message
            }

        } catch (IOException e) {
        }
    }

    public void receiveRegDP(){
        try {
            DatagramPacket DP = new DatagramPacket(bp, 1024);// create a new datagram packet
            DS.receive(DP);// receive the packet
            IPr = DP.getAddress();// get the address of the packet
            byte Payload[] = DP.getData();// get the data of the packet
            int len = DP.getLength();// get the length of the packet
            String res = new String(Payload, 0, 0, len);// convert the data to a string
            if (res.charAt(0) == 'y'){// if the message starts with y
                confirm = true;// set confirm to true
            }
            if (res.length() > 1){// if the message is longer than 1 character
                if (res.charAt(1) == 'p'){// if the message starts with yp
                    String tmp = res.substring(2);// get the port number
                    int p = Integer.parseInt(tmp);// convert the port number to an integer
                    setPort(p);// set the port number
                    usedPorts.add(p);// add the port number to the set of used ports
                    regUser = true;// set regUser to true
                }
            }

        } catch (IOException e) {
        }
    }

    public void sendDP(int Pr, String msg, String end) {
        int len = msg.length();// get the length of the message
        byte b[] = new byte[len];// create a new byte array
        msg.getBytes(0, len, b, 0);// convert the message to a byte array
        try {
            ER = InetAddress.getByName(end);// get the address of the destination
            DatagramPacket DP = new DatagramPacket(b, len, ER, Pr);// create a new datagram packet
            DS.send(DP);// send the packet
        } catch (IOException e) {
        }
    }

    public void sendtoServices(int Pr, String msg) {
        int len = msg.length();
        byte b[] = new byte[len];
        msg.getBytes(0, len, b, 0);
        try {
            ER = InetAddress.getByName("127.0.0.1");
            DatagramPacket DP = new DatagramPacket(b, len, ER, Pr);
            DS.send(DP);
        } catch (IOException e) {
        }
    }

    public void run() {
        try {
            DS = new DatagramSocket();
            System.out.println("Porta: " + DS.getLocalPort());
        } catch (IOException e) {
        }
        while (!regUser){
            receiveRegDP();
        }
        DS.close();
        try {
            DS = new DatagramSocket(port);
            System.out.println("Nova porta: " + DS.getLocalPort());
        } catch (IOException e) {
        }
        while (true){
            receiveDP();
        }
    }
}