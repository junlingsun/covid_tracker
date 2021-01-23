var l1_chart = echarts.init(document.getElementById('l1'));

update_l1_data()

function update_l1_data(){
        $.ajax({
            url: "/l1",
            timeout: 1000,
            success: function(data) {
                console.log(data)

                load_chart(data.x_data, data.legend, data.positive_data, data.death_data);
            },
            error:function(xhr, type, errorThrown){
            }
        });
    }




function load_chart(x_data, legend_data, positive_data, death_data) {
    l1_option = {
    color: ["green", "red"],
    title: {
        text: 'Cumulative spread',
        textStyle: {
            color:'grey',
            fontStyle: 'italic',
            fontSize: 15
        },
        left:"center",
        top: "0%"
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        type:"scroll",
        data: legend_data,
        left: "35%",
        top: "8%",
        itemGap: 0.5,
        textStyle: {
            fontSize: 8,
            color: 'grey',
        },


    },
    grid: {
        left: '3%',
        right: '5%',
        bottom: '3%',
        containLabel: true,
        show:true,
        borderColor: "black"

    },

    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: x_data,
        axisLabel: {
            fontSize: 8,
            color: "red",
        },
        axisLine: {
            show: false
        },
        splitLine: {
            show: false
        }


    },
    yAxis: {
        type: 'value',
        splitLine: {
            show: false
        }

    },
    series: [
        {
            name: 'positive',
            type: 'line',

            data: positive_data
        },
        {
            name: 'death',
            type: 'line',

            data: death_data
        }
    ]
};

l1_chart.setOption(l1_option);
}



