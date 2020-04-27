function lifeStyleCdrCallsOfferedCharts(lst){

    // Load google charts
        google.charts.load('current', {'packages':['corechart']});
        google.charts.setOnLoadCallback(drawChart);

        // Draw the chart and set the chart values
        function drawChart() {
          var data = google.visualization.arrayToDataTable([
          ['Time', 'Count Of Calls', {type: 'number', role: 'annotation'}],
          ['10 AM-11 AM', lst[0], lst[0]],
          ['11 AM-12 PM', lst[1], lst[1]],
          ['12 PM-1 PM', lst[2], lst[2]],
          ['1 PM-2 PM', lst[3], lst[3]],
          ['2 PM-3 PM', lst[4], lst[4]],
          ['3 PM-4 PM', lst[5], lst[5]],
          ['4 PM-5 PM', lst[6], lst[6]],
          ['5 PM-6 PM', lst[7], lst[7]],
          ['6 PM-7 PM', lst[8], lst[8]],
          ['7 PM-8 PM', lst[9], lst[9]],
          ['8 PM-9 PM', lst[10], lst[10]],
          ['9 PM-10 PM', lst[11], lst[11]]
        ]);

          // Optional; add a title and set the width and height of the chart
          var options = {title: 'Lifestyle CDR Calls Offered', width: 1500, height: 300,
            legend: { position: 'top', maxLines: 3 },
            chartArea:{left:100, right:100},
            hAxis: {
                title: 'Hourly Time',
                viewWindow: {
                    min: [20, 50, 0],
                    max: [27, 70, 0]
                }
            },
            vAxes: {
             // Adds titles to each axis.
                0: {title: 'Count'},
                1: {title: ''}
            }
          };

          // Display the chart inside the <div> element with id="calls_offered_chart"
          var chart = new google.visualization.ColumnChart(document.getElementById('calls_offered_chart'));
          chart.draw(data, options);
        }
    };


function lifeStyleCdrCallsAnsCharts(lst1,lst2){
    // Load google charts
         // Load google charts
        google.charts.load('current', {'packages':['corechart']});
        google.charts.setOnLoadCallback(drawChart);

        // Draw the chart and set the chart values
        function drawChart() {
          var data = google.visualization.arrayToDataTable([
          ['Time', 'Count Of Calls', {type: 'number', role: 'annotation'}, 'Percentage Of Calls', {type: 'number', role: 'annotation'}],
          ['10 AM-11 AM', lst1[0], lst1[0], lst2[0], lst2[0]],
          ['11 AM-12 PM', lst1[1], lst1[1], lst2[1], lst2[1]],
          ['12 PM-1 PM', lst1[2], lst1[2], lst2[2], lst2[2]],
          ['1 PM-2 PM', lst1[3], lst1[3], lst2[3], lst2[3]],
          ['2 PM-3 PM', lst1[4], lst1[4], lst2[4], lst2[4]],
          ['3 PM-4 PM', lst1[5], lst1[5], lst2[5], lst2[5]],
          ['4 PM-5 PM', lst1[6], lst1[6], lst2[6], lst2[6]],
          ['5 PM-6 PM', lst1[7], lst1[7], lst2[7], lst2[7]],
          ['6 PM-7 PM', lst1[8], lst1[8], lst2[8], lst2[8]],
          ['7 PM-8 PM', lst1[9], lst1[9], lst2[9], lst2[9]],
          ['8 PM-9 PM', lst1[10], lst1[10], lst2[10], lst2[10]],
          ['9 PM-10 PM', lst1[11], lst1[11], lst2[11], lst2[11]]
        ]);

        var classicOptions = {
          chartArea:{left:100, right:100},
          height: 400,
          colors: ['#9575cd', '#33ac71'],
          series: {
            0: {targetAxisIndex: 0},
            1: {targetAxisIndex: 1}
          },
          title: 'Lifestyle Inbound Calls Answered',
          vAxes: {
            // Adds titles to each axis.
            0: {title: 'Count'},
            1: {title: 'Percentage'}
          },
          hAxis:{
            title: 'Hourly Time'
            }
        };
          var chartDiv = document.getElementById('calls_ans_chart')
          var classicChart = new google.visualization.ColumnChart(chartDiv);
          classicChart.draw(data, classicOptions);
        }
    };


