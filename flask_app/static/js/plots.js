function build_cases_chart(){
    d3.json("/api/case_data").then(function(result) {
    

    // 

    var x = Object.keys(result)
    var y = Object.values(result)
    // console.log(x)
    // console.log(y)

    var data = [
        {
          x: x,
          y: y,
          type: 'bar'
        }
      ];
    var layout = {
    title: 'Cases by Week',
    xaxis: {title: 'Date'},
    yaxis: {title: 'Cases'},
    }  
      Plotly.newPlot('caseplot', data, layout);
})
}

function build_deaths_chart(){
    d3.json("/api/death_data").then(function(result) {

    var x = Object.keys(result)
    var y = Object.values(result)
    console.log(x)
    console.log(y)

    var data = [
        {
          x: x,
          y: y,
          type: 'bar'
        }
      ];
    var layout = {
    title: 'Deaths by Week',
    xaxis: {title: 'Date'},
    yaxis: {title: 'Deaths'}
    }
      Plotly.newPlot('deathplot', data, layout);
})
}
build_cases_chart()
build_deaths_chart()

// handleClick is functional - it can capture the value entered into the fips_code filter
// now we need to be able to get the fips_code value into the cases function in the flask app.
function handleClick() {

    let fips = d3.select("#fips_filter").property("value");
    console.log(fips)
    d3.json("http://localhost:5000/api/case_data").then(function(result) {
        console.log(result)
    
        // if (fips.include(result)) {
        //     filterFips = fips.filter(fips.include(result))
        // }
        //result.filter()
    
        var x = Object.keys(fips)
        var y = Object.values(fips)
        console.log(x)
        console.log(y)
    });     
}

function filter() {
    let fips = d3.select("#fips_code").property("value");

}















//var fips_filters = {};
//console.log(fips_filters)

// function fips_filter() {
//     console.log('this function is working...kinda')
//     let changedElement = d3.select(this);
//     console.log('the changed element is...' + changedElement)
//     let elementValue = changedElement.property("value");
//     console.log('the element value is...' + elementValue);

//     let filterId = changedElement.attr("id");
//     console.log(filterId);

//     if (elementValue) {
//         fips_filters[filterId] = elementValue
//     }
//     else {
//         delete fips_filters
//         console.log("yes")
//     }
// }


// let fips = d3.select("#fips_code").property("value");
// console.log(fips)




// Event listener
d3.selectAll("#filter-btn").on("click", handleClick);
//d3.selectAll("input").on("change", fips_filter())