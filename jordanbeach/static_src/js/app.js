import $ from 'jquery'
import 'foundation'
import 'foundation-mediaquery'


// initialize foundation
$(document).foundation()
// example
const dateDisplayEl = document.createElement('div')
dateDisplayEl.innerHTML = new Date()
document.body.appendChild(dateDisplayEl)


$('#js-video-controls').hover(
  $(this).attr('controls', true),
  $(this).removeAttr('controls')
)

// $('#js-video-controls').click(
//   function() {
//   if $(this).attr('autoplay') {
//     $(this).removeAttr('autoplay');
//   }
//   }
// });
