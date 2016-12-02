<?php
$con = mysql_connect("localhost","root","raspberry");
if (!$con) {
die('Could not connect: ' . mysql_error());
}
mysql_select_db("Sensor_Statistics", $con);
$result = mysql_query("SELECT * FROM `Sensors1` WHERE Node_no=1 ") or die ("Connection error");
while($row = mysql_fetch_array($result)) {
echo $row['time_stamp'] . "/" . $row['Temp']. "/" ;
}
mysql_close($con);
?>
