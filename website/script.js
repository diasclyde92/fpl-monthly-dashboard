// ==========================================
// Fantasy Premier League Monthly Dashboard
// ==========================================

let dashboard;
let currentMonth;

async function loadDashboard() {

    try {

        const response = await fetch("leaderboard.json");

        if (!response.ok) {
            throw new Error("Unable to load leaderboard.json");
        }

        dashboard = await response.json();

        document.getElementById("league-name").textContent =
            dashboard.league_name;

        document.getElementById("updated").textContent =
            "Last Updated: " + dashboard.last_updated;

        buildMonthButtons();

        currentMonth = Object.keys(dashboard.months)[0];

        showMonth(currentMonth);

        buildOverall();

    } catch (err) {

        document.body.innerHTML = `
            <div class="container py-5">
                <div class="alert alert-danger">
                    <h3>Unable to load dashboard.</h3>
                    <p>${err.message}</p>
                </div>
            </div>
        `;

    }

}

function buildMonthButtons() {

    const container = document.getElementById("month-buttons");

    container.innerHTML = "";

    Object.keys(dashboard.months).forEach(month => {

        const button = document.createElement("button");

        button.textContent = month;

        button.onclick = () => {

            document
                .querySelectorAll(".month-buttons button")
                .forEach(b => b.classList.remove("active"));

            button.classList.add("active");

            showMonth(month);

        };

        container.appendChild(button);

    });

    container.firstChild.classList.add("active");

}

function showMonth(month) {

    const managers = dashboard.months[month];

    buildPodium(managers);

    buildMonthlyTable(managers);

}

function buildPodium(managers) {

    const first = managers[0];
    const second = managers[1];
    const third = managers[2];

    document.getElementById("first-place").innerHTML =
        createPodiumCard("🥇", first);

    document.getElementById("second-place").innerHTML =
        createPodiumCard("🥈", second);

    document.getElementById("third-place").innerHTML =
        createPodiumCard("🥉", third);

}

function createPodiumCard(icon, manager) {

    if (!manager) return "";

    return `
        <div class="podium-rank">${icon}</div>

        <div class="podium-name">
            ${manager.manager}
        </div>

        <div class="podium-team">
            ${manager.team}
        </div>

        <div class="podium-points">
            ${manager.points} pts
        </div>
    `;

}

function buildMonthlyTable(managers) {

    const tbody = document.getElementById("monthly-table");

    tbody.innerHTML = "";

    managers.forEach(manager => {

        let badge = manager.rank;

        if (manager.rank === 1)
            badge = '<span class="rank gold">1</span>';

        if (manager.rank === 2)
            badge = '<span class="rank silver">2</span>';

        if (manager.rank === 3)
            badge = '<span class="rank bronze">3</span>';

        tbody.innerHTML += `
            <tr>

                <td>${badge}</td>

                <td>${manager.manager}</td>

                <td>${manager.team}</td>

                <td><strong>${manager.points}</strong></td>

            </tr>
        `;

    });

}

function buildOverall() {

    const tbody = document.getElementById("overall-table");

    tbody.innerHTML = "";

    dashboard.overall.forEach(manager => {

        let badge = manager.rank;

        if (manager.rank === 1)
            badge = '<span class="rank gold">1</span>';

        if (manager.rank === 2)
            badge = '<span class="rank silver">2</span>';

        if (manager.rank === 3)
            badge = '<span class="rank bronze">3</span>';

        tbody.innerHTML += `
            <tr>

                <td>${badge}</td>

                <td>${manager.manager}</td>

                <td>${manager.team}</td>

                <td><strong>${manager.points}</strong></td>

            </tr>
        `;

    });

}

loadDashboard();