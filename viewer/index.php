<html>
    <head><title>Visor Inventari</title>
    <link rel="stylesheet" type="text/css" href="style.css"></head>
    <body>
        <table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th> 
    <th>Age</th>
  </tr>
        <?php
require_once('config.php');

error_reporting(E_ALL);
ini_set('display_errors', 1);

$sql = "SELECT * FROM inventory";
$result = $db->query($sql);

if (!$result) {
    die('Invalid query: ' . mysqli_error());
}

$row_cnt = $result->num_rows;

if ($row_cnt > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo '<tr><td>' . $row['id']. '</td><td> '. $row['last_seen'].'</td><td> '. $row['version'].'</td><td> '. $row['cpu'].'</td><td> '. $row['pc_name'].'</td><td> '. $row['product_name'].'</td><td> '. $row['arch'].'</td><td> '. $row['RAM'].'</td><td> '. $row['mac_wlan'].'</td><td> '. $row['mac_eth'].'</td><td> ' . $row['oem_key']. '</td></tr>';
    }
} else {
    echo 'No hi ha entrades';
}
?></table>
    </body>


</html>
