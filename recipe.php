<?php
// Connect to the database
$db_host = 'localhost';
$db_user = 'username';
$db_pass = 'password';
$db_name = 'fridge_inventory';
$conn = mysqli_connect($db_host, $db_user, $db_pass, $db_name);

// Retrieve the inventory data from the database
$sql = "SELECT * FROM inventory";
$result = mysqli_query($conn, $sql);

// Output the inventory data in an HTML table
echo "<table>";
echo "<tr><th>Name</th><th>Expiration Date</th></tr>";
while ($row = mysqli_fetch_assoc($result)) {
    echo "<tr>";
    echo "<td>" . $row['name'] . "</td>";
    echo "<td>" . $row['expiration_date'] . "</td>";
    echo "</tr>";
}
echo "</table>";

// Close the database connection
mysqli_close($conn);
?>
<!-- 

First, set up a development environment for PHP. 
This typically involves installing a web server (such as Apache or Nginx), a database server (such as MySQL), and PHP itself.
Design the database schema for storing the inventory data. 
This might include a table for storing information about the items in the fridge, with columns for the item name, expiration date, and any other relevant information.
Write a PHP script to handle the logic for displaying the current inventory. 
This might involve creating a SQL query to select all rows from the inventory table, and using a loop to iterate over the results and display them in an HTML table.
Use HTML, CSS, and JavaScript to design the user interface (UI) and user experience (UX) of the app. You will need to make use of PHP's echo function to output the HTML, as well as any data from the database.
Test the app thoroughly to ensure that it is stable and user-friendly.
Here is an example of what the PHP code for displaying the inventory might look like:
 -->