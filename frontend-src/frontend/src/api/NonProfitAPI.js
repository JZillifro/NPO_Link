// A simple data API that will be used to get the data for our
// components. On a real website, a more robust data fetching
// solution would be more appropriate.
const NonProfitAPI = {
  nonprofits: [
    { id: 1, location: 1, category: 1,  name: "Austin Film Festival",
      description: "Austin Film Festival furthers the art and craft of storytelling by inspiring and championing the work of writers, filmmakers, and all artists who use written and visual language to tell a story.",
      image: "https://www.austinchronicle.com/binary/784a/austinfilmfestival-logo.jpg",
      vol_event: {name: "Austin Film Festival 2018", url: "https://www.allforgood.org/projects/1JlmWYkz"}  },
    {id: 2, location: 2, category: 2,  name: "CanCare" , description: "CanCare is a mighty community of survivors who lift up and inspire cancer patients and caregivers through one-on-one support, empathy, and hope." ,
      image: "https://s.hdnux.com/photos/52/37/17/11137986/7/920x920.jpg",
      vol_event: {name: "CanCare Run for a Reason Program", url: "https://www.allforgood.org/projects/wkxPPMkR"} },
    {id: 3, location: 3, category: 3,   name: "Soldier's Angels", description: "Soldiers' Angels provides aid and comfort to the men and women of the United States Army, Marines, Navy, Air Force, Coast Guard, their families, and a growing veteran population.",
      image: "https://www.mrcy.com/contentassets/59c8f195f9c8409282b353a5fce7deb3/soldiers-and-angels-lrg.jpg",
      vol_event: {name: "Virtual Opportunity - Soldiers' Angels Women of Valor", url: "https://www.allforgood.org/projects/LQrwYd8r"}}
  ],
  all: function() { return this.nonprofits},
  get: function(id) {
    const isNonProfit = p => p.id === id
    return this.nonprofits.find(isNonProfit)
  }
}

export default NonProfitAPI
