<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page import="java.io.File" %>
<%@ page import="java.io.FileReader" %>
<%@ page import="java.io.BufferedReader" %>
<%@ page import="java.io.IOException" %>
<%@ page import="java.util.ArrayList" %>
<!DOCTYPE html>
<html>
<head>
    <title>Login Processing</title>
</head>
<body>
<%
    String name = request.getParameter("name");
    String password = request.getParameter("password");

    // Get the generic path relative to the application context path
    String filePath = getServletContext().getRealPath("/data/register.txt");
    File file = new File(filePath);
    if (!file.exists()) {
        out.println("File does not exist. Please register first.");
    } else {
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
            String existingPassword = parts[1];
            if (existingName.equals(name) && existingPassword.equals(password)) {
                userExists = true;
                break;
            }
        }

        if (userExists) {
            // Redirect to another page upon successful login
            response.sendRedirect("welcome.jsp");
        } else {
            out.println("Invalid username or password. Please try again.");
        }
    }
%>
</body>
</html>