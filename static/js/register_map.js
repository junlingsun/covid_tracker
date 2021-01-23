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