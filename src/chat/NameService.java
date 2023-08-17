package chat;

import java.awt.*;
import java.io.*;

public class NameService extends Frame {
    TextArea NameServer = new TextArea(12, 40);//text area for the name server
    NameServiceSocket sock = new NameServiceSocket(NameServer);//socket for the name server

    public NameService(String nm) {
        super(nm);
    }

    public void GUI() {
        setBackground(Color.lightGray);//set background color
        NameServer.setEditable(false);//set text area to not editable
        GridBagLayout GBL = new GridBagLayout();//set layout
        setLayout(GBL);//set layout
        Panel P1 = new Panel();//create panel
        P1.setLayout(new BorderLayout(5, 5));//set layout
        P1.add("Center", NameServer);//add text area to panel
        GridBagConstraints P1C = new GridBagConstraints();//create grid bag constraints
        P1C.gridwidth = GridBagConstraints.REMAINDER;//set grid width
        GBL.setConstraints(P1, P1C);//set constraints
        add(P1);//add panel to frame
    }

    public void StartSocket() {
        sock.start();
    }

    public boolean handleEvent(Event i) {
        if (i.id == Event.WINDOW_DESTROY) {
            dispose();
            System.exit(0);
            return true;
        }
        return super.handleEvent(i);
    }

    public static void main(String[] args) throws IOException {
        NameService app = new NameService("Name Service");
        app.resize(320, 240);
        app.GUI();
        app.show();
        app.StartSocket();
    }
}
