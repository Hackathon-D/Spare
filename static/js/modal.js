//modalの外をクリックしたら閉じる処理
window.onclick = function(event) {
  if(event.target == modal_reaction) {
      modal_reaction.style.display = 'none';
  }
  if(event.target == modal_draft) {
    modal_draft.style.display = 'none';
  }
  if(event.target == modal_templete) {
  modal_templete.style.display = 'none';
  }
};

// モーダルを表示させる

const addChannelModal = document.getElementById("add-channel-modal");
const deleteChannelModal = document.getElementById("delete-channel-modal");

const addPageButtonClose = document.getElementById("add-page-close-btn");
const deletePageButtonClose = document.getElementById("delete-page-close-btn");

const addChannelBtn = document.getElementById("add-channel-btn");

const addChannelConfirmBtn = document.getElementById(
  "add-channel-confirmation-btn"
);
const deleteChannelConfirmBtn = document.getElementById(
  "delete-channel-confirmation-btn"
);

// モーダルを開く
// <button id="add-channel-btn">チャンネル追加</button>ボタンがクリックされた時
addChannelBtn.addEventListener("click", () => {
  modalOpen("add");
});

function modalOpen(mode) {
  if (mode === "add") {
    addChannelModal.style.display = "block";
  } else if (mode === "delete") {
    deleteChannelModal.style.display = "block";
  } else if (mode === "update") {
    updateChannelModal.style.display = "block";
  }
}

// モーダル内のバツ印がクリックされた時
addPageButtonClose.addEventListener("click", () => {
  modalClose("add");
});
deletePageButtonClose.addEventListener("click", () => {
  modalClose("delete");
});

function modalClose(mode) {
  if (mode === "add") {
    addChannelModal.style.display = "none";
  } else if (mode === "delete") {
    deleteChannelModal.style.display = "none";
  } else if (mode === "update") {
    updateChannelModal.style.display = "none";
  }
}

const reaction_modal = document.getElementsByClassName('reaction-add');

//clickするとmodalを開く処理
reaction_modal.onclick = function() {
  reaction_modal.style.display = 'block';
};