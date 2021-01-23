

data = [
                    {name : 'Alabama', value : 4822023},
                    {name : 'Alaska', value : 731449},
                    {name : 'Arizona', value : 6553255},
           ]


update_c2_data()
function update_c2_data(){
        $.ajax({
            url: "/c2",
            timeout: 1000,
            success: function(response) {

                loading_map(response.response)
            },
            error:function(xhr, type, errorThrown){
            }
        });
    }

//setInterval(update_c2_data, 1000)


function loading_map(my_data) {
    var myChart = echarts.init(document.getElementById('main'));
    $.get('https://s3-us-west-2.amazonaws.com/s.cdpn.io/95368/USA_geo.json', function (usaJson) {
    myChart.hideLoading();

    echarts.registerMap('USA', usaJson, {
        Alaska: {              // 把阿拉斯加移到美国主大陆左下方
            left: -131,
            top: 25,
            width: 15
        },
        Hawaii: {
            left: -110,        // 夏威夷
            top: 28,
            width: 5
        },
        'Puerto Rico': {       // 波多黎各
            left: -76,
            top: 26,
            width: 2
        }
    });
    option = {
        title : {

        },
        tooltip : {
            trigger: 'item',
            showDelay: 0,
            transitionDuration: 0.2,
            formatter : function (params) {
                var value = (params.value + '').split('.');
                value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,');
                return params.seriesName + '<br/>' + params.name + ' : ' + value;
            }
        },
        visualMap: {
            show: false,
            left: 'right',
            min: 50000,
            max: 3000000,
            color: ['red','pink','yellow','orange', 'lightskyblue'],
            text:['High','Low'],           // 文本，默认为数值文本
            calculable : true
        },
        toolbox: {
            show : false,
            //orient : 'vertical',
            left: '0%',
            right: '10%',
            top: 'top',
            feature : {
                mark : {show: true},
                dataView : {show: true, readOnly: false},
                restore : {show: true},
                saveAsImage : {show: true}
            }
        },
        series : [
            {
                name: 'positive cases',
                type: 'map',
                roam: false,
                map: 'USA',
                itemStyle:{
                    emphasis:{label:{show:true}}
                },
                // 文本位置修正
                textFixed : {
                    Alaska : [20, -20]
                },
                data:my_data
            }
        ]
    };

	    myChart.setOption(option);
});
}


