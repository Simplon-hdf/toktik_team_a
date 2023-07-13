function initForm()
{
	form = document.querySelector("#form_post")
	form.onsubmit = function(event){
		var xhr = new XMLHttpRequest();
		var formData = new FormData(form);
		//open the request
		xhr.open('POST','http://localhost:8000/post/create')
		xhr.setRequestHeader("Content-Type", "application/json");
		//send the form data
		xhr.send(JSON.stringify(Object.fromEntries(formData)));

		xhr.onreadystatechange = function() {
			if (xhr.readyState == XMLHttpRequest.DONE) {
				httpCode = xhr.status
				if (httpCode == 200) {
					postId = JSON.parse(xhr.response).id
					window.location.href = "./index.html?post="+postId
				}
			}
		}
		//Fail the onsubmit to avoid page refresh.
		return false;
	}
}

setTimeout(initForm, 1000);
