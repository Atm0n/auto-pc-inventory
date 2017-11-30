<html>
    <head><title>Visor Inventari</title>
    <link rel="stylesheet" type="text/css" href="style.css"></head>
    <body>
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
        echo '<hr><h1 class="blogtitol">' . $row['titol']. '</h1><br> ' . $row['contingut']. '<br>';
    }
} else {
    echo 'No hi ha entrades';
}
?>
    </body>


</html>
