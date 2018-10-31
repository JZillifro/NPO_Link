const assert = require('assert')
import {getManyNonProfits, getNonProfit} from './src/api/NonProfitAPI' //get functions to get nonprofits on page and a specifc nonprofit from nonprofit call file
import {getManyLocations, getLocation} from './src/api/LocationAPI' //same but Locations
import {getManyCategories, getCategory} from './src/api/CategoryAPI' //same but categories

describe('Check Number of Instances Returned for Nonprofits', function() {
  it('should have 12 instances', async function() {
    response = await getManyNonProfits(/*params*/);
    assert.equal(response.data.nonprofits.length, 12);
  });
})

describe('Check Number of Instances Returned for Locations', function() {
  it('should have 12 response', async function() {
    response = await getManyLocations(/*params*/); //update params needed
    assert.equal(response.objects.length, 12); //may need to change depending on what return looks like
  })
})

describe('Check Number of Instances Returned for Categories', function() {
  it('should have 12 response', async function() {
    response = await getManyCategories(/*params*/); //update params needed
    assert.equal(response.objects.length, 12); //may need to change depending on what return looks like
  });
})

describe('Check correct instance returned for Nonprofit', function() {
  it('return the correct nonprofit', async function() {
    response = await getNonProfit(/*Name*/);//if need name, send name of one of them
    assert.equal(response[0].name, /*Name*/); //may need to change depending on what return looks like
  });
})

describe('Check correct instance returned for Location', function() {
  it('return the correct location', async function() {
    response = await getLocation(/*Name*/); //if need name, send name of one of them
    assert.equal(response[0].name, /*Name*/); //may need to change depending on what return looks like
  });
})

describe('Check correct instance returned for Category', function() {
  it('return the correct category', function() {
    response = await getCategory(/*Name*/); //if need name, send name of one of them
    assert.equal(response[0].name, /*Name*/); //may need to change depending on what return looks like
  });
})
