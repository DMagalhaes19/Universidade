package chat;

import java.awt.*;
import java.io.IOException;

class UserRegistration extends Frame {
    TextArea Registry = new TextArea(12, 40);
    UserRegistrationSocket sock = new UserRegistrationSocket(Registry);

    public UserRegistration(String nm) {
        super(nm);
    }

    public void GUI() {
        setBackground(Color.lightGray);
        Registry.setEditable(false);
        GridBagLayout GBL = new GridBagLayout();
        setLayout(GBL);
        Panel P1 = new Panel();
        P1.setLayout(new BorderLayout(5, 5));
        P1.add("Center", Registry);
        GridBagConstraints P1C = new GridBagConstraints();
        P1C.gridwidth = GridBagConstraints.REMAINDER;
        GBL.setConstraints(P1, P1C);
        add(P1);
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
        UserRegistration app = new UserRegistration("Registry Service");
        app.resize(320, 240);
        app.GUI();
        app.show();
        app.StartSocket();
    }
}
