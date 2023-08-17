package chat;


import java.awt.*;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.*;
import java.util.List;

public class NameServiceSocket extends Thread {
    private Map<String, Integer> userList = new HashMap<>();
    Set<Integer> usedPorts = new HashSet<>();
    InetAddress ER;
    DatagramSocket DS;
    byte bp[] = new byte[1024];
    TextArea Server = new TextArea(12, 40);
    NameServiceSocket(TextArea ta) {
        Server = ta;
    }

    public void run() {
        try {
            DS = new DatagramSocket(8080);
        } catch (IOException e) {
        }
        while (true)
            receiveDP();
    }

    public void receiveDP() {
        try {
            DatagramPacket DP = new DatagramPacket(bp, 1024);//receive a packet
            DS.receive(DP);//receive a packet
            byte Payload[] = DP.getData();//get the data from the packet
            int len = DP.getLength();//get the length of the data
            String msg = new String(Payload, 0, 0, len);//convert the data to a string
            int sender = DP.getPort();//get the port of the sender
            int portNum = 0;
            String assignedPort = null;
            String assignedmsg = null;
                String msgArray[] = msg.split(":");
                String username = msgArray[0].substring(0).toLowerCase();
                if(msgArray.length > 1){
                    portNum = Integer.parseInt(msgArray[1]);
                }
                if (username.charAt(0) == '-' && username.charAt(1) == 'a' && username.charAt(2) == 'm') {//if the message is a registration message from the user registration service then add the user to the list
                    String askmsg = username.substring(3).toLowerCase();//get the username from the message
                    String[] askmsgArray = askmsg.split(",");//split the message into an array
                    assignedmsg = "-am";//create a message to send to the user registration service
                    for (String dest : askmsgArray) {//for each username in the array
                        if (userList.containsKey(dest)) {//if the username is in the list
                            //get the port of the receiver
                            assignedPort = userList.get(dest).toString();
                            assignedmsg += assignedPort;//add the port number to the message
                        }
                    }
                    sendDP(sender, assignedmsg);//send the message to the user registration service
                }
                if(username.charAt(0) == '-' && username.charAt(1) == 'a'){
                    String askmsg = username.substring(2).toLowerCase();//get the username from the message
                    if (userList.containsKey(askmsg)) {//if the username is in the list
                        assignedPort = String.valueOf(userList.get(askmsg));//get the port of the receiver
                        assignedmsg = "-a" + assignedPort;//create a message to send to the user registration service
                        sendDP(sender, assignedmsg);//send the message to the user registration service
                    }
                }

                if(username.charAt(0) == '-' && username.charAt(1) == 'r'){
                    String regmsg = username.substring(2).toLowerCase();//get the username from the message
                    if (userList.isEmpty()) {//if the list is empty
                        if(!usedPorts.contains(portNum)) {
                            userList.put(regmsg, portNum);//add the username and port number to the list
                            usedPorts.add(portNum);
                            String user = regmsg.substring(0, 1).toUpperCase() + regmsg.substring(1);//capitalize the first letter
                            Server.append("\nAssigned '" + user + "' on Port: " + portNum + "!");//print the name and port
                            String portAssign = "y" + "p" + portNum;//create a message to send to the user registration service
                            sendDP(sender, portAssign);//send the message to the user registration service
                        }
                    } else {
                        String portAssign = null;//create a message to send to the user registration service
                        String cliSenderName = regmsg;//get the username from the message
                        for (String key : userList.keySet()) {//check if user already exists
                            if (key.equals(cliSenderName)) {//if the user already exists
                                Server.append("\nUser already exists. Choose a different name.");//print the name and port
                                portAssign = "n";//create a message to send to the user registration service
                                sendDP(sender, portAssign);//send the message to the user registration service
                                break;//break out of the loop
                            } else {//if user doesn't exist
                                if(!usedPorts.contains(portNum)) {
                                    userList.put(regmsg, portNum);//add the username and port number to the list
                                    usedPorts.add(portNum);
                                    String user = regmsg.substring(0, 1).toUpperCase() + regmsg.substring(1);//capitalize the first letter
                                    Server.append("\nAssigned '" + user + "' on Port: " + portNum + "!");//print the name and port
                                    portAssign = "y" + "p" + portNum;//create a message to send to the user registration service
                                    sendDP(sender, portAssign);//send the message to the user registration service
                                    break;//break out of the loop
                                }
                            }
                        }
                    }
                }
        } catch (IOException e) {
        }
    }
    public void sendDP(int Pr, String msg) {
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
}