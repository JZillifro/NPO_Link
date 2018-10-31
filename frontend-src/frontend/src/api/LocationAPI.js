// A simple data API that will be used to get the data for our
// components. On a real website, a more robust data fetching
// solution would be more appropriate.
const LocationAPI = {
  locations: [
    {id: 1, nonprofit: 1, category: 1, name: "Austin, Tx", description: "Austin is the state capital of Texas, an inland city bordering the Hill Country region.", image: "https://s.yimg.com/ny/api/res/1.2/F5QNZk6yFsCo.xljxX7Nwg--~A/YXBwaWQ9aGlnaGxhbmRlcjtzbT0xO3c9ODAw/http://media.zenfs.com/en-US/homerun/businessinsider.com/686264f597202e8902e8ccbe53d74fc4" },
    {id: 2, nonprofit: 2, category: 2, name: "Houston, Texas", description: "Houston is a large metropolis in Texas, extending to Galveston Bay.", image: "https://assets3.thrillist.com/v1/image/1808718/size/tmg-article_default_mobile.jpg"},
    {id: 3, nonprofit: 3, category: 3, name: "San Antonio, Texas", description: "San Antonio is a major city in south-central Texas with a rich colonial heritage.", image: "https://www.tripsavvy.com/thmb/bN3MDpQtAZpnsP--SSVgqtVhNjg=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/downtown-san-antonio-180514061-598b9a4c396e5a00101781c1.jpg"}

  ],
  all: function() { return this.locations},
  get: function(id) {
    const isLocation = p => p.id === id
    return this.locations.find(isLocation)
  }
}

export default LocationAPI
