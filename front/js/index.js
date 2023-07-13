function bodyLoad() {
    initHeaderSearchForm()
    const postId = urlParams.get('post')
    postId === "" ? randomVideo() : fetchAndUpdate(postId)
}

function initHeaderSearchForm()
{
	form = document.querySelector("#header_search")
	form.onsubmit = function(event){
		var xhr = new XMLHttpRequest();

		searchId = document.getElementById('search_id').value
		window.location.href = "./index.html?post=" + searchId

		return false;
	}
}



var videoContainer = document.querySelector('.video-container');
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const color = urlParams.get('post')

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

async function fetchAndUpdate(id=null)
{
    const rest_url = id == null ? "http://localhost:8000/post/random" : "http://localhost:8000/post/" + id
    const response = await fetch(rest_url)

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

function changeVideo(delta) {
    fetchAndUpdate(currentPostId + delta)
}

function randomVideo() {
    fetchAndUpdate(null)
}





// var video = videoContainer.querySelector('video');

// // Lecture automatique des vidéos suivantes
// video.addEventListener('ended', playNextVideo);

// function playNextVideo() {
//     // Remplacez "video1.mp4" par le chemin de votre prochaine vidéo
//     video.src = "video2.mp4";
//     video.load();
//     video.play();
// }
