function onChoiceChange(e){
  symbol = this.value;

  loadData();
};







function loadData(){
// Examples of correct url for api's
// https://www.quandl.com/api/v3/datasets/CME/YWZ2017.json?api_key=zeZW2ba38zkWbmBz_ufL
// https://www.quandl.com/api/v3/datasets/CME/YKX2017.json?api_key=zeZW2ba38zkWbmBz_ufL
// https://www.quandl.com/api/v3/datasets/ICE/CTZ2017.json?api_key=zeZW2ba38zkWbmBz_ufL]
// AJAX call of api, substituting django variables which were defined for javascript in corresponding html
var API="https://www.quandl.com/api/v3/datasets/" + exchange + "/"+symbol+".json?api_key=zeZW2ba38zkWbmBz_ufL";
$.ajax(
   {
  url: API,
    method: "GET",
    success: function(data){

      $('#purchasesymbol').val(symbol);
    var results = data.dataset.data[0][6];
      $("#price").html(results);
      $("#purchaseprice").val(results);

    var results1 = data.dataset.data[1][6];
      $("#net-change").html(parseFloat((results-results1).toFixed(3)));
      if (results>results1){
        $('#net-change').removeAttr('class', 'futures');
        $('#net-change').attr('class', 'futures-up');}

      else if (results<results1) {
        $('#net-change').removeAttr('class', 'futures');
        $('#net-change').attr('class', 'futures-down');}


    var results = data.dataset.data[0][1];
      $("#open").html(results);

    var results = data.dataset.data[0][2];
      $("#high").html(results);

    var results = data.dataset.data[0][3];
      $("#low").html(results);

    var results = data.dataset.data[1][6];
      $("#prev-settle").html(results);

    var results = data.dataset.data[0][7];
      $("#volume").html(results);

    $('.symbolchoice').html(symbol);

      var a = data.dataset.data;
        var z= [];
        var c= [];
        var d= [];
        var e= [];
        var k= [];
        for (var i=0; i<a.length; i++){
          z.push(a[i][0]) //date
          // test to eliminate null and zero values
          if (a[i][2]>0 && a[i][3]>0 && a[i][1]>0 && a[i][6]>0){
          c.push(a[i][2]) //High
          d.push(a[i][3]) //low
          e.push(a[i][1]) //open
          k.push(a[i][6])}}; //close
// Get max and min values of high and low. Need to filter out with Boolean to eliminate null values.
    var max=(Math.max.apply(null, c));
    var min=(Math.min.apply(null, d.filter(Boolean)));
// Set downside of range for chart and attempting to eliminate faulty data values
    var index = c.indexOf(max);
     if (min<results1*.8){
        min=results1*.9
      };


  // Set upside of range for chart and attempting to eliminate faulty data values
  // Need to eliminate highest value if it is way higher than second highest
    if (max>results1*1.2){
      c.splice(index,1);
      var max2=(Math.max.apply(null, c));
        if (max>max2*1.03){
          max=max2;
          c.splice(index,0, max)}
        else {
          c.splice(index,0,max);
        }
      };
// checks to see if arrays and min maxes are what I think
    console.log(index);
    console.log(results1);
    console.log(max);
    console.log(min);
    // console.log(z);
    // console.log(c);
    // console.log(d);
    // console.log(e);
    // console.log(k);





// Candlestick chart code
     var trace = {
       x: z,
       close: k,
       high: c,
       low: d,
       open: e,

       // cutomise colors
       increasing: {line: {color: 'black'}},
       decreasing: {line: {color: 'red'}},

       type: 'candlestick',
       xaxis: 'x',
       yaxis: 'y'
     };

     var data = [trace];

     var layout = {
       dragmode: 'zoom',
       showlegend: false,
      //  autosize: false,
      //   width: 1400,
      //   height: 1200,
      //   margin: {
      //   l: 500,
      //   r: 100,
      //   b: 700,
      //   t: 100,
      //   pad: 0
      // },
       xaxis: {
         autorange: true,
         title: 'Date',
     	 rangeselector: {
             x: 0,
             y: 1.2,
             xanchor: 'left',
             font: {size:8},
             buttons: [{
                 step: 'month',
                 stepmode: 'backward',
                 count: 1,
                 label: '1 month'
             }, {
                 step: 'month',
                 stepmode: 'backward',
                 count: 3,
                 label: '3 months'
             },
                {
                 step: 'month',
                 stepmode: 'backward',
                 count: 6,
                 label: '6 months'
             },
                {
                 step: 'all',
                 label: 'All dates'
             }]
           }
       },
       yaxis: {
         autorange: false,
           range: [min*.95, max*1.05],
       }
     };

     Plotly.newPlot('candlestick', data, layout);






  $(".choice").change(onChoiceChange);
  $("#sellbutton").click(onSellClick);
  $("#buybutton").click(onBuyClick);


  $("form").submit(function(e){
    e.preventDefault();
    var quantity = $('#purchasequantity').val();
    var price = $('#purchaseprice').val();
    var sym = $('#purchasesymbol').val();
    var multiplier = $('#total_multiplier').val();
    $.post("/instrument/purchase/", {
      quantity: quantity,
      price: price,
      symbol: sym,
      multiplier:multiplier
    }).then(function(response){
      console.log(response);
    }, function(error_response){
      console.log(error_response)
    })

  })



  function onSellClick(e){
    if ($('.quantity').val()!=0){
      var quantity = $('.quantity').val()*-1;
      var price = $('#purchaseprice').val();
      var sym = $('#purchasesymbol').val();
      var multiplier = $('#total_multiplier').val();
      $('#purchasequantity').val($('.quantity').val()[0] * -1);
      confirm("You want to sell  "+quantity*-1+" contract(s) of "+sym+" at "+ price);
      var cash_outlay=quantity*price*50

  }
    else{
      confirm("You must enter in a quantity");
  }
}



  function onBuyClick(e){
    if ($('.quantity').val()!=0){
      var quantity = $('.quantity').val();
      var price = $('#purchaseprice').val();
      var sym = $('#purchasesymbol').val();
      var multiplier = $('#total_multiplier').val();
      $('#purchasequantity').val($('.quantity').val()[0]);
      confirm("You want to buy  "+quantity+" contract(s) of "+sym+" at "+ price);
  }
    else{
      confirm("You must enter in a quantity");
    }
}







   },
   error: function(error){
    alert(message)
    console.log(error,message);
   }
   });
}


loadData();