function lifeStyleServiceLevelCallsCharts(lst1, lst2){
    // Load google charts
        google.charts.load('current', {'packages':['corechart']});
        google.charts.setOnLoadCallback(drawChart);

        // Draw the chart and set the chart values
        function drawChart() {
          var data = google.visualization.arrayToDataTable([
          ['Time', 'Count Of Calls', {type: 'number', role: 'annotation'}, 'Percentage Of Calls', {type: 'number', role:'annotation'}],
          ['10 AM-11 AM', lst1[0], lst1[0], lst2[0], lst2[0]],
          ['11 AM-12 PM', lst1[1], lst1[1], lst2[1], lst2[1]],
          ['12 PM-1 PM', lst1[2], lst1[2], lst2[2], lst2[2]],
          ['1 PM-2 PM', lst1[3], lst1[3], lst2[3], lst2[3]],
          ['2 PM-3 PM', lst1[4], lst1[4], lst2[4], lst2[4]],
          ['3 PM-4 PM', lst1[5], lst1[5], lst2[5], lst2[5]],
          ['4 PM-5 PM', lst1[6], lst1[6], lst2[6], lst2[6]],
          ['5 PM-6 PM', lst1[7], lst1[7], lst2[7], lst2[7]],
          ['6 PM-7 PM', lst1[8], lst1[8], lst2[8], lst2[8]],
          ['7 PM-8 PM', lst1[9], lst1[9], lst2[9], lst2[9]],
          ['8 PM-9 PM', lst1[10], lst1[10], lst2[10], lst2[10]],
          ['9 PM-10 PM', lst1[11], lst1[11], lst2[11], lst2[11]]
        ]);

        var classicOptions = {
          chartArea:{left:100, right:100},
          height: 400,
          colors: ['#008080','#FF8C00'],
          series: {
            0: {targetAxisIndex: 0},
            1: {targetAxisIndex: 1}
          },
          title: 'Lifestyle Inbound Service Level Calls Answered',
          vAxes: {
            // Adds titles to each axis.
            0: {title: 'Count'},
            1: {title: 'Percentage'}
          },
          hAxis:{
            title: 'Hourly Time'
          }
        };
          var chartDiv = document.getElementById('service_level_calls_chart')
          var classicChart = new google.visualization.ColumnChart(chartDiv);
          classicChart.draw(data, classicOptions);
        }
    };


function abandonedCallsCharts(lst1, lst2){
    // Load google charts
        google.charts.load('current', {'packages':['corechart']});
        google.charts.setOnLoadCallback(drawChart);

        // Draw the chart and set the chart values
    function drawChart() {
          var data = google.visualization.arrayToDataTable([
          ['Time', 'Count Of Calls', {type: 'number', role: 'annotation'}, 'Percentage Of Calls', {type: 'number', role: 'annotation'}],
          ['10 AM-11 AM', lst1[0], lst1[0], lst2[0], lst2[0]],
          ['11 AM-12 PM', lst1[1], lst1[1], lst2[1], lst2[1]],
          ['12 PM-1 PM', lst1[2], lst1[2], lst2[2], lst2[2]],
          ['1 PM-2 PM', lst1[3], lst1[3], lst2[3], lst2[3]],
          ['2 PM-3 PM', lst1[4], lst1[4], lst2[4], lst2[4]],
          ['3 PM-4 PM', lst1[5], lst1[5], lst2[5], lst2[5]],
          ['4 PM-5 PM', lst1[6], lst1[6], lst2[6], lst2[6]],
          ['5 PM-6 PM', lst1[7], lst1[7], lst2[7], lst2[7]],
          ['6 PM-7 PM', lst1[8], lst1[8], lst2[8], lst2[8]],
          ['7 PM-8 PM', lst1[9], lst1[9], lst2[9], lst2[9]],
          ['8 PM-9 PM', lst1[10], lst1[10], lst2[10], lst2[10]],
          ['9 PM-10 PM', lst1[11], lst1[11], lst2[11], lst2[11]]
        ]);

        var classicOptions = {
          chartArea:{left:100, right:100},
          height: 400,
          series: {
            0: {targetAxisIndex: 0},
            1: {targetAxisIndex: 1}
          },
          title: 'Lifestyle Inbound Abandoned Calls',
          vAxes: {
            // Adds titles to each axis.
            0: {title: 'Count'},
            1: {title: 'Percentage'}
          },
          hAxis:{
            title: 'Hourly Time'
          }
        };
          var chartDiv = document.getElementById('abandoned_calls_chart')
          var classicChart = new google.visualization.ColumnChart(chartDiv);
          classicChart.draw(data, classicOptions);
        }
    };



