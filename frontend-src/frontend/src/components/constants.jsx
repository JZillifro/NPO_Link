const BASE_API_URL = (process.env.NODE_ENV === 'production')
    ? 'http://api.npolink.me'
    : (process.env.NODE_ENV === 'test')
    ? 'http://backend:5000'
    : 'http://localhost:5000';

// const STATES = ["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"];

const STATES = ["AR", "AZ", "CA", "CO", "CT", "FL", "GA", "HI", "IA", "IL", "IN", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MT", "NC", "NH", "NJ", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "TN", "TX", "UT", "VA", "VT", "WA"];

const CAT_CODES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

export {
 BASE_API_URL,
 STATES,
 CAT_CODES
}
