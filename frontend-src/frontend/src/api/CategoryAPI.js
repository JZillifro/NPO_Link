// A simple data API that will be used to get the data for our
// components. On a real website, a more robust data fetching
// solution would be more appropriate.
const CategoryAPI = {
  categories: [{id: 1, nonprofit: 1, location: 1, name: "Film/Video", description: "These organization support independant film makers.", image: "https://3.imimg.com/data3/TS/GF/MY-3304941/ad-flim-making-services-250x250.jpg"},
               {id: 2, nonprofit: 2, location: 2, name: "Disease", description: "These organizations support medical research.", image: "https://www.irishcentral.com/uploads/article/13911/cropped_Hemochromatosis_celtic_blood_disease_iStock.jpg?t=1516784551"},
               {id: 3, nonprofit: 3, location: 3, name: "Disaster Preparedness", description: "These organization help prepare cities and their community for natural disasters.", image: "https://www.dominicavibes.dm/wp-content/uploads/2018/03/14297991.54854f3816f2f.jpg"}
            ],
  all: function() { return this.categories},
  get: function(id) {
    const isCategory = p => p.id === id
    return this.categories.find(isCategory)
  }
}

export default CategoryAPI
