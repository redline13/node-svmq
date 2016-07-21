var MessageQueue = require('../');
require('chai').should();

describe('MessageQueue', function() {

  describe('.open()', function() {
    it('should open/create a queue and return a positive integer (queue ID)', function() {
      MessageQueue
        .open(id, 950)
        .should.be.above(0);
    })
  });

});
