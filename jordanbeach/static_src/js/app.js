import $ from 'jquery'
import 'foundation'
import 'foundation-mediaquery'

const pathname = window.location.pathname
const url      = window.location.href
const homeLink = $('#js-home')
const cvLink = $('#js-cv')
const video = $("#js-video-controls")
console.log(video)
console.log(homeLink)

// homeLink.animate({
//       borderBottom: '2px solid black'
//       // width : '46%'
//     }, 500);
// // initialize foundation
// $(document).foundation()
// // example
// const dateDisplayEl = document.createElement('div')
// dateDisplayEl.innerHTML = new Date()
// document.body.appendChild(dateDisplayEl)


// $('#js-video-controls').hover(
//   $(this).attr('controls', true),
//   $(this).removeAttr('controls')
// )


if (pathname === '/')
  homeLink.addClass('js-page-loaded')
if (pathname === '/cv/')
  cvLink.addClass('js-page-loaded')

video.playbackRate = .5;
console.log(pathname)
console.log(video.duration)
