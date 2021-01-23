function getTime(){
        $.ajax({
            url: "/time",
            timeout: 1000,
            success: function(data) {

                $("#time").text(data);
            },
            error:function(xhr, type, errorThrown){
            }
        });
    }

    function update_c1_data(){
        $.ajax({
            url: "/c1",
            timeout: 1000,
            success: function(data) {
                $(".num h1").eq(0).html(Number(data.positive).toLocaleString());
                $(".num h1").eq(1).html(Number(data.death).toLocaleString());
                $(".num b").eq(0).html("+" + Number(data.positive_increase).toLocaleString());
                $(".num b").eq(1).html("+" + Number(data.death_increase).toLocaleString());
            },
            error:function(xhr, type, errorThrown){
            }
        });
    }


setInterval(getTime, 1000)
setInterval(update_c1_data, 1000)