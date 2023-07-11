var videoContainer = document.querySelector('.video-container');
var video = videoContainer.querySelector('video');

// Lecture automatique des vidéos suivantes
video.addEventListener('ended', playNextVideo);

function playNextVideo() {
    // Remplacez "video1.mp4" par le chemin de votre prochaine vidéo
    video.src = "video2.mp4";
    video.load();
    video.play();
}