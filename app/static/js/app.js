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

    }

    catch(error){

        console.error(error);

    }

}

loadMarket();

/* Refresh every 10 seconds */

setInterval(loadMarket,10000);

if(document.getElementById("tradingview_chart")){

    const script=document.createElement("script");

    script.src="https://s3.tradingview.com/tv.js";

    script.onload=function(){

        new TradingView.widget({

            autosize:true,

            symbol:"BINANCE:BTCUSDT",

            interval:"15",

            timezone:"Etc/UTC",

            theme:"dark",

            style:"1",

            locale:"en",

            toolbar_bg:"#111827",

            enable_publishing:false,

            hide_side_toolbar:false,

            allow_symbol_change:true,

            container_id:"tradingview_chart"

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
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        document.querySelector(".loading").remove();

        chat.innerHTML += `
            <div class="ai-message">
                ${data.reply}
            </div>
        `;

        chat.scrollTop = chat.scrollHeight;

    }

    catch (error) {

        document.querySelector(".loading").remove();

        chat.innerHTML += `
            <div class="ai-message">
                ❌ Failed to connect with QuantNova AI.
            </div>
        `;

        console.error(error);

    }

}