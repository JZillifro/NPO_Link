const assert = require('assert')
import {getManyNonprofits, getNonprofit} from './src/nonprofitcalls' //get functions to get nonprofits on page and a specifc nonprofit from nonprofit call file
import {getManyLocations, getLocation} from './src/locationcalls' //same but Locations
import {getManyCategories, getCategory} from './src/categorycalls' //same but categories

describe('Check Number of Instances Returned for Nonprofits', function() {
  it('should have 12 instances', async function() {
    instances = await getManyNonprofits(/*params*/);
    assert.equal(instances.objects.length, 12);
  });
})

describe('Check Number of Instances Returned for Locations', function() {
  it('should have 12 instances', async function() {
    instances = await getManyLocations(/*params*/); //update params needed
    assert.equal(instances.objects.length, 12); //may need to change depending on what return looks like
  })
})

describe('Check Number of Instances Returned for Categories', function() {
  it('should have 12 instances', async function() {
    instances = await getManyCategories(/*params*/); //update params needed
    assert.equal(instances.objects.length, 12); //may need to change depending on what return looks like
  });
})

describe('Check correct instance returned for Nonprofit', function() {
  it('return the correct nonprofit', async function() {
    instance_returned = await getNonprofit(/*Name*/);//if need name, send name of one of them
    assert.equal(instance_returned[0].name, /*Name*/); //may need to change depending on what return looks like
  });
})

describe('Check correct instance returned for Location', function() {
  it('return the correct location', async function() {
    instance_returned = await getLocation(/*Name*/); //if need name, send name of one of them
    assert.equal(instance_returned[0].name, /*Name*/); //may need to change depending on what return looks like
  });
})

describe('Check correct instance returned for Category', function() {
  it('return the correct category', function() {
    instance_returned = await getCategory(/*Name*/); //if need name, send name of one of them
    assert.equal(instance_returned[0].name, /*Name*/); //may need to change depending on what return looks like
  });
})
