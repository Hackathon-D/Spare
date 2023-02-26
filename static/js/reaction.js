//modalの表示
const modal_reaction = document.getElementById('demo-modal-reaction');
const btn_reaction = document.getElementById('reaction-add');
const close_reaction = document.getElementsByClassName('close-reaction')[0];

// Get all the reaction-add buttons
const reactionAddBtns = document.querySelectorAll('.reaction-add');

// Add click event listener to all the reaction-add buttons
reactionAddBtns.forEach((btn) => {
  btn.addEventListener('click', () => {
    // Open the modal when the reaction-add button is clicked
    const modalReaction = document.getElementById('demo-modal-reaction');
    modalReaction.style.display = 'block';
  });
});

//Xで閉じる処理
close_reaction.onclick = function() {
    modal_reaction.style.display = 'none';
};

//modalの外をクリックしたら閉じる処理
window.onclick = function(event) {
    if(event.target == modal_reaction) {
        modal_reaction.style.display = 'none';
    }
};