const upvoteButton = document.getElementById('upvote');
const upvoteCountSpan = document.getElementById('upvote-count');
const csrf_Token =document.querySelector("input[name=csrfmiddlewaretoken]").value;

upvoteButton.addEventListener('click', () => {
        const noteId = upvoteButton.getAttribute('data-id');
        const url = '/notes/upvote/'+noteId;
        fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken':csrf_Token, 
          },
        })
        .then(response => response.json())
        .then(data => {
          const updatedUpvotes = data.total_upvotes;
          const text = data.text;
          upvoteCountSpan.innerText = updatedUpvotes;
          if(text){
              upvoteButton.innerHTML = '<i class="bi bi-caret-up-square"></i> Upvote';
          }
          else{
            upvoteButton.innerHTML = '<i class="bi bi-caret-up-square-fill"></i> Upvoted';
          };
        })
        .catch(error => {
          console.error('Error:', error);
        });
});