var offeredCalls = 0; var AnsCalls = 0; var serviceLevelCalls = 0; var abandoned = 0; var date = 0;
async function lifeStyleFinalLineChartsByDate(lst,res){

    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
        if(res === 1) {
            lst.length = lst["length"]-1
            offeredCalls = lst;
        }
        if(res === 2) {
            lst.length = lst["length"]-1
            AnsCalls = lst;
        }
        if(res === 3) {
            lst.length = lst["length"]-1
            serviceLevelCalls = lst;
        }
        if(res === 4) {
            lst.length = lst["length"]-1
            abandoned = lst;
        }
        if(res === 5) {
            lst.length = lst["length"]-1
            date = lst;
        }

    if (offeredCalls && AnsCalls && serviceLevelCalls){
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Date');
      data.addColumn('number', 'Calls Offered');
      data.addColumn({type:'number', role: 'annotation'});
      data.addColumn('number', 'Service Level Calls Answered');
      data.addColumn({type:'number', role: 'annotation'});
      data.addColumn('number', 'Calls Answered');
      data.addColumn({type:'number', role: 'annotation'});
      data.addColumn('number', 'Abandoned');
      data.addColumn({type:'number', role: 'annotation'});
      graphWidth = 0;
      for (var i = 0; i < date.length; i ++){
      data.addRows([
        [date[i],  offeredCalls[i], offeredCalls[i],  serviceLevelCalls[i], serviceLevelCalls[i], AnsCalls[i], AnsCalls[i], abandoned[i], abandoned[i]]
      ]);
      graphWidth += 100
};


      var options = {
      height: 500,
      width: 300 + graphWidth,
      colors: ['#800000', '#008080', '#483D8B', '#FF0000'],
      chartArea:{left:100, right:100},
      bar: { groupWidth: '60%' },
      title: 'Lifestyle CDR Inbound Performance',
      series: {
        0: {targetAxisIndex: 0},
        1: {targetAxisIndex: 1}
      },
      vAxes: {
        // Adds titles to each axis.
        0: {title: 'Count'},
        1: {title: 'Count'}
      },
      hAxis: {
          title: 'Date',
          viewWindow: {
            min: [7, 30, 0],
            max: [17, 30, 0]
          }
      },
    };

//        var options = {
//        height: 500,
//        width: 300 + graphWidth,
//        chartArea:{left:50, right:10},
//        colors: ['#800000', '#8B4513', '#DEB887', '#FF0000'],
//        legend: { position: 'top', maxLines: 3 },
//        bar: { groupWidth: '60%' },
//        title: 'Lifestyle CDR Inbound Performance',
//        isStacked: true,
//        hAxis: {
//          title: 'Date',
//          viewWindow: {
//            min: [7, 30, 0],
//            max: [17, 30, 0]
//          }
//        },
//      };

      var chart =  new google.visualization.ColumnChart(document.getElementById('line'));
      chart.draw(data, options);
    }
    }
};


//-------------------------------------------------------------------------------------------------------------------