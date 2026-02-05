<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Train Ticket Booking</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: lightgray;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        form {
            background: white;
            padding: 20px;
            width: 100%;
            max-width: 400px;
            border-radius: 8px;
            box-shadow: 0 0 10px gray;
        }

        input, select, button {
            width: 100%;
            padding: 10px;
            margin-bottom: 12px;
            font-size: 16px;
        }

        button {
            background: blue;
            color: white;
            border: none;
            cursor: pointer;
        }

        button:hover {
            background: navy;
        }

        .result {
            margin-top: 15px;
            background: lavender;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>

<body>

<form method="post">
    <input type="text" name="pname" placeholder="Passenger Name" required>
    <input type="number" name="page" placeholder="Age" min="1" required>
    <input type="number" name="dis" placeholder="Distance (km)" min="1" required>

    <select name="clas" required>
        <option value="">Select Class</option>
        <option value="SL">SL</option>
        <option value="3AC">3AC</option>
        <option value="2AC">2AC</option>
        <option value="1AC">1AC</option>
    </select>

    <select name="pay" required>
        <option value="">Payment Mode</option>
        <option value="UPI">UPI</option>
        <option value="Cash">Cash</option>
        <option value="Other">Other</option>
    </select>

    <input type="number" name="ticket" placeholder="Number of Tickets" min="1" required>

    <button type="submit" name="submit">BOOK</button>

<?php
if (isset($_POST['submit'])) {

    $pname  = filter_input(INPUT_POST, 'pname');
    $age    = filter_input(INPUT_POST, 'page', FILTER_VALIDATE_INT);
    $dis    = filter_input(INPUT_POST, 'dis', FILTER_VALIDATE_INT);
    $clas   = filter_input(INPUT_POST, 'clas');
    $pay    = filter_input(INPUT_POST, 'pay');
    $ticket = filter_input(INPUT_POST, 'ticket', FILTER_VALIDATE_INT);

    if ($ticket <= 0) {
        echo "<p class='result'>Please enter a valid ticket count.</p>";
        exit;
    }

    $fare = 10 * $dis;

    if ($age <= 12) {
        $fare *= 0.5;
    } elseif ($age <= 16) {
        $fare *= 0.6;
    }

    if ($dis >= 500) {
        $fare *= 0.9;
    } elseif ($dis > 100) {
        $fare *= 0.95;
    }

    switch ($clas) {
        case "1AC": $fare *= 1.4; break;
        case "2AC": $fare *= 1.3; break;
        case "3AC": $fare *= 1.2; break;
    }

    if ($pay === "UPI") {
        $fare *= 0.9;
    } elseif ($pay === "Other") {
        $fare *= 0.95;
    }

    if ($ticket >= 5) {
        $fare *= 0.9;
    }

    $total = max(0, round($fare * $ticket, 2));

    echo "
    <div cl
