console.log("Market Module Loaded");

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

    catch (error) {

        console.error(error);

    }

}

loadMarket();

setInterval(loadMarket,10000);