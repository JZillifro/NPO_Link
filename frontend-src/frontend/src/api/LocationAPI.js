import {BASE_API_URL} from './../components/constants.jsx'
import axios from 'axios'
// A simple data API that will be used to get the data for our
// components. On a real website, a more robust data fetching
// solution would be more appropriate.
export async function getLocation(id) {
  const response = axios.get(`${BASE_API_URL}/v1.0/locations/location/${id}`)
  return response
}
export async function getManyLocations(id) {
  const response = axios.get(`${BASE_API_URL}/v1.0/locations/${id}`)
  return response
}
