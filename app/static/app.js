document.addEventListener("DOMContentLoaded", () => {
    // API base URL
    const API_BASE = "";

    // State Variables
    let decisionsChart = null;
    let currentDbTable = "users";

    // DOM Elements
    const navItems = document.querySelectorAll(".nav-item");
    const panels = document.querySelectorAll(".panel");
    const dbTabBtns = document.querySelectorAll(".db-tab-btn");
    const refreshBtn = document.getElementById("btn-refresh-data");

    // Toast Notification helper
    function showToast(message, type = "info") {
        const toast = document.getElementById("toast");
        const icon = document.getElementById("toast-icon");
        const msgSpan = document.getElementById("toast-message");

        // Remove old classes
        toast.className = "toast";
        toast.classList.add(type);

        // Icon settings
        icon.className = "fa-solid";
        if (type === "success") {
            icon.classList.add("fa-circle-check");
        } else if (type === "error") {
            icon.classList.add("fa-circle-exclamation");
        } else {
            icon.classList.add("fa-circle-info");
        }

        msgSpan.textContent = message;
        toast.classList.remove("hidden");

        // Auto hide after 3 seconds
        setTimeout(() => {
            toast.classList.add("hidden");
        }, 3000);
    }

    // Tab Switching Navigation
    navItems.forEach(item => {
        item.addEventListener("click", (e) => {
            e.preventDefault();
            const target = item.getAttribute("data-target");

            navItems.forEach(i => i.classList.remove("active"));
            panels.forEach(p => p.classList.remove("active"));

            item.classList.add("active");
            document.getElementById(`panel-${target}`).classList.add("active");

            // Custom tasks based on panel
            if (target === "database") {
                loadDatabaseTable(currentDbTable);
            } else if (target === "overview") {
                loadOverviewStats();
            }
        });
    });

    // DB Viewer Sub-Tab Switching
    dbTabBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            dbTabBtns.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");
            
            const tableName = btn.getAttribute("data-table");
            currentDbTable = tableName;
            loadDatabaseTable(tableName);
        });
    });

    // Global Refresh Trigger
    if (refreshBtn) {
        refreshBtn.addEventListener("click", () => {
            loadOverviewStats();
            populateDropdowns();
            showToast("Database and statistics synchronized!", "success");
        });
    }

    // --- FORM SUBMISSIONS ---

    // 1. Register User Form
    const createUserForm = document.getElementById("form-create-user");
    if (createUserForm) {
        createUserForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const formData = new FormData(createUserForm);
            const data = Object.fromEntries(formData.entries());

            try {
                const response = await fetch(`${API_BASE}/api/users`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(data)
                });

                if (!response.ok) {
                    const err = await response.json();
                    throw new Error(err.detail || "Failed to create user");
                }

                showToast(`User "${data.name}" registered successfully!`, "success");
                createUserForm.reset();
                populateDropdowns();
                loadOverviewStats();
            } catch (error) {
                showToast(error.message, "error");
            }
        });
    }

    // 2. Create Applicant Profile Form
    const createProfileForm = document.getElementById("form-create-profile");
    if (createProfileForm) {
        createProfileForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const formData = new FormData(createProfileForm);
            const data = Object.fromEntries(formData.entries());
            
            // Clean user_id if empty
            if (data.user_id === "") {
                data.user_id = null;
            } else {
                data.user_id = parseInt(data.user_id);
            }
            data.dependents = parseInt(data.dependents);

            try {
                const response = await fetch(`${API_BASE}/api/profiles`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(data)
                });

                if (!response.ok) {
                    const err = await response.json();
                    throw new Error(err.detail || "Failed to create profile");
                }

                showToast("Applicant profile created successfully!", "success");
                createProfileForm.reset();
                populateDropdowns();
                loadOverviewStats();
            } catch (error) {
                showToast(error.message, "error");
            }
        });
    }

    // 3. Associate Credit History Form
    const addCreditForm = document.getElementById("form-add-credit");
    if (addCreditForm) {
        addCreditForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const formData = new FormData(addCreditForm);
            const data = Object.fromEntries(formData.entries());

            data.applicant_id = parseInt(data.applicant_id);
            data.credit_score = parseFloat(data.credit_score);
            data.credit_history_status = parseInt(data.credit_history_status);

            try {
                const response = await fetch(`${API_BASE}/api/credit-histories`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(data)
                });

                if (!response.ok) {
                    const err = await response.json();
                    throw new Error(err.detail || "Failed to save credit history");
                }

                showToast("Credit history linked to applicant!", "success");
                addCreditForm.reset();
                loadOverviewStats();
            } catch (error) {
                showToast(error.message, "error");
            }
        });
    }

    // 4. Submit Loan Application Form
    const createLoanForm = document.getElementById("form-create-loan");
    if (createLoanForm) {
        createLoanForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const formData = new FormData(createLoanForm);
            const data = Object.fromEntries(formData.entries());

            data.applicant_id = parseInt(data.applicant_id);
            data.income = parseFloat(data.income);
            data.coapplicant_income = parseFloat(data.coapplicant_income);
            data.loan_amount = parseFloat(data.loan_amount);
            data.loan_term = parseInt(data.loan_term);

            try {
                const response = await fetch(`${API_BASE}/api/loans`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(data)
                });

                if (!response.ok) {
                    const err = await response.json();
                    throw new Error(err.detail || "Failed to submit loan request");
                }

                showToast("Loan application submitted successfully!", "success");
                createLoanForm.reset();
                populateDropdowns();
                loadOverviewStats();
            } catch (error) {
                showToast(error.message, "error");
            }
        });
    }

    // 5. Run Prediction / Evaluation Form
    const runPredictionForm = document.getElementById("form-run-prediction");
    const resultPlaceholder = document.querySelector(".result-placeholder");
    const resultContent = document.getElementById("prediction-result-content");
    const displayCard = document.getElementById("prediction-result-display");

    if (runPredictionForm) {
        runPredictionForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const formData = new FormData(runPredictionForm);
            const data = Object.fromEntries(formData.entries());

            data.loan_id = parseInt(data.loan_id);
            data.model_id = parseInt(data.model_id);

            // Visual feedback: evaluating state
            resultPlaceholder.innerHTML = `
                <i class="fa-solid fa-gear fa-spin placeholder-brain" style="color: var(--color-secondary);"></i>
                <h4>Evaluating Applicant risk...</h4>
                <p>Retrieving applicant profiles, credit history and parsing metrics through XGBoost model.</p>
            `;
            resultPlaceholder.classList.remove("hidden");
            resultContent.classList.add("hidden");

            try {
                // Delay slightly to give a realistic machine learning compute feeling
                await new Promise(r => setTimeout(r, 800));

                const response = await fetch(`${API_BASE}/api/predictions/run`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(data)
                });

                if (!response.ok) {
                    const err = await response.json();
                    throw new Error(err.detail || "Model prediction execution failed");
                }

                const result = await response.json();
                renderPredictionResult(result);
                loadOverviewStats();
                showToast("Evaluation complete! Prediction stored in database.", "success");
            } catch (error) {
                showToast(error.message, "error");
                // Reset placeholder on error
                resultPlaceholder.innerHTML = `
                    <i class="fa-solid fa-circle-exclamation placeholder-brain" style="color: var(--color-danger);"></i>
                    <h4>Evaluation Failed</h4>
                    <p>${error.message}</p>
                `;
            }
        });
    }

    function renderPredictionResult(result) {
        resultPlaceholder.classList.add("hidden");
        resultContent.classList.remove("hidden");

        const statusBox = document.getElementById("result-status-box");
        const statusIcon = document.getElementById("result-status-icon");
        const statusTitle = document.getElementById("result-status-title");
        const probabilityPercent = document.getElementById("result-probability-percent");
        const radialIndicator = document.querySelector(".probability-score-radial");
        
        const predId = document.getElementById("result-prediction-id");
        const predTime = document.getElementById("result-prediction-time");
        const modelName = document.getElementById("result-model-name");

        // Format outputs
        const prob = Math.round(result.probability_score * 100);
        probabilityPercent.textContent = `${prob}%`;
        predId.textContent = `#PRD-${result.prediction_id}`;
        predTime.textContent = new Date(result.prediction_time).toLocaleString();
        
        // Find selected model name
        const modelSelect = document.getElementById("pred-model-id");
        modelName.textContent = modelSelect.options[modelSelect.selectedIndex]?.text || `Model ID: ${result.model_id}`;

        // Set Approved/Rejected aesthetics
        statusBox.className = "result-status-header";
        statusIcon.className = "fa-solid";
        
        if (result.prediction_status === "Approved") {
            statusBox.classList.add("approved");
            statusIcon.classList.add("fa-circle-check");
            statusTitle.textContent = "Approved";
            // Success ring coloration
            radialIndicator.style.background = `conic-gradient(var(--color-success) ${prob}%, rgba(255, 255, 255, 0.05) ${prob}%)`;
            radialIndicator.style.boxShadow = "0 0 25px var(--color-success-glow)";
        } else {
            statusBox.classList.add("rejected");
            statusIcon.classList.add("fa-triangle-exclamation");
            statusTitle.textContent = "Rejected";
            // Danger ring coloration
            radialIndicator.style.background = `conic-gradient(var(--color-danger) ${prob}%, rgba(255, 255, 255, 0.05) ${prob}%)`;
            radialIndicator.style.boxShadow = "0 0 25px var(--color-danger-glow)";
        }
    }

    // --- POPULATE SELECTION DROPDOWNS ---
    async function populateDropdowns() {
        try {
            // Populate Users dropdown
            const uRes = await fetch(`${API_BASE}/api/users`);
            const users = await uRes.json();
            const userSelect = document.getElementById("prof-user-id");
            userSelect.innerHTML = `<option value="">-- Choose User --</option>`;
            users.forEach(u => {
                userSelect.innerHTML += `<option value="${u.user_id}">${u.name} (${u.role})</option>`;
            });

            // Populate Profiles dropdowns
            const pRes = await fetch(`${API_BASE}/api/profiles`);
            const profiles = await pRes.json();
            const creditProfileSelect = document.getElementById("credit-applicant-id");
            const loanProfileSelect = document.getElementById("loan-applicant-id");
            
            creditProfileSelect.innerHTML = `<option value="">-- Select Profile --</option>`;
            loanProfileSelect.innerHTML = `<option value="">-- Choose Applicant Profile --</option>`;
            
            profiles.forEach(p => {
                const label = `Profile #${p.applicant_id} [${p.gender}, Dep: ${p.dependents}, ${p.education}]`;
                creditProfileSelect.innerHTML += `<option value="${p.applicant_id}">${label}</option>`;
                loanProfileSelect.innerHTML += `<option value="${p.applicant_id}">${label}</option>`;
            });

            // Populate Loan Applications dropdown
            const lRes = await fetch(`${API_BASE}/api/loans`);
            const loans = await lRes.json();
            const predLoanSelect = document.getElementById("pred-loan-id");
            predLoanSelect.innerHTML = `<option value="">-- Choose Loan Application --</option>`;
            loans.forEach(l => {
                const label = `App #${l.loan_id} (Income: $${l.income}, Request: $${l.loan_amount}k)`;
                predLoanSelect.innerHTML += `<option value="${l.loan_id}">${label}</option>`;
            });

            // Populate Models dropdown
            const mRes = await fetch(`${API_BASE}/api/models`);
            const models = await mRes.json();
            const predModelSelect = document.getElementById("pred-model-id");
            predModelSelect.innerHTML = `<option value="">-- Select Model --</option>`;
            
            if (models.length > 0) {
                models.forEach(m => {
                    predModelSelect.innerHTML += `<option value="${m.model_id}">${m.model_name}</option>`;
                });
                
                // Select first model automatically
                predModelSelect.value = models[0].model_id;

                // Update Sidebar Model details
                const activeModel = models[0];
                document.getElementById("active-model-id").textContent = activeModel.model_id;
                document.getElementById("model-status-text").textContent = activeModel.model_name;
                document.getElementById("model-train-acc").textContent = `${Math.round(activeModel.training_accuracy * 100)}%`;
                document.getElementById("model-test-acc").textContent = `${Math.round(activeModel.testing_accuracy * 100)}%`;
                
                document.getElementById("model-dot").className = "pulse-dot green";
            } else {
                document.getElementById("model-status-text").textContent = "No Trained Models";
                document.getElementById("model-dot").className = "pulse-dot red";
            }
        } catch (error) {
            console.error("Error populating select fields:", error);
        }
    }

    // --- RENDER ANALYTICS CHARTS ---
    function renderCharts(approved, rejected) {
        const ctx = document.getElementById("chart-decisions");
        if (!ctx) return;

        if (decisionsChart) {
            decisionsChart.destroy();
        }

        if (approved === 0 && rejected === 0) {
            // Render default chart if no data
            decisionsChart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    labels: ['Pending System Evaluations'],
                    datasets: [{
                        data: [100],
                        backgroundColor: ['rgba(255, 255, 255, 0.05)'],
                        borderColor: ['rgba(255, 255, 255, 0.08)'],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: true, position: 'bottom', labels: { color: '#94a3b8' } }
                    }
                }
            });
            return;
        }

        decisionsChart = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Approved Loans', 'Rejected Loans'],
                datasets: [{
                    data: [approved, rejected],
                    backgroundColor: [
                        'rgba(16, 185, 129, 0.6)', // Emerald green
                        'rgba(244, 63, 94, 0.6)'    // Rose red
                    ],
                    borderColor: [
                        '#10b981',
                        '#f43f5e'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: true,
                        position: 'bottom',
                        labels: {
                            color: '#94a3b8',
                            font: { family: 'Inter', size: 12 }
                        }
                    }
                },
                cutout: '70%'
            }
        });
    }

    // --- LOAD OVERVIEW STATS & RECENT TABLE ---
    async function loadOverviewStats() {
        try {
            const response = await fetch(`${API_BASE}/api/dashboard/stats`);
            const stats = await response.json();

            // Load metrics counts
            document.getElementById("stat-total-apps").textContent = stats.total_applications;
            document.getElementById("stat-approval-rate").textContent = `${stats.approval_rate}%`;
            document.getElementById("stat-total-profiles").textContent = stats.total_profiles;
            document.getElementById("stat-avg-credit").textContent = stats.average_credit_score || "--";

            // Render distribution charts
            renderCharts(stats.approved_predictions, stats.rejected_predictions);

            // Populate recent predictions list
            const pRes = await fetch(`${API_BASE}/api/predictions?limit=5`);
            const predictions = await pRes.json();
            const recentBody = document.querySelector("#table-recent-predictions tbody");
            recentBody.innerHTML = "";

            if (predictions.length === 0) {
                recentBody.innerHTML = `<tr><td colspan="5" class="text-center">No predictions run yet.</td></tr>`;
            } else {
                predictions.reverse().slice(0, 5).forEach(p => {
                    const date = new Date(p.prediction_time).toLocaleDateString();
                    const statusClass = p.prediction_status === "Approved" ? "approved" : "rejected";
                    const prob = Math.round(p.probability_score * 100);
                    
                    recentBody.innerHTML += `
                        <tr>
                            <td>#${p.loan_id}</td>
                            <td>${p.prediction_id}</td>
                            <td><span class="badge ${statusClass}">${p.prediction_status}</span></td>
                            <td><strong>${prob}%</strong></td>
                            <td>${date}</td>
                        </tr>
                    `;
                });
            }
        } catch (error) {
            console.error("Error loading dashboard stats:", error);
        }
    }

    // --- LOAD DATABASE TABLE VIEWS ---
    async function loadDatabaseTable(tableName) {
        const table = document.getElementById("system-db-table");
        const thead = table.querySelector("thead");
        const tbody = table.querySelector("tbody");

        thead.innerHTML = "";
        tbody.innerHTML = `<tr><td class="text-center" colspan="100%">Loading records...</td></tr>`;

        try {
            let endpoint = "";
            if (tableName === "users") endpoint = "/api/users";
            else if (tableName === "profiles") endpoint = "/api/profiles";
            else if (tableName === "loans") endpoint = "/api/loans";
            else if (tableName === "predictions") endpoint = "/api/predictions";

            const res = await fetch(`${API_BASE}${endpoint}`);
            const data = await res.json();

            tbody.innerHTML = "";

            if (data.length === 0) {
                thead.innerHTML = `<tr><th>System Information</th></tr>`;
                tbody.innerHTML = `<tr><td class="text-center">No records found in this table yet.</td></tr>`;
                return;
            }

            // Build dynamic headers based on keys of the first row object
            const headers = Object.keys(data[0]);
            let headerRow = "<tr>";
            headers.forEach(h => {
                headerRow += `<th>${h.replace("_", " ").toUpperCase()}</th>`;
            });
            headerRow += "</tr>";
            thead.innerHTML = headerRow;

            // Build dynamic rows
            data.forEach(row => {
                let rowHtml = "<tr>";
                headers.forEach(h => {
                    let val = row[h];
                    
                    // Format dates
                    if (typeof val === "string" && (val.includes("T") || h.includes("date") || h.includes("time"))) {
                        const d = new Date(val);
                        if (!isNaN(d.getTime())) {
                            val = d.toLocaleString();
                        }
                    }

                    // Badges for values
                    if (h === "prediction_status" || h === "role") {
                        const statusClass = val.toLowerCase().replace(" ", "-");
                        rowHtml += `<td><span class="badge ${statusClass}">${val}</span></td>`;
                    } else if (h === "probability_score") {
                        rowHtml += `<td><strong>${Math.round(val * 100)}%</strong></td>`;
                    } else {
                        rowHtml += `<td>${val === null ? '<em style="color:var(--text-muted)">None</em>' : val}</td>`;
                    }
                });
                rowHtml += "</tr>";
                tbody.innerHTML += rowHtml;
            });
        } catch (error) {
            tbody.innerHTML = `<tr><td class="text-center" style="color:var(--color-danger)">Error loading table: ${error.message}</td></tr>`;
        }
    }

    // --- INITIAL DATA SYNC ---
    loadOverviewStats();
    populateDropdowns();
});
