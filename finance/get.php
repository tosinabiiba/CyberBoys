<?php
if (isset($_POST['bills']) && isset($_POST['amount'])) {
  $bills = $_POST['bills'];
  $amount = $_POST['amount'];

  $file = fopen("expenses.csv", "a");
  fputcsv($file, [$bills, $amount]);
  fclose($file);
}
?>