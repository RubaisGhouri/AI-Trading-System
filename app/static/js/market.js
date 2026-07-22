async function loadMarket() {

    const grid = document.getElementById("market-grid");

    if (!grid) return;

    try {

        const response = await fetch("/api/market/");

        const data = await response.json();

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

                    <div class="${positive ? "market-green" : "market-red"}">

                        ${positive ? "▲" : "▼"}

                        ${coin.change.toFixed(2)}%

                    </div>

                    <div class="market-volume">

                        Vol:
                        ${Number(coin.volume).toLocaleString()}

                    </div>

                </div>
            `;

        });

    }

    catch(error){

        console.error(error);

        grid.innerHTML = `
            <div class="loading">
                Unable to load market data.
            </div>
        `;

    }

}

document.addEventListener("DOMContentLoaded",()=>{

    loadMarket();

    setInterval(loadMarket,10000);

});