const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
        } else {
            entry.target.classList.remove('show');
        } 
    }); 
});


const hiddenElements = document.querySelectorAll('.hidden');
hiddenElements.forEach((el) => observer.observe(el));

window.sr = ScrollReveal();

    sr.reveal('nav',{
        duration: 1000,
        origin:'bottom',
        distance: '-50px'
    });

window.sr = ScrollReveal();

    sr.reveal('.scrolldown',{
        duration: 2000,
        origin:'top',
        distance: '-500px'
    });



