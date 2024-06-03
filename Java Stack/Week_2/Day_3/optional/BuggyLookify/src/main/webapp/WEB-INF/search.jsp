<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!-- New line below to use the JSP Standard Tag Library -->
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<%@ page isErrorPage="true"%>
<!-- for Bootstrap CSS -->
<!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous"> -->
<link rel="stylesheet" href="/webjars/bootstrap/css/bootstrap.min.css" />

<%@ taglib prefix = "fmt" uri = "http://java.sun.com/jsp/jstl/fmt" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Search result</title>
<link rel="stylesheet" type="text/css" href="/css/style.css">
</head>
<body>
<div class="container mt-3">
    <h1>Search result</h1>
    <table class="table table-striped">
        <thead>
            <tr>
                <th>Title</th>
                <th>Artist</th>
                <th>Rating</th>
            </tr>
        </thead>
        <tbody>
            <c:forEach var="song" items="${songs}">
                <tr>
                    <td><a href="/songs/${song.id}"><c:out value="${song.title}"></c:out></a></td>
                    <td><c:out value="${song.artist}"></c:out></td>
                    <td><c:out value="${song.rating}"></c:out></td>
                </tr>
            </c:forEach>
        </tbody>
    </table>
    <p><a href="/dashboard">Back to Dashboard</a></p>


</div>
</body>
</html>