import {BASE_API_URL} from './../components/constants.jsx'
import axios from 'axios'
import { __esModule } from 'google-map-react/lib/marker_dispatcher';
// A simple data API that will be used to get the data for our
// components. On a real website, a more robust data fetching
// solution would be more appropriate.
let category = {}
export async function getCategory(id) {
  const response = axios.get(`${BASE_API_URL}/v1.0/categories/category/${id}`)
  return response
}
category.getCategory = async function getCategory(id) {
  const response = axios.get(`${BASE_API_URL}/v1.0/categories/category/${id}`)
  return response
}

export async function getManyCategory(id) {
  const response = axios.get(`${BASE_API_URL}/v1.0/categories/${id}`)
  return response
}
category.getManyCategory = async function getManyCategory(id) {
  const response = axios.get(`${BASE_API_URL}/v1.0/categories/${id}`)
  return response
}

module.expose = category