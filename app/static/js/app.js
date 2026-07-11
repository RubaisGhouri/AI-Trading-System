console.log("QuantNova Started...");

async function loadMarket() {
  try {
    const response = await fetch("/api/market");

    const data = await response.json();

    const grid = document.getElementById("market-grid");

    if (!grid) return;

    grid.innerHTML = "";

    data.forEach((coin) => {
      const positive = coin.change >= 0;

      grid.innerHTML += `

                <div class="market-card">

                    <div class="market-symbol">
                        ${coin.symbol}
                    </div>

                    <div class="market-price">
                        $${Number(coin.price).toLocaleString()}
                    </div>

                    <div class="market-change ${positive ? "market-green" : "market-red"}">

                        ${positive ? "▲" : "▼"}

                        ${coin.change.toFixed(2)}%

                    </div>

                    <br>

                    <small>

                        Volume:
                        ${Number(coin.volume).toLocaleString()}

                    </small>

                </div>

            `;
    });
  } catch (error) {
    console.error(error);
  }
}

loadMarket();

/* Refresh every 10 seconds */

setInterval(loadMarket, 10000);

if (document.getElementById("tradingview_chart")) {
  const script = document.createElement("script");

  script.src = "https://s3.tradingview.com/tv.js";

  script.onload = function () {
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
}

/* ================================
   QuantNova AI Chat
================================ */

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

      body: JSON.stringify({
        message: message,
      }),
    });

    const data = await response.json();

    document.querySelector(".loading").remove();

    chat.innerHTML += `
            <div class="ai-message">
                ${data.reply}
            </div>
        `;

    chat.scrollTop = chat.scrollHeight;
  } catch (error) {
    document.querySelector(".loading").remove();

    chat.innerHTML += `
            <div class="ai-message">
                ❌ Failed to connect with QuantNova AI.
            </div>
        `;

    console.error(error);
  }
}

async function loadSignal() {
  try {
    const response = await fetch("/api/signal");

    const signal = await response.json();

    const div = document.getElementById("signal-card");

    if (!div) return;

    const signalColor =
      signal.signal === "BUY"
        ? "#12d6a2"
        : signal.signal === "SELL"
          ? "#ff5b5b"
          : "#ffc857";

    const directionIcon =
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

            <h2 style="color:${signalColor};margin-bottom:20px;">

                ${directionIcon}

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

                <span>Take Profit 1</span>

                <strong>${signal.tp1}</strong>

            </div>

            <div class="scanner-row">

                <span>Take Profit 2</span>

                <strong>${signal.tp2}</strong>

            </div>

            <div class="scanner-row">

                <span>Take Profit 3</span>

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

            <div style="margin-top:20px;">

                <strong>AI Analysis</strong>

                <ul style="margin-top:10px;padding-left:20px;line-height:1.8;">

                    ${reasons}

                </ul>

            </div>

        `;
  } catch (err) {
    console.log(err);
  }
}

loadSignal();

setInterval(loadSignal, 15000);

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

                    </div>

                    <div style="color:${color};font-weight:700;">

                        ${coin.signal}

                    </div>

                    <div>

                        ${coin.confidence}%

                    </div>

                </div>

            `;
    });
  } catch (err) {
    console.log(err);
  }
}

loadScanner();

setInterval(loadScanner, 15000);
loadNews();
