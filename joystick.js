var radius = 100;

var sampleJoystick = {
    mode: 'static',
    position: {
      left: '75%',
      top: '80%'
    },
    size: radius*2,
    color: 'black'
};

var joystick;
var position;
joystick = nipplejs.create(sampleJoystick);
joystick.on('start end', function(evt, data) {
  position = data;
}).on('move', function(evt, data) {
  position = data;
}).on('dir:up plain:up dir:left plain:left dir:down' +
      'plain:down dir:right plain:right',
      function(evt, data) {
  //position=data;
}
     ).on('pressure', function(evt, data) {
  position=data;
});