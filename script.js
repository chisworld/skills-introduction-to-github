async function sendMsg() {
  const input = document.getElementById("input");
  const chatBox = document.getElementById("chat-box");
  const msg = input.value.trim();
  if (!msg) return;

  // 显示用户消息
  const userMsg = document.createElement("div");
  userMsg.className = "msg user";
  userMsg.textContent = "你: " + msg;
  chatBox.appendChild(userMsg);
  chatBox.scrollTop = chatBox.scrollHeight;
  input.value = "";

  // 调用后端 API
  const res = await fetch("/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ message: msg })
  });
  const data = await res.json();

  // 显示 AI 回复
  const aiMsg = document.createElement("div");
  aiMsg.className = "msg ai";
  aiMsg.textContent = "AI: " + data.reply;
  chatBox.appendChild(aiMsg);
  chatBox.scrollTop = chatBox.scrollHeight;
}
