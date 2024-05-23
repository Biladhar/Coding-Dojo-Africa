<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Time</title>
<link rel="stylesheet" type="text/css" href="/css/date.css">
<script type="text/javascript" src="/js/time.js"></script>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</head>
<body>
    <div >
        <p class="fs-1 fw-bold text-primary">
            <%
                java.text.SimpleDateFormat formatter = new java.text.SimpleDateFormat("h:mm a");  
                java.util.Date time = new java.util.Date();  
                out.print(formatter.format(time));
            %>
        </p>
    </div>
</body>
</html>