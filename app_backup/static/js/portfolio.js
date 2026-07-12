console.log("Portfolio Module Loaded");

async function loadPortfolio() {

    try {

        const response = await fetch("/api/portfolio");

        const data = await response.json();

        const widget = document.getElementById("portfolio-widget");

        if (!widget) return;

        if (!data.connected) {

            widget.innerHTML = `

                <div class="scanner-row">
                    <span>Broker</span>
                    <strong>${data.broker}</strong>
                </div>

                <div class="scanner-row">
                    <span>Balance</span>
                    <strong>--</strong>
                </div>

                <div class="scanner-row">
                    <span>Open Trades</span>
                    <strong>0</strong>
                </div>

                <div class="scanner-row">
                    <span>Today's P/L</span>
                    <strong>--</strong>
                </div>

                <div class="scanner-row">
                    <span>Status</span>
                    <strong style="color:#12d6a2;">
                        Connect Exchange
                    </strong>
                </div>

            `;

            return;

        }

    }

    catch (err) {

        console.error(err);

    }

}

loadPortfolio();

setInterval(loadPortfolio,10000);