
const API_URL = 'http://localhost:5000';
function make_request(route, success, error, data={}, method='GET') {

  console.log(API_URL + route);
  console.log("data is ",data);
  fetch(API_URL + route, {method: method})
  .then(res => res.json())
  .then(success, error);  
}
export default make_request;