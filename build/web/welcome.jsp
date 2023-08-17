<%-- 
    Document   : welcome
    Created on : 9/jun/2023, 18:07:01
    Author     : phlag
--%>

<%@page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>File Upload/Download</title>
        
    </head>
    <body>
        <%
            if(session.getAttribute("username") == null){
                response.sendRedirect("login.jsp");
            }
        %>
        <h1>Welcome ${username}</h1>
        <form action="Logout">
        <input type="submit" value="Logout">
        </form>
        <br>
        
        <div class="main">
            <form action="FileUploadServlet" method="post" enctype="multipart/form-data">
                Select <input type="file" name="file" id="file"/>
                Destination <input type="text" value="/temp" name="destination"/>
                <br>
                <input type="submit" value="Upload file" name="upload" id="upload">      
            </form>                     
        </div>  
        
        <h1>Download</h1>
        Guru Downloading File<a href="guru_download">Download here!!!</a>

<%--        
        <form name="frm" action="proccess.jsp" method="POST" enctype="multipart/form-data">
            Browse your image:
            <input type="file" name="upload"/>
            <input type="submit" value="Upload the file"/>
        </form>
--%> 
<%--
        <div class="main">
            <form method="POST" action="UploadServlet" enctype="multipart/form-data">
                <input type="file" name="file"/>
                <input type="submit" value="Upload"/>
            </form>
        </div>  
--%>       
    </body>
</html>
