<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exercise 1</title>
    <style>
        select{
            width: 170px;
        }
    </style>
</head>
<body>
    <form method="post">
        <input type="text" name="pname" placeholder="Enter Name" required> <br><br>
        <input type="text" name="page" placeholder="Enter Age" required><br><br>
        <input type="text" name="dis" placeholder="Enter Distance" required><br><br>
        <select name="clas" required>
            <option value="SL">SL</option>
            <option value="1AC">1AC</option>
            <option value="2AC">2AC</option>
            <option value="3AC">3AC</option>
        </select><br><br>
        <select name="pay"required>
            <option value="UPI">UPI</option>
            <option value="Cash">Cash</option>
            <option value="Other">Other</option>
        </select><br><br>
        <input type="text" name="ticket" placeholder="Enter ticket number" required><br><br><br><br>
        <input type="submit" value="BOOK" name="submit"><br><br>
    </form>
</body>
</html>
<?php
    if(isset($_POST['submit'])){
        $pname=$_POST['pname'];
        $page=$_POST['page'];
        $dis=$_POST['dis'];
        $clas=$_POST['clas'];
        $pay=$_POST['pay'];
        $ticket=$_POST['ticket'];

        $total=10*$dis;

        if ($page<=12) $total-=$total*0.5;
        else if ($page<=16 && $page>12) $total-=$total*0.4;

        if ($dis>=500) $total-=$total*0.1;
        else if($dis>100 && $dis<500) $total-=$total*0.05;

        if ($clas=="1AC") $total+=$total*0.4;
        else if ($clas=="2AC") $total+=$total*0.3;
        else if ($clas=="3AC") $total+=$total*0.2;

        if ($pay=="UPI") $total-=$total*0.1;
        else if ($pay=="Other")  $total-=$total*0.05;

        if($ticket==0) echo"give valid ticket";

        if($ticket>=5)  $total-=$total*0.1;

        echo "Name = $pname <br>";
        echo "Age = $page <br>";
        echo "Tickets = $ticket <br>";
        echo "Class = $clas <br>";
        echo "Total = $total <br>";
    }
?>