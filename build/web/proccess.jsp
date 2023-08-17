<%-- 
    Document   : proccess
    Created on : 10/jun/2023, 11:23:34
    Author     : phlag
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="com.oreilly.servlet.MultipartRequest" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%
           String root=getServletContext().getRealPath("files");
           MultipartRequest mr=new MultipartRequest(request,root);
           out.print("sccs");
        %>
    </body>
</html>
