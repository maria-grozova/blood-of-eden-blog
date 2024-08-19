const editButtons = document.getElementsByClassName("edit-button");
const commentText = document.getElementById("id_body");
const commentScore = document.getElementById("id_rating");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = document.getElementById("deleteModal");
const deleteButtons = document.getElementsByClassName("delete-button");
const deleteConfirm = document.getElementById("deleteConfirm");
const modalCheckbox = document.querySelector("input[name=modal-close]");

const messageCheckbox = document.querySelector("input[name=message-close]");
const messageBlock = document.getElementById("msg");


/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment and rating.
* - Populates the `commentText` and `commentScore` input/textarea with the comment's content and score for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let commentId = e.target.getAttribute("comment_id");
    let commentRating = document.getElementById(`rating${commentId}`).innerHTML;
    console.log(commentRating);
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    commentText.value = commentContent;
    commentScore.value = commentRating;
    submitButton.innerText = "Update";
    commentForm.setAttribute("action", `edit_comment/${commentId}`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      deleteConfirm.href = `delete_comment/${commentId}`;
      deleteModal.classList.toggle("hide");
    });
  }

modalCheckbox.addEventListener('change', function() {
  if (this.checked) {
    deleteModal.classList.add("hide");
   }
});

/**
 * Listens for messages to activate close button
 */
messageCheckbox.addEventListener('change', function() {
  if (this.checked) {
    messageBlock.classList.add("hide");
 }
});

  