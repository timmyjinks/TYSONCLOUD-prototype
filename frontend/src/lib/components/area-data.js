const csvNortheast = 
  `Day,Usage (%)
  1,29.662053
  2,34.427091
  3,35.976777
  4,39.477986
  5,44.677819
  6,49.040703
  7,98.135283`;



function csvConvert(csv) {
  return csv.split('\n').slice(1).map(str => {
    const [date, usage] = str.split(',')
    .map((el) => (el > 1 ? el : parseFloat(el)));
    return { date, usage};
  });
}
const northeast = csvConvert(csvNortheast);

export default [
  {
    id: 'CPU',
    data: northeast
  },
]
