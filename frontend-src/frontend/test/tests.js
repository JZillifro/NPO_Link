const assert = require('assert');
import {getManyNonProfits, getNonProfit} from './../src/api/NonProfitAPI' //get functions to get nonprofits on page and a specifc nonprofit from nonprofit call file
import {getManyLocations, getLocation} from './../src/api/LocationAPI' //same but Locations
import {getManyCategories, getCategory} from './../src/api/CategoryAPI' //same but categories

describe('Check Number of Instances Returned for Nonprofits', function() {
  it('should have 12 instances', async function() {
    const response = await getManyNonProfits(1);
    assert.equal(response.data.data.nonprofits.length, 12);
  });
})

describe('Check Number of Instances Returned for Locations', function() {
  it('should have 12 response', async function() {
    const response = await getManyLocations(1); //update params needed
    assert.equal(response.data.data.locations.length, 12); //may need to change depending on what return looks like
  })
})

describe('Check Number of Instances Returned for Categories', function() {
  it('should have 12 response', async function() {
    const response = await getManyCategories(1); //update params needed
    assert.equal(response.data.data.categories.length, 12); //may need to change depending on what return looks like
  });
})

describe('Check correct instance returned for Nonprofit', function() {
  it('return the correct nonprofit', async function() {
    const response = await getNonProfit(1);//if need name, send name of one of them
    assert.equal(response.data.data.nonprofit.id, 1); //may need to change depending on what return looks like
  });
})

describe('Check correct instance returned for Location', function() {
  it('return the correct location', async function() {
    const response = await getLocation(1); //if need name, send name of one of them
    assert.equal(response.data.data.location.id, 1); //may need to change depending on what return looks like
  });
})

describe('Check correct instance returned for Category', function() {
  it('return the correct category', async function() {
    const response = await getCategory(1); //if need name, send name of one of them
    assert.equal(response.data.data.category.id, 1); //may need to change depending on what return looks like
  });
});
