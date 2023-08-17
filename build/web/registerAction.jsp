<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="java.io.File" %>
<%@ page import="java.io.FileWriter" %>
<%@ page import="java.io.BufferedWriter" %>
<%@ page import="java.io.FileReader" %>
<%@ page import="java.io.BufferedReader" %>
<%@ page import="java.io.IOException" %>
<%@ page import="java.util.ArrayList" %>
<!DOCTYPE html>
<html>
<head>
    <title>Register Processing</title>
</head>
<body>
<%
    String name = request.getParameter("name");
    String password = request.getParameter("password");

    // Check if the file exists
    String filePath = getServletContext().getRealPath("C:/Users/phlag/Desktop/Projeto_AAdS/data/register.txt");
    File file = new File(filePath);
    if (!file.exists()) {
        file.createNewFile();
    }

    // Read existing entries from the file
    ArrayList<String> entries = new ArrayList<>();
    BufferedReader reader = null;
    try {
        reader = new BufferedReader(new FileReader(filePath));
        String line;
        while ((line = reader.readLine()) != null) {
            entries.add(line);
        }
    } finally {
        if (reader != null) {
            reader.close();
        }
    }

    // Search for the user in the entries list
    boolean userExists = false;
    for (String entry : entries) {
        String[] parts = entry.split(",");
        String existingName = parts[0];
        if (existingName.equals(name)) {
            userExists = true;
            break;
        }
    }

    if (userExists) {
        out.println("User already exists. Please choose a different name.");
    } else {
        // Add the new entry to the list
        String newEntry = name + "," + password;
        entries.add(newEntry);

        // Save the updated entries to the file
        BufferedWriter writer = null;
        try {
            writer = new BufferedWriter(new FileWriter(filePath, true));
            writer.write(newEntry);
            writer.newLine();
        } finally {
            if (writer != null) {
                writer.close();
            }
        }

        out.println("Registration successful.");
    }
%>
</body>
</html>