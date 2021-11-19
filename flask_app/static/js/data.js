// let usCounties = 'https://raw.githubusercontent.com/kowiak89/mapping-earthquakes/Earthquakes_past7days/usCounties.json';

let fips = usCounties.map(function(x) {
    return x.geometry
})
console.log(fips)