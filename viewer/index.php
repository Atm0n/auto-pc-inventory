

<html>
    <head><title>Visor Inventari</title>
    <link rel="stylesheet" type="text/css" href="style.css">
<script language="javascript" type="text/javascript" src="actb.js"></script><!-- External script -->
<script language="javascript" type="text/javascript" src="tablefilter.js"></script>
</head>
    <body>
<?php $password = "admin";?>
<?php 
// If password is valid let the user get access
if (isset($_POST["password"]) && ($_POST["password"]=="$password")) {
?>
<table id="table1" class="mytable" >
  <tr>
    <th>id</th>
    <th>last_seen</th> 
    <th>version</th>
      <th>cpu</th>
      <th>pc_name</th>
      <th>product_name</th>
      <th>arch</th>
      <th>RAM</th>
      <th>mac_wlan</th>
      <th>mac_eth</th>
      <th>oem_key</th>
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


<script language="javascript" type="text/javascript">
//<![CDATA[
	setFilterGrid( "table1" );
//]]>
</script>
<?php 
}
else
{
// Wrong password or no password entered display this message
if (isset($_POST['password']) || $password == "") {
  }
  print "<form method=\"post\"><p align=\"center\">Please enter your password for access<br>";
  print "<input name=\"password\" type=\"password\" size=\"25\" maxlength=\"10\"><input value=\"Login\" type=\"submit\"></p></form>";
}
  
?>
    </body>


</html>
