#!/usr/bin/node
document.querySelector("#add_item").onclick = () => {
      const ul = document.querySelector(".my_list");
      const li = document.createElement("li");
      li.textContent = "Item";
      ul.appendChild(li);
}
