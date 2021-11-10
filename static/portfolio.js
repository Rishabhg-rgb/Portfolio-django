a = document.querySelector('#menu')
b = document.querySelector('.header')
a.addEventListener('click', () => {
    if (b.style.display == 'none') {
        b.style.display = 'flex'
        a.innerHTML = 'X'
        a.style.fontSize = '2.5rem'
    }
    else {
        b.style.display = 'none'
        a.innerHTML = `<div class="burger"></div>
        <div class="burger"></div>
        <div class="burger"></div>`
    }
})
