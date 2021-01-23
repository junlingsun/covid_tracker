var r1_chart = echarts.init(document.getElementById('r1'));

update_r1_data()

function update_r1_data(){
        $.ajax({
            url: "/r1",
            timeout: 1000,
            success: function(data) {
                load_r1_chart(data.names, data.positive);
            },
            error:function(xhr, type, errorThrown){
            }
        });
    }




function load_r1_chart(names, positive) {
    r1_option = {
            title: {
                text: 'TOP 10 STATES',
                textStyle: {
                    color:'grey',
                    fontStyle: 'italic',
                    fontSize: 20
                },
                left:"center",
                top: "20%"
            },
            color: ["#3398DB"],
            xAxis: {
                type: 'category',
                data: names,
                splitLine: {
                    show: false
                }
            },
            tooltip: {
                trigger: "axis",
                axisPointer: {
                  type: "shadow"
                }
              },
            yAxis: {
                type: 'value',
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            series: [{
                name: "POSITIVE CASES",
                type: "bar",
                data: positive,
            }]
        };

    r1_chart.setOption(r1_option);
}



