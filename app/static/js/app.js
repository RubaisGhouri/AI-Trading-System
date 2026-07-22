console.log("QuantNova Started...");

/* ==========================================================
   TradingView Chart
========================================================== */

document.addEventListener("DOMContentLoaded", () => {
  if (!document.getElementById("tradingview_chart")) return;

  const script = document.createElement("script");
  script.src = "https://s3.tradingview.com/tv.js";

  script.onload = () => {
    new TradingView.widget({
      autosize: true,
      symbol: "BINANCE:BTCUSDT",
      interval: "15",
      timezone: "Etc/UTC",
      theme: "dark",
      style: "1",
      locale: "en",
      toolbar_bg: "#111827",
      enable_publishing: false,
      hide_side_toolbar: false,
      allow_symbol_change: true,
      withdateranges: true,
      studies: [
        "RSI@tv-basicstudies",
        "MACD@tv-basicstudies",
        "MASimple@tv-basicstudies",
      ],
      container_id: "tradingview_chart",
    });
  };

  document.body.appendChild(script);
});

/* ==========================================================
   AI CHAT
========================================================== */

const sendBtn = document.getElementById("send-btn");

if (sendBtn) {
  sendBtn.addEventListener("click", sendMessage);
}

const input = document.getElementById("user-message");

if (input) {
  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });
}

async function sendMessage() {
  const input = document.getElementById("user-message");
  const chat = document.getElementById("chat-window");

  if (!input || !chat) return;

  const message = input.value.trim();

  if (!message) return;

  chat.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

  input.value = "";

  chat.innerHTML += `
        <div class="ai-message loading">
            QuantNova is thinking...
        </div>
    `;

  chat.scrollTop = chat.scrollHeight;

  try {
    const response = await fetch("/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    const data = await response.json();

    document.querySelector(".loading")?.remove();

    chat.innerHTML += `
            <div class="ai-message">
                ${data.reply}
            </div>
        `;
  } catch (error) {
    document.querySelector(".loading")?.remove();

    chat.innerHTML += `
            <div class="ai-message">
                ❌ QuantNova AI is currently unavailable.
            </div>
        `;

    console.error(error);
  }

  chat.scrollTop = chat.scrollHeight;
}

/* ==========================================================
   SIGNAL ENGINE
========================================================== */

async function loadSignal() {
  try {
    const response = await fetch("/api/signal");
    const signal = await response.json();

    const div = document.getElementById("signal-card");

    if (!div) return;

    const color =
      signal.signal === "BUY"
        ? "#12d6a2"
        : signal.signal === "SELL"
        ? "#ff5b5b"
        : "#ffc857";

    const direction =
      signal.direction === "LONG"
        ? "🟢 LONG"
        : signal.direction === "SHORT"
        ? "🔴 SHORT"
        : "🟡 WAIT";

    let reasons = "";

    signal.reason.forEach((reason) => {
      reasons += `<li>${reason}</li>`;
    });

    div.innerHTML = `
        <h2 style="color:${color};margin-bottom:20px;">
            ${direction}
        </h2>

        <div class="scanner-row">
            <span>Coin</span>
            <strong>${signal.coin}</strong>
        </div>

        <div class="scanner-row">
            <span>Confidence</span>
            <strong>${signal.confidence}%</strong>
        </div>

        <div class="scanner-row">
            <span>Entry Zone</span>
            <strong>${signal.entry}</strong>
        </div>

        <div class="scanner-row">
            <span>TP1</span>
            <strong>${signal.tp1}</strong>
        </div>

        <div class="scanner-row">
            <span>TP2</span>
            <strong>${signal.tp2}</strong>
        </div>

        <div class="scanner-row">
            <span>TP3</span>
            <strong>${signal.tp3}</strong>
        </div>

        <div class="scanner-row">
            <span>Stop Loss</span>
            <strong>${signal.stop_loss}</strong>
        </div>

        <div class="scanner-row">
            <span>Risk / Reward</span>
            <strong>${signal.risk_reward}</strong>
        </div>

        <div class="scanner-row">
            <span>Timeframe</span>
            <strong>${signal.timeframe}</strong>
        </div>

        <div class="scanner-row">
            <span>Leverage</span>
            <strong>${signal.leverage}</strong>
        </div>

        <div style="margin-top:18px;">
            <strong>AI Analysis</strong>

            <ul style="margin-top:10px;padding-left:18px;line-height:1.8;">
                ${reasons}
            </ul>
        </div>
    `;
  } catch (err) {
    console.error(err);
  }
}

/* ==========================================================
   OPPORTUNITY SCANNER
========================================================== */

async function loadScanner() {
  try {
    const response = await fetch("/api/opportunities");
    const data = await response.json();

    const container = document.getElementById("scanner-list");

    if (!container) return;

    container.innerHTML = "";

    data.forEach((coin) => {
      let color = "#ffc857";

      if (coin.signal === "BUY") color = "#12d6a2";
      if (coin.signal === "SELL") color = "#ff5b5b";

      container.innerHTML += `
            <div class="scanner-row">

                <div>

                    <strong>${coin.coin}</strong>

                    <br>

                    <small>${coin.direction}</small>

                </div>

                <div style="text-align:right">

                    <div style="color:${color};font-weight:700;">
                        ${coin.signal}
                    </div>

                    <small>${coin.confidence}%</small>

                </div>

            </div>
        `;
    });
  } catch (err) {
    console.error(err);
  }
}

/* ==========================================================
   INITIAL LOAD
========================================================== */

document.addEventListener("DOMContentLoaded", () => {
  loadSignal();
  loadScanner();

  setInterval(loadSignal, 15000);
  setInterval(loadScanner, 15000);
});