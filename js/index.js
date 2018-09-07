$.getScript("https://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js",function(){
    var data=remote_ip_info;
    var city=data.city;
    getWeather(city);
})
function getWeather(city){
    $(".now_city_name").html(city);
    $.ajax({
        url:"https://api.jisuapi.com/weather/query?appkey=f0eefe7b6e598b15&city="+city,
        dataType:"jsonp",
        success:function(r) {
            $(".temp").html(r.result.temp+"℃");
            $(".weather").html(r.result.weather);
            $(".weather_img").html(`<img src="img/weather/${r.result.img}.png">`);
        }
    })}