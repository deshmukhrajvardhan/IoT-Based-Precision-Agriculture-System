<?php
        include 'con.php';
/*
<h1>Create A User</h1>
<form action="create.php" method = "post">
        <input type="text" name="inputName" value=""/>
        <input type="text" name="inputName" value=""/>
        <br/>
        <input type="submit" name="submit" value=""/>
</form>
*/      $query = "SELECT * FROM  Sensors1 ORDER BY Id_no DESC";
        $result= mysql_query($query);
        $sp='&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;';
        echo "<h1>" . 'Precision Agriculture' . "</h1>";
        echo "<h2>" .' Id ' . ' Node_no. ' .'&nbsp;&nbsp;&nbsp'. ' Time_Stamp ' .'&nbsp;&nbsp;&nbsp;&nbsp;'.$sp.'Crop'.'&nbsp;&nbsp;'.' Temp(C) ' . 'Light_Intensity'. ' Moisture ' .'&nbsp;' .' pH '.'&nbsp;&nbsp;'.' Lime Required'.'&nbsp;&nbsp;'.'Nodes down'. "</h2>";
        while($sensor_values = mysql_fetch_array($result)){
//      echo "<h1>" . 'Percision Agriculture' . "</h1>";
//      echo "<h2>" . 'Id_no. ' . ' Node_no. ' .'&nbsp;&nbsp;&nbsp'. ' Time_Stamp ' .'&nbsp;&nbsp;&nbsp;&nbsp;'. ' Temperature ' . ' Light_Inte$
        echo "<h3>" .'&nbsp;'.$sensor_values['Id_no'] .$sp.'  '. $sensor_values['Node_no'] .$sp.$sp. $sensor_values['time_stamp'].$sp.'&nbsp;&nbsp;&nbsp;&nbsp;'.$sensor_values['Crop'].$sp.$sp. $sensor_values['Temp'] .$sp.$sp.$sp. $sensor_values['light_Intensity'] .$sp.$sp.$sensor_values['moisture'].$sp.$sensor_values['pH'].$sp.$sp.$sensor_values['lime_req'].$sp.$sp.$sp.$sensor_values['nodes_down']. "</h3>";
//      echo "<p>" . $sensor_values['Node no.'] . "</p>";
}

?>

