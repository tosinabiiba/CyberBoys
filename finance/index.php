<?php

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the data from the form
    $bills = $_POST["bills"];
    $amount = $_POST["amount"];
   
    // Open the CSV file for writing
    $file = fopen("bills.csv", "a");

    // Write the data to the CSV file
    fputcsv($file, [$bills, $amount]);

    // Close the CSV file
    fclose($file);
}

// Read the CSV file
$data = array_map('str_getcsv', file('bills.csv'));

// Calculate the total expenses
$total = 0;
foreach ($data as $row) {
    $total += (float) str_replace("£", "", $row[1]);
}

?>

<!DOCTYPE html>
<html>
<head>
    <title>Expenses Monitor</title>
</head>
<body>
    <h1>Expenses Monitor</h1>

    <form action="" method="post">
        <label for="bills">Bills:</label>
        <input type="text" name="bills" id="bills">

        <label for="amount">Amount:</label>
        <input type="text" name="amount" id="amount">

        <input type="submit" value="Add">
    </form>

    <table>
        <thead>
            <tr>
                <th>Bills</th>
                <th>Amount</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($data as $row): ?>
                <tr>
                    <td><?= $row[0] ?></td>
                    <td><?= $row[1] ?></td>
                </tr>
            <?php endforeach ?>
        </tbody>
        <tfoot>
            <tr>
                <td>Total</td>
                <td>£<?= number_format($total, 2) ?></td>
            </tr>
        </tfoot>
    </table>
</body>
</html>
