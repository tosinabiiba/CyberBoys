<?php
$file = fopen("expenses.csv", "r");

$table = "<tr><th>Bills</th><th>Amount</th></tr>";
while (($data = fgetcsv($file)) !== false) {
  $table .= "<tr><td>{$data[0]}</td><td>{$data[1]}</td></tr>";
}
fclose($file);

echo $table;
?>
