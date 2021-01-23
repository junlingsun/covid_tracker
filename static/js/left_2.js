var l2_chart = echarts.init(document.getElementById('l2'));

update_l2_data()

function update_l2_data(){
        $.ajax({
            url: "/l2",
            timeout: 1000,
            success: function(data) {
                load_l2_chart(data.x_data, data.legend, data.positive_data, data.death_data);
            },
            error:function(xhr, type, errorThrown){
            }
        });
    }




function load_l2_chart(x_data, legend_data, positive_data, death_data) {
    l2_option = {
    color: ["pink", "gold"],
    title: {
        text: 'Daily Increase',
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
            name: 'positive_increase',
            type: 'line',

            data: positive_data,
            color: "green"
        },
        {
            name: 'death_increase',
            type: 'line',

            data: death_data
        }
    ]
};

l2_chart.setOption(l2_option);
}



