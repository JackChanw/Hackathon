/**
 * @name lightmoon
 * @overview
 * @author Woodu <woodu-noreply@domob.cn>
 * @2016/12/9.
 * uses old echarts2 and jquery.
 * 愉快な世界で皆　Drink a toast!　DANCE DANCE DANCE!
 */
/* 初始化maps区域，在bootstrap下面会有高度自动这个问题 */
var tempMediaIdToName = ['DVX', '首席体验师', '现场活动'];
var resizeMap = function () {
  var nowheight = $(document).height();
  console.log(nowheight);
  jQuery('#map').css('height', nowheight);
};
$(window).resize(resizeMap);
resizeMap();
/* baidu maps */
var option = {
  backgroundColor: '#0068b7',
  color: ['gold', 'aqua', 'lime'],
  title: {
    text: '',
    subtext: '',
    x: 'center',
    textStyle: {
      color: '#fff'
    }
  },
  tooltip: {
    trigger: 'item',
    formatter: '{b}'
  },
  legend: {
    show: false,
    orient: 'vertical',
    x: 'right',
    data: ['北京 Top10'],
    selectedMode: 'single',
    selected: {},
    textStyle: {
      color: '#fff'
    }
  },
  toolbox: {
    show: true,
    orient: 'vertical',
    x: 'right',
    y: 'center',
    feature: {
      mark: {show: false},
      dataView: {show: false, readOnly: false},
      restore: {show: true},
      saveAsImage: {show: false}
    }
  },
  dataRange: {
    show: false,
    min: 0,
    max: 100,
    calculable: true,
    color: ['#fff', '#67EEBA', '#ffba00'],
    textStyle: {
      color: '#fff'
    }
  },
  series: [
    {
      name: '全国',
      type: 'map',
      roam: true,
      hoverable: false,
      mapType: 'china',
      itemStyle: {
        normal: {
          borderColor: 'rgba(2,83,25,1)',
          borderWidth: 1,
          areaStyle: {
            color: '#0068b7'
          }
        }
      },
      data: [],
      markLine: {
        smooth: true,
        symbol: ['none', 'circle'],
        symbolSize: 1,
        itemStyle: {
          normal: {
            color: '#fff',
            borderWidth: 1,
            borderColor: 'rgba(2,83,145,1)'
          }
        },
        data: []
      },
      geoCoord: {
        '上海': [121.4648, 31.2891],
        '东莞': [113.8953, 22.901],
        '东营': [118.7073, 37.5513],
        '中山': [113.4229, 22.478],
        '临汾': [111.4783, 36.1615],
        '临沂': [118.3118, 35.2936],
        '丹东': [124.541, 40.4242],
        '丽水': [119.5642, 28.1854],
        '乌鲁木齐': [87.9236, 43.5883],
        '佛山': [112.8955, 23.1097],
        '保定': [115.0488, 39.0948],
        '兰州': [103.5901, 36.3043],
        '包头': [110.3467, 41.4899],
        '北京': [116.4551, 40.2539],
        '北海': [109.314, 21.6211],
        '南京': [118.8062, 31.9208],
        '南宁': [108.479, 23.1152],
        '南昌': [116.0046, 28.6633],
        '南通': [121.1023, 32.1625],
        '厦门': [118.1689, 24.6478],
        '台州': [121.1353, 28.6688],
        '合肥': [117.29, 32.0581],
        '呼和浩特': [111.4124, 40.4901],
        '咸阳': [108.4131, 34.8706],
        '哈尔滨': [127.9688, 45.368],
        '唐山': [118.4766, 39.6826],
        '嘉兴': [120.9155, 30.6354],
        '大同': [113.7854, 39.8035],
        '大连': [122.2229, 39.4409],
        '天津': [117.4219, 39.4189],
        '太原': [112.3352, 37.9413],
        '威海': [121.9482, 37.1393],
        '宁波': [121.5967, 29.6466],
        '驻马店': [114.0200, 32.9800],
        '洛阳': [112.434468 , 34.663041],
        '宝鸡': [107.1826, 34.3433],
        '宿迁': [118.5535, 33.7775],
        '常州': [119.4543, 31.5582],
        '广州': [113.5107, 23.2196],
        '廊坊': [116.521, 39.0509],
        '延安': [109.1052, 36.4252],
        '张家口': [115.1477, 40.8527],
        '徐州': [117.5208, 34.3268],
        '德州': [116.6858, 37.2107],
        '惠州': [114.6204, 23.1647],
        '成都': [103.9526, 30.7617],
        '扬州': [119.4653, 32.8162],
        '承德': [117.5757, 41.4075],
        '拉萨': [91.1865, 30.1465],
        '无锡': [120.3442, 31.5527],
        '日照': [119.2786, 35.5023],
        '昆明': [102.9199, 25.4663],
        '杭州': [119.5313, 29.8773],
        '枣庄': [117.323, 34.8926],
        '柳州': [109.3799, 24.9774],
        '株洲': [113.5327, 27.0319],
        '武汉': [114.3896, 30.6628],
        '汕头': [117.1692, 23.3405],
        '江门': [112.6318, 22.1484],
        '沈阳': [123.1238, 42.1216],
        '沧州': [116.8286, 38.2104],
        '河源': [114.917, 23.9722],
        '泉州': [118.3228, 25.1147],
        '泰安': [117.0264, 36.0516],
        '泰州': [120.0586, 32.5525],
        '济南': [117.1582, 36.8701],
        '济宁': [116.8286, 35.3375],
        '海口': [110.3893, 19.8516],
        '淄博': [118.0371, 36.6064],
        '淮安': [118.927, 33.4039],
        '深圳': [114.5435, 22.5439],
        '清远': [112.9175, 24.3292],
        '温州': [120.498, 27.8119],
        '渭南': [109.7864, 35.0299],
        '湖州': [119.8608, 30.7782],
        '湘潭': [112.5439, 27.7075],
        '滨州': [117.8174, 37.4963],
        '潍坊': [119.0918, 36.524],
        '烟台': [120.7397, 37.5128],
        '玉溪': [101.9312, 23.8898],
        '珠海': [113.7305, 22.1155],
        '盐城': [120.2234, 33.5577],
        '盘锦': [121.9482, 41.0449],
        '石家庄': [114.4995, 38.1006],
        '福州': [119.4543, 25.9222],
        '秦皇岛': [119.2126, 40.0232],
        '绍兴': [120.564, 29.7565],
        '聊城': [115.9167, 36.4032],
        '肇庆': [112.1265, 23.5822],
        '舟山': [122.2559, 30.2234],
        '苏州': [120.6519, 31.3989],
        '莱芜': [117.6526, 36.2714],
        '菏泽': [115.6201, 35.2057],
        '营口': [122.4316, 40.4297],
        '葫芦岛': [120.1575, 40.578],
        '衡水': [115.8838, 37.7161],
        '衢州': [118.6853, 28.8666],
        '西宁': [101.4038, 36.8207],
        '西安': [109.1162, 34.2004],
        '贵阳': [106.6992, 26.7682],
        '连云港': [119.1248, 34.552],
        '邢台': [114.8071, 37.2821],
        '邯郸': [114.4775, 36.535],
        '郑州': [113.4668, 34.6234],
        '鄂尔多斯': [108.9734, 39.2487],
        '重庆': [107.7539, 30.1904],
        '金华': [120.0037, 29.1028],
        '铜川': [109.0393, 35.1947],
        '银川': [106.3586, 38.1775],
        '镇江': [119.4763, 31.9702],
        '长春': [125.8154, 44.2584],
        '长沙': [113.0823, 28.2568],
        '长治': [112.8625, 36.4746],
        '阳泉': [113.4778, 38.0951],
        '青岛': [120.4651, 36.3373],
        '韶关': [113.7964, 24.7028]
      }
    },
    {
      name: '北京 Top10',
      type: 'map',
      mapType: 'china',
      data: [],
      markLine: {
        smooth: true,
        effect: {
          show: true,
          scaleSize: 1,
          period: 30,
          color: '#fff',
          shadowBlur: 10
        },
        itemStyle: {
          normal: {
            borderWidth: 1,
            lineStyle: {
              type: 'solid',
              shadowBlur: 10
            }
          }
        },
        data: []
      },
      markPoint: {
        symbol: 'emptyCircle',
        symbolSize: function (v) {
          return 10 + v / 10
        },
        effect: {
          show: true,
          shadowBlur: 0
        },
        itemStyle: {
          normal: {
            label: {show: false}
          },
          emphasis: {
            label: {position: 'top'}
          }
        },
        data: []
      }
    }
  ]
};
var lightmoon = echarts.init(document.getElementById('map'));
var lineGroups = [];
var rawLineGroups = [];
lightmoon.setOption(option);
/*画画函数*/
var drawFunc = function (getdatasettings) {
  jQuery.when(jQuery.ajax(getdatasettings)).done(function (data) {
    var firstAdd = false;
    //更新图表
    if (data.length > 0) {
      var text = data;
      // console.log(data.length);
      jQuery.each(text, function (index, data, array) {
        // console.log(data);
        jQuery.each(data.value, function (index, data, array) {
          if (rawLineGroups.length <= 300) rawLineGroups.push(data);
        });

      });
      drawLineToPicture();
    }
    // console.log(option.series[1].markLine.data);
  });
  // console.info(rawLineGroups.length, lineGroups.length);
};
var drawLineToPicture = function () {
  var waitToDraw = 0;
  if (rawLineGroups.length > 275) {
    waitToDraw = (rawLineGroups.length - 275);
  } else {
    waitToDraw = 50;
  }
  for (var i = 0; i < waitToDraw; i++) {
    setTimeout(function () {
      data = rawLineGroups.shift();
      if (typeof(data) != 'undefined') {
        lightmoon.addMarkLine(1, {
          smooth: true,
          effect: {
            show: true,
            scaleSize: 1,
            period: 30,
            color: '#fff',
            shadowBlur: 10
          },
          itemStyle: {
            normal: {
              borderWidth: 1,
              lineStyle: {
                type: 'solid',
                shadowBlur: 10
              },
              label: false
            }
          },
          data: [data]
        });
        //给起止点增加圈
        lightmoon.addMarkPoint(0, {
          symbol: 'emptyCircle',
          symbolSize: function (v) {
            return 10 + v / 10
          },
          effect: {
            show: true,
            loop: false,
            shadowBlur: 0,
          },
          itemStyle: {
            normal: {
              label: {show: false}
            }
          },
          data: [data[0]]
        }, 2000);
        lightmoon.addMarkPoint(0, {
          symbol: 'emptyCircle',
          symbolSize: function (v) {
            return 10 + v / 10
          },
          effect: {
            show: true,
            loop: false,
            shadowBlur: 0,
          },
          itemStyle: {
            normal: {
              label: {show: false}
            }
          },
          data: [data[1]]
        }, 2000);
        data.addtime = (new Date()).valueOf();
        lineGroups.push(data);
      }
    }, Math.floor(Math.random() * 4000 + 1));

  }

};
var delFunc = function () {
  //循环删除过期的线
  if (lineGroups.length > 10) {
    jQuery.each(lineGroups, function (index, data, array) {
      if (typeof(data) != "undefined") if (data.addtime < ((new Date()).valueOf() - 2000)) {
        if (typeof(lineGroups[0][0].name) == 'undefined') {
          lineGroups.shift();
          return true;
        }
        var todelete = lineGroups[0][0].name + " > " + lineGroups[0][1].name;
        lightmoon.delMarkLine(1, todelete);
        lightmoon.delMarkPoint(1, lineGroups[0][0].name);
        lightmoon.delMarkPoint(1, lineGroups[0][1].name);
        lineGroups.shift();
      }
    });
  }
};
var infoWall = [];
// var infoWallOnWall = [];
var drawText = function (getdatasettings) {
  jQuery.when(jQuery.ajax(getdatasettings)).done(function (data) {
    jQuery.each(data, function (index, data, array) {

      if(infoWall.length < 200 && data.value.length>0){
        jQuery.each(data.value,function(index,data,array){
          infoWall.push(data);
        });
      }
    });
  });
};

