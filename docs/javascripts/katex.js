;(() => {
  'use strict'

  // macros personnalisées
  const macros = {
    '\\RR': '\\mathbb{R}',
    '\\vect': '{\\begin{pmatrix}#1\\\\#2\\end{pmatrix}}',
  }

  // rendu katex
  function katexMath() {
    let maths = document.querySelectorAll('.arithmatex'),
      tex

    for (let i = 0; i < maths.length; i++) {
      tex = maths[i].textContent || maths[i].innerText
      if (tex.startsWith('\\(') && tex.endsWith('\\)')) {
        katex.render(tex.slice(2, -2), maths[i], {
          displayMode: false,
          macros,
          throwOnError: false,
        })
      } else if (tex.startsWith('\\[') && tex.endsWith('\\]')) {
        katex.render(tex.slice(2, -2), maths[i], {
          displayMode: true,
          macros,
          throwOnError: false,
        })
      }
    }
  }
  ;(() => {
    function onReady(fn) {
      if (document.addEventListener) {
        document.addEventListener('DOMContentLoaded', fn)
      } else {
        document.attachEvent('onreadystatechange', function () {
          if (document.readyState === 'interactive') {
            fn()
          }
        })
      }
    }

    onReady(() => {
      if (typeof katex !== 'undefined') {
        katexMath()
      }
    })
  })()
})()
