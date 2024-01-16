function startSlideshow() {
    let currentSlide = 1;
    const videos = document.querySelectorAll('.slide-video');

    function showSlide(n) {
        if (n < 1) {
            currentSlide = videos.length;
        } else if (n > videos.length) {
            currentSlide = 1;
        }
        videos.forEach(video => video.classList.add('hidden'));
        videos[currentSlide - 1].classList.remove('hidden');
    }

    function prevVideo() {
        showSlide(currentSlide -= 1);
    }

    function nextVideo() {
        showSlide(currentSlide += 1);
    }

    // Show the first slide on page load
    showSlide(currentSlide);

    return { prevVideo, nextVideo };
}

document.addEventListener('DOMContentLoaded', () => {
    const { prevVideo, nextVideo } = startSlideshow();

    // Attach event listeners to buttons after the DOM is fully loaded
    document.querySelector('.prev-btn').addEventListener('click', prevVideo);
    document.querySelector('.next-btn').addEventListener('click', nextVideo);
});
