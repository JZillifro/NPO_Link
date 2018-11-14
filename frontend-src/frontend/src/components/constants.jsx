const BASE_API_URL = (process.env.NODE_ENV === 'production')
    ? 'http://api.npolink.me'
    : (process.env.NODE_ENV === 'test')
    ? 'http://backend:5000'
    : 'http://localhost:5000';
export {
 BASE_API_URL
}
