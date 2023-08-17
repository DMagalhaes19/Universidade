package chat;

import java.awt.*;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class UserRegistrationSocket extends Thread{
    InetAddress ER;
    DatagramSocket DS;
    byte bp[] = new byte[1024];
    TextArea Registry = new TextArea(12, 40);
    Map<String,Integer> usersList = new HashMap<>();

    String assignedmsg = null;

    UserRegistrationSocket(TextArea ta) {
        Registry = ta;
    }

    public void run() {
        try {
            DS = new DatagramSocket(8081);
            Registry.append("Welcome to the Registry Service!\n");
        } catch (IOException e) {
        }
        while (true)
            receiveDP();
    }

    public String receiveAssignDP(){
        String msg = null;
        try{
            DatagramPacket DP = new DatagramPacket(bp, 1024);
            DS.receive(DP);
            byte Payload[] = DP.getData();
            int len = DP.getLength();
            msg = new String(Payload, 0, 0, len);
        }
        catch (IOException e) {
        }
        return msg;
    }

    public void receiveDP() {
        try {
            DatagramPacket DP = new DatagramPacket(bp, 1024);
            DS.receive(DP);
            byte Payload[] = DP.getData();
            int len = DP.getLength();
            int sender = DP.getPort();
            String msg = new String(Payload, 0, 0, len);
            if (msg.charAt(0) == '-' && msg.charAt(1) == 'r'){
                String regmsg = msg.substring(2);
                String sendRegmsg = "-r" + regmsg;
                sendDP(8080, sendRegmsg);
                assignedmsg = receiveAssignDP();
                if(assignedmsg.charAt(0) == 'y'){
                    String msgToSend = assignedmsg;
                    sendDP(sender, msgToSend);
                    int portAssigned = Integer.parseInt(msgToSend.substring(2));
                    usersList.put(regmsg,portAssigned);
                    regmsg = regmsg.substring(0, 1).toUpperCase() + regmsg.substring(1);
                    Registry.append("\nCreated: " + regmsg + "!");
                }
                else{
                    String res = "n";
                    Registry.append("\n" + "User not assigned due to a conflict!");
                    sendDP(sender, res);
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
