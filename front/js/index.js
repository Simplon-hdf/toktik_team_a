var videoContainer = document.querySelector('.video-container');
// var video = videoContainer.querySelector('video');

// // Lecture automatique des vidéos suivantes
// video.addEventListener('ended', playNextVideo);

// function playNextVideo() {
//     // Remplacez "video1.mp4" par le chemin de votre prochaine vidéo
//     video.src = "video2.mp4";
//     video.load();
//     video.play();
// }

currentPostId = 0

function displayComments(json)
{
    commentSection = document.querySelector("#video-comments > ul")
    commentSection.innerText = ""

    json.forEach(element => {
        var comment = document.createElement('li');
        comment.innerText = element.author_id + " : " + element.content;
        // newChildren.push(comment);
        commentSection.appendChild(comment);
    });
}

async function fetchAndUpdate(id)
{
    const response = await fetch("http://localhost:8000/post/" + id);

    if (response.ok) {
        const post = await response.json();
        console.log(post);
        document.getElementById("video-author").innerHTML = post.author_id;
        document.getElementById("video-title").innerHTML = post.title;
        document.getElementById("video-description").innerHTML = post.description === null ? "<i>Pas de description</i>" : post.description

        videoUrl = post.video_url.match(/watch\?v\=(.*)/)[1]
        embedUrl = "https://www.youtube.com/embed/" + videoUrl
        document.querySelector("#video-container > iframe").src = embedUrl

        displayComments(post.comments)

        currentPostId = post.id
    }
}

function changeVideo(delta)
{
    fetchAndUpdate(currentPostId + delta)
}