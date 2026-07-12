async function loadNews() {

    try {

        const response = await fetch("/api/news");

        const news = await response.json();

        const widget = document.getElementById("news-widget");

        if (!widget) return;

        widget.innerHTML = "";

        news.slice(0,6).forEach(item=>{

            let icon="🟡";

            const title=item.title.toLowerCase();

            if(
                title.includes("rise") ||
                title.includes("record") ||
                title.includes("approval") ||
                title.includes("inflow") ||
                title.includes("launch")
            ){
                icon="🟢";
            }

            if(
                title.includes("hack") ||
                title.includes("delay") ||
                title.includes("sell") ||
                title.includes("outflow") ||
                title.includes("tension") ||
                title.includes("scam")
            ){
                icon="🔴";
            }

            widget.innerHTML += `

            <div class="scanner-row">

                <div>

                    <strong>${icon} ${item.title}</strong>

                    <br>

                    <small>${item.source}</small>

                </div>

            </div>

            `;

        });

    }

    catch(err){

        console.log(err);

    }

}

loadNews();

setInterval(loadNews,60000);