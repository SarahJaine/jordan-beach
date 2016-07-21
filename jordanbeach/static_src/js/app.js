import $ from 'jquery'
import 'foundation'
import 'foundation-mediaquery'


// initialize foundation
$(document).foundation()
// example
const dateDisplayEl = document.createElement('div')
dateDisplayEl.innerHTML = new Date()
document.body.appendChild(dateDisplayEl)


$("#js-video-controls").hover(
  function() {
    $(this).attr('controls', true);
  }, function() {
    $(this).removeAttr('controls');
  }
)

// $("#js-video-controls").click(function() {
//   // if $(this).paused() {
//   //   $(this).play();
//   // } else {
//     $(this).pause();
//     $(this).removeAttr('autoplay');
//   }
// });