var drawInfoWall = function(){
  if(infoWall.length > 0){
    $tobeDisplayed = infoWall.length > 10 ? 10:infoWall.length;
    // if(infoWall.length > 20) $tobeDisplayed = infoWall.length - 10;
    for(var i = 0;i<$tobeDisplayed;i++){
      $.infobox.show(infoWall.shift());
    }
  }

};

$.infobox = {
  show: function(e, t, n) {
    var a = $("#info-box")
      , i = n ? n : "info"
      , r = $('<p class="info ' + n + '"><i class="icon icon-' + i + '"></i><span>' + e + "</span></p>");
    return a.append(r),
      r.animate({
        right: 0
      }, 300),
      setTimeout(function() {
        r.animate({
          right: "-100%"
        }, 300, function() {
          r.remove()
        })
      }, t || 1500),
      this
  },
  error: function(e, t) {
    return this.show(e, t, "error")
  },
  warning: function(e, t) {
    return this.show(e, t, "warning")
  },
  success: function(e, t) {
    return this.show(e, t, "success")
  }
};

var formatNumber = function (num) {
  if (!/^(\+|-)?(\d+)(\.\d+)?$/.test(num)) {
    return num;
  }
  var a = RegExp.$1, b = RegExp.$2, c = RegExp.$3;
  var re = new RegExp("(\\d)(\\d{3})(,|$)");
  while (re.test(b))   b = b.replace(re, "$1,$2$3");
  return a + "" + b + "" + c;
};
var updateAppsInfo = function () {
  jQuery.when(jQuery.ajax('//lightmoon.moxz.cn/redis/GET/key_1_event_share'),
    jQuery.ajax('//lightmoon.moxz.cn/redis/GET/key_2_event_share'),
    jQuery.ajax('//lightmoon.moxz.cn/redis/GET/key_3_event_share'),
    jQuery.ajax('//lightmoon.moxz.cn/redis/GET/key_events')).done(function (a, b, c, d) {
    jQuery('#text-line-1').html(tempMediaIdToName[0] + "的总消耗量：" + parseFloat(a[0]['GET'], 2).toFixed(2));
    jQuery('#text-line-2').html(tempMediaIdToName[1] + "的总消耗量：" + parseFloat(b[0]['GET'], 2).toFixed(2));
    jQuery('#text-line-3').html(tempMediaIdToName[2] + "的总消耗量：" + parseFloat(c[0]['GET'], 2).toFixed(2));
    jQuery('#text-line-4').html("<span class='text-line-x1'>总计观察数据</span><br /><span class='text-line-x2'>" + formatNumber(parseFloat(d[0]['GET'], 2))+"</span><br /><span class='text-line-x3'>自2016-12-08起</span></span>");
  });
};

jQuery(document).ready(function () {
  //kafka部分，注册consumer并开始刷数据
  var consumerName = "lightmoon_instance_" + (new Date()).valueOf();
  var consumerInfo = [];
  var settings = {
    type: "POST",
    url: '//lightmoon.moxz.cn/kafka/consumers/' + consumerName,
    data: JSON.stringify({"name": consumerName, "format": "json", "auto.offset.reset": "largest"}),
    dataType: 'json',
    contentType: 'application/json; charset=utf-8',
    headers: {
      'Content-Type': 'application/vnd.kafka.v1+json',
    },
    success: function (data) {
      consumerInfo = data;
      // console.log(data);
      var getdatasettings = {
        type: "GET",
        url: '//lightmoon.moxz.cn/kafka/consumers/' + consumerName + '/instances/' + consumerName + '/topics/lightmoon_test_2',
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        headers: {
          'Accept': 'application/vnd.kafka.json.v1+json',
          'Content-Type': 'application/vnd.kafka.v1+json',
        }
      };
      drawFunc(getdatasettings);
      updateAppsInfo();
      setInterval(function () {
        drawFunc(getdatasettings)
      }, 2000);
      setInterval(delFunc, 2000);
      setInterval(updateAppsInfo, 5000);
    }
  };

  $.ajax(settings);//.then(Start-to-draw).
});
//consumer-2
jQuery(document).ready(function () {
  //kafka部分，注册consumer并开始刷数据
  var consumerName = "lightmoon_instance2_" + (new Date()).valueOf();
  var consumerInfo = [];
  var settings = {
    type: "POST",
    url: '//lightmoon.moxz.cn/kafka/consumers/' + consumerName,
    data: JSON.stringify({"name": consumerName, "format": "json", "auto.offset.reset": "largest"}),
    dataType: 'json',
    contentType: 'application/json; charset=utf-8',
    headers: {
      'Content-Type': 'application/vnd.kafka.v1+json',
    },
    success: function (data) {
      consumerInfo = data;
      // console.log(data);
      var getdatasettings = {
        type: "GET",
        url: '//lightmoon.moxz.cn/kafka/consumers/' + consumerName + '/instances/' + consumerName + '/topics/lm_message_test_2',
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        headers: {
          'Accept': 'application/vnd.kafka.json.v1+json',
          'Content-Type': 'application/vnd.kafka.v1+json',
        }
      };
      drawText(getdatasettings);
      // updateAppsInfo();
      setInterval(function () {
        drawText(getdatasettings)
      }, 2000);
      setInterval(function(){
        drawInfoWall();
      },1000);
      // setInterval(delFunc, 2000);
      // setInterval(updateAppsInfo, 5000);
    }
  };

  $.ajax(settings);//.then(Start-to-draw).
});