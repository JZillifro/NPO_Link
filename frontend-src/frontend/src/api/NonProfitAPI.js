import {BASE_API_URL} from './../components/constants.jsx'
import axios from 'axios'
import { __esModule } from 'google-map-react/lib/google_map';
// A simple data API that will be used to get the data for our
// components. On a real website, a more robust data fetching
// solution would be more appropriate.
let nonprofit = {};
export async function getNonProfit(id) {
  const response = axios.get(`${BASE_API_URL}/v1.0/nonprofits/nonprofit/${id}`)
  return response
}
nonprofit.getNonProfit = async function getNonProfit(id) {
  const response = axios.get(`${BASE_API_URL}/v1.0/nonprofits/nonprofit/${id}`)
  return response
}
export async function getManyNonProfits(page){
  const response = axios.get(`${BASE_API_URL}/v1.0/nonprofits/${page}`)
  return response
}
nonprofit.getManyNonProfits = async function getManyNonProfits(page){
  const response = axios.get(`${BASE_API_URL}/v1.0/nonprofits/${page}`)
  return response
}
