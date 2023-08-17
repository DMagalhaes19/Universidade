package chat;

import javax.swing.*;
import java.io.*;
import java.awt.*;
import java.util.Date;
import java.util.HashSet;
import java.util.Random;
import java.util.Set;
import java.util.concurrent.TimeUnit;

public class chat extends Frame {
    TextArea ecran = new TextArea(10, 30);//, TextArea.SCROLLBARS_VERTICAL_ONLY);
    TextField text = new TextField(30); // text field for user input
    Label userlab = new Label();// label for user input
    Button Send = new Button("Send");// button for user input
    Button Remembers = new Button("Remember Your Pin");// button for user input
    socket sock = new socket(ecran);// socket for user input

    String user = null;// user name
    String formUser = null;// formatted user name
    boolean userLenValid = false;// user name length validation

    public chat(String str) {
        super(str);
    }

    public void GUI() {
        setBackground(Color.lightGray);
        ecran.setEditable(false);
        GridBagLayout GBL = new GridBagLayout();
        setLayout(GBL);
        Panel P1 = new Panel();
        P1.setLayout(new BorderLayout(5, 5));
        P1.add("North", userlab);
        P1.add("Center", text);
        P1.add("East", Send);
        P1.add("West", Remembers);
        P1.add("South", ecran);
        GridBagConstraints P1C = new GridBagConstraints();
        P1C.gridwidth = GridBagConstraints.REMAINDER;
        GBL.setConstraints(P1, P1C);
        add(P1);
    }

    public void setupClient() {
        while (!userLenValid) { // while user name is not valid
            user = JOptionPane.showInputDialog("Enter your username");// get user name
            if (user.length() > 0) {// if user name is not empty
                userLenValid = true;// set user name length validation to true
                break;// break out of while loop
            }// end if
            else {
                JOptionPane.showInputDialog("Username cannot be empty! Enter your username");// get user name
            }
        }// end while
        int portNum = 0;
        int option = JOptionPane.showOptionDialog(null, "Would you like to specify a port number or let the code assign one?", "Port Number Selection", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE, null, new Object[] {"Specify", "Assign"}, "Specify");
        if (option == JOptionPane.YES_OPTION) {
            while (true) {
                try {
                    portNum = Integer.parseInt(JOptionPane.showInputDialog("Enter a port number between 8000 and 8010"));
                    if (portNum >= 8000 && portNum <= 8010) {
                        break;
                    } else {
                        JOptionPane.showMessageDialog(null, "Invalid port number, please enter a number between 8000 and 8010");
                    }
                } catch (NumberFormatException e) {
                    JOptionPane.showMessageDialog(null, "Invalid input, please enter a number between 8000 and 8010");
                }
            }
        }
        else {
            Random rand = new Random();
            portNum = rand.nextInt((8010 - 8000) + 1) + 8000;
            System.out.println("Port number: " + portNum);
        }
            user = "-r" + user + ":" + portNum;
            String userName = user.split(":")[0]; // format user name for display
            formUser = userName.substring(2);
            formUser = formUser.substring(0, 1).toUpperCase() + formUser.substring(1);//capitalize first letter of username
            userlab.setText("Logged in as: " + formUser);// set user name label
            sock.sendtoServices(8081, user);// send user name to name service
            try {
                TimeUnit.MILLISECONDS.sleep(100);// wait 100 milliseconds
            } catch (InterruptedException e) {
                System.out.println("Interrupted");
            }
            while (!sock.getConfirm()) {// while user name is not confirmed
                //close the panel and restart the process
                JOptionPane.showMessageDialog(null, "Username already exists, please enter a different username");
                try {
                    TimeUnit.MILLISECONDS.sleep(100);
                } catch (InterruptedException e) {
                    System.out.println("Interrupted");
                }
                userLenValid = false;
                setupClient();
            }
        }
    public void StartSocket() {
        sock.start();// start socket
    }

    public boolean handleEvent(Event i) {
        if (i.id == Event.WINDOW_DESTROY) {
            dispose();// dispose of window
            System.exit(0);// exit program
            return true;// return true
        }
        return super.handleEvent(i);// return super handle event
    }

    public boolean action(Event i, Object o) {
        if (i.target == Send) {// if send button is clicked
            int pin = Integer.parseInt(JOptionPane.showInputDialog("Introduce your pin: "));// get pin
            if(sock.getPort() != pin) {// if pin is not correct
                JOptionPane.showMessageDialog(null, "Incorrect pin!");// show incorrect pin message
                return true;// return true
            }
            int portDest = 0;// port destination
            String msg = text.getText();//// get text from text field
            String addrDest = JOptionPane.showInputDialog("Enter to whom you want to send the message");// get address destination
            if (addrDest.contains(",")) {// if address destination contains a comma
                String askDest = "-am" + addrDest;// add -am to address destination
                sock.sendtoServices(8080, askDest);// send address destination to services
            } else {// if address destination does not contain a comma
                String askDest = "-a" + addrDest;// add -a to address destination
                sock.sendtoServices(8080, askDest);// send address destination to services
            }// end if

            try {
                TimeUnit.MILLISECONDS.sleep(1000);// wait 1000 milliseconds
            } catch (InterruptedException e) {// catch interrupted exception
                System.out.println("Interrupted");// print interrupted
            }

            portDest = sock.getdestPort();// get port destination

            ecran.appendText("\n" + "Eu: " + msg);// append message to text area

            msg = user + ',' + msg;// add user name to message

            int j = 0;
            if (j < Integer.toString(portDest).length()) {
                do {
                    String strPortDest = Integer.toString(portDest).substring(j, j + 4);
                    int singlePort = Integer.parseInt(strPortDest);
                    sock.sendDP(singlePort, msg, "127.0.0.1");
                    j = j + 4;
                } while (j < Integer.toString(portDest).length());
            }


            text.setText("");// clear text field

            sock.setdestPort(0);// set port destination to 0

            return true;
        }
        else if(i.target == Remembers){
            JOptionPane.showMessageDialog(null, "Your Pin is  " + sock.getPort());
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        NameService.main(args);// start name service
        UserRegistration.main(args);// start user registration
        launchChatInstance();
}
    private static void launchChatInstance() throws IOException {
        chat app = new chat("chat");// create new chat instance
        app.resize(600, 350);// resize chat instance
        app.StartSocket();// start socket
        app.setupClient();// setup client
        app.GUI();// set up GUI
        app.show();// show chat instance
        int choice = JOptionPane.showConfirmDialog(null, "Do you want to launch another chat instance?", "Launch another instance", JOptionPane.YES_NO_OPTION);// ask user if they want to launch another chat instance
        if (choice == JOptionPane.YES_OPTION) {// if user chooses yes
            launchChatInstance();// launch another chat instance
        }
    }
}