function getReview() {
    console.log("getReview function called");  // Add this line
    var content = document.getElementById('content').value;
    fetch('/get_review', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({content: content})
    }).then(response => response.json())
    .then(data => {
        console.log(data);
        // Update the 'feedback' div with AI review
        document.getElementById('feedback').innerText = data['feedback'];
        
        if (data['approval']) {
            document.getElementById('approval').innerText = 'Merge Request Approved';
            document.getElementById('approval').style.color = 'green';
            document.getElementById('commit-btn').disabled = false;
        } else {
            document.getElementById('approval').innerText = 'Merge Request Denied';
            document.getElementById('approval').style.color = 'red';
            document.getElementById('commit-btn').disabled = true;
        }

        appendToHistory(content, data['feedback'], data['approval'], document.getElementById('history').children.length + 1);
    });
}

function updateMergeRequest() {
    var content = document.getElementById('content').value;
    fetch('/update_merge_request', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({content: content})
    }).then(response => response.json())
    .then(data => {
        // Update the 'merged-content' div with updated content
        document.getElementById('merged-content').innerText = data['merged_content'];
    });
}

function commitToDocument() {
    var content = document.getElementById('content').value;
    fetch('/commit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({content: content})
    }).then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            window.location.href = "/";  // Redirect to the index page
        } else {
            console.error(data.message);
        }
    });
}

document.getElementById('get-review-btn').addEventListener('click', getReview);
document.getElementById('update-merge-request-btn').addEventListener('click', updateMergeRequest);
document.getElementById('commit-btn').addEventListener('click', commitToDocument);

function appendToHistory(content, feedback, approval, iteration) {
    var historyDiv = document.getElementById('history');
    var newReviewDiv = document.createElement('div');
    newReviewDiv.innerHTML = `
<div class="rounded shadow-lg mb-6 p-6 bg-gray-100">
    <h3>Iteration ${iteration}:</h3>
    <p class="mt-2"><strong>Content:</strong></p>
    <p>${content}</p>
    <p class="mt-2"><strong>AI Feedback:</strong></p>
    <p>${feedback}</p>
    <p class="mt-2 text-2xl" style="color: ${approval ? 'green' : 'red'};">${approval ? 'Approved' : 'Not Approved'}</p>
</div>`;
    while (newReviewDiv.firstChild) {
        historyDiv.appendChild(newReviewDiv.firstChild);
    }
}
