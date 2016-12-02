<?php
	$dbhost = 'localhost';
	$dbuser = 'root';
	$dbpass = 'raspberry';
	
	$db = 'Sensor_Statistics';
	$conn = mysql_connect($dbhost,$dbuser,$dbpass);
	mysql_select_db($db);
?>
