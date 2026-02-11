<?php
function calculateTotalBill(
    float $itemPrice,
    int $quantity,
    string $day,
    string $paymentMode,
    string $shoppingTime,
    string $membershipStatus,
    string $carryBagRequired,
    int $distinctItems
){
    $day = strtolower($day);
    $paymentMode = strtolower($paymentMode);
    $shoppingTime = strtolower($shoppingTime);
    $membershipStatus = strtolower($membershipStatus);
    $carryBagRequired = strtolower($carryBagRequired);

    $totalBill = $itemPrice * $quantity;
    $discount = 0;

    if ($day === 'wednesday') {
            $discount += 0.10;
        }

        if ($totalBill > 3000) {
            $discount += 0.07;
        }

        if ($distinctItems >= 5) {
            $discount += 0.05;
        }

        if ($paymentMode === 'upi') {
            $discount += 0.05;
        } elseif ($paymentMode === 'online') {
            $discount += 0.03;
        }

        if ($shoppingTime === 'morning') {
            $discount += 0.02;
        }

        if ($membershipStatus === 'member') {
            $discount += 0.05;
        }

        $totalBill -= $totalBill * $discount;

        if ($carryBagRequired === 'yes') {
            $totalBill += 10;
        }
        
        return max($totalBill, 0);
    }

?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Supermarket Billing</title>
<style>
    body {
        font-family: Arial, Helvetica, sans-serif;
        background: linear-gradient(120deg, #274dc1, #66f5ff);
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    form {
        background: #fff;
        padding: 25px;
        width: 350px;
        border-radius: 12px;
    }

    h2 {
        text-align: center;
        margin-bottom: 20px;
        color: #333;
    }

    label {
        font-weight: bold;
        margin-top: 10px;
        display: block;
        color: #555;
    }

    input, select {
        width: 100%;
        padding: 8px;
        margin-top: 5px;
        border-radius: 6px;
        border: 1px solid #ccc;
        font-size: 14px;
    }

    input:focus, select:focus {
        outline: none;
        border-color: #66a6ff;
    }

    input[type="submit"] {
        margin-top: 20px;
        background: #66a6ff;
        color: white;
        border: none;
        font-size: 16px;
        padding: 10px;
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    input[type="submit"]:hover {
        transform: translateY(-10px);
    }


    .result {
        margin-top: 20px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        color: #2c3e50;
    }
</style>
</head>
<body>

<form method="post">
    <h2>Billing System</h2>

    <label>Item Price</label>
    <input type="number" name="itemPrice" min=1 required>

    <label>Quantity</label>
    <input type="number" name="quantity" min=1 required>

    <label>Day of Shopping</label>
    <select name="day">
        <option>Monday</option>
        <option>Tuesday</option>
        <option>Wednesday</option>
        <option>Thursday</option>
        <option>Friday</option>
        <option>Saturday</option>
        <option>Sunday</option>
    </select>

    <label>Payment Mode</label>
    <select name="paymentMode">
        <option>UPI</option>
        <option>Online</option>
        <option>Cash</option>
    </select>

    <label>Shopping Time</label>
    <select name="shoppingTime">
        <option>Morning</option>
        <option>Evening</option>
    </select>

    <label>Membership Status</label>
    <select name="membershipStatus">
        <option>Member</option>
        <option>Non-member</option>
    </select>

    <label>Carry Bag Required</label>
    <select name="carryBagRequired">
        <option>Yes</option>
        <option>No</option>
    </select>

    <label>Distinct Items</label>
    <input type="number" name="distinctItems" min=1 required>

    <input type="submit" name="submit" value="Calculate Bill">

    <?php
    if (isset($_POST['submit'])) {
        $totalBill = calculateTotalBill(
            $_POST['itemPrice'],
            $_POST['quantity'],
            $_POST['day'],
            $_POST['paymentMode'],
            $_POST['shoppingTime'],
            $_POST['membershipStatus'],
            $_POST['carryBagRequired'],
            $_POST['distinctItems']
        );

        echo "<div class='result'>Total Bill: ₹" . number_format($totalBill, 2) . "</div>";
    }
    ?>
</form>

</body>
</html>
