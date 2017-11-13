// var table = $("#mprDetailDataTable table tbody");


var symbols = $.map($(".transaction-symbols"), function(e){ return $(e).text()});

var amounts = $.map($(".transaction-symbols-amounts"), function(e){ return parseFloat($(e).text())});





// var value=[53000, 23000, 7000, 6000, 4000, 7000];

var data = [{
  values: amounts,
  labels: symbols,
  type: 'pie'
}];

var layout = {
  title: 'Portfolio Breakdown',
  font: {
    family: 'garamond monospace',
    size: 24,
    color: '#485d7f'},

  height: 700,
  width: 900

};

Plotly.newPlot('pie-chart', data, layout);
