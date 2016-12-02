$(function() {
 
    var x_values = [];

    var y_values = [];
    var switch1 = true;
    $.get('graph_temp.php', function(data) {
 
        data = data.split('/');
        for (var i in data)
        {
            if (switch1 == true)
            {
                var ts = data[i];
                x_values.push(ts);
                switch1 = false;
            }
            else
            {
                y_values.push(parseFloat(data[i]));
                switch1 = true;
            }
 
        }
        x_values.pop();
 
        $('#chart').highcharts({
            chart : {
                type : 'spline'
            },
            title : {
                text : 'Node 1 Temperature'
            },
            subtitle : {
                text : 'IoT based Precision Farming'
            },
            xAxis : {
                title : {
                    text : 'Time'
                },
                categories : x_values
            },
            yAxis : {
                title : {
                    text : 'Temperature'
                },
                labels : {
                    formatter : function() {
                        return this.value + ' C'
                    }
                }
            },
            tooltip : {
                crosshairs : true,
                shared : true,
                valueSuffix : ''
            },
            plotOptions : {
                spline : {
                    marker : {
                        radius : 4,
                        lineColor : '#666666',
                        lineWidth : 1
                    }
                }
            },
            series : [{
 
                name : 'Temperature',
                data : y_values
            }]
        });
    });
});
 
 
 
function timeConverter(UNIX_timestamp){
  var a = new Date(UNIX_timestamp * 1000);
  var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  var year = a.getFullYear();
  var month = months[a.getMonth()];
  var date = a.getDate();
  var hour = a.getHours();
  var min = a.getMinutes() < 10 ? '0' + a.getMinutes() : a.getMinutes();
  var sec = a.getSeconds() < 10 ? '0' + a.getSeconds() : a.getSeconds();
  var time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec ;
  return time;
}
