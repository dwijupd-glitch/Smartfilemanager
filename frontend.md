<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>StorageSentry v1.0 Control Panel</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #38bdf8;
            --accent-hover: #0ea5e9;
            --border: #334155;
            --alert-bg: #451a03;
            --alert-text: #fdba74;
        }

        body {
            font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
        }

        .container {
            width: 100%;
            max-width: 700px;
        }

        header {
            margin-bottom: 24px;
            text-align: center;
        }

        header h1 {
            font-size: 1.8rem;
            margin: 0 0 8px 0;
            color: var(--accent);
        }

        header p {
            color: var(--text-muted);
            margin: 0;
            font-size: 0.95rem;
        }

        .card {
            background-color: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }

        .form-group {
            margin-bottom: 16px;
        }

        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 500;
            font-size: 0.9rem;
        }

        input[type="text"] {
            width: 100%;
            padding: 12px;
            background-color: var(--bg-color);
            border: 1px solid var(--border);
            border-radius: 8px;
            color: var(--text-main);
            font-size: 1rem;
            box-sizing: border-box;
        }

        input[type="text"]:focus {
            outline: none;
            border-color: var(--accent);
        }

        button {
            background-color: var(--accent);
            color: #0f172a;
            border: none;
            padding: 12px 20px;
            font-size: 1rem;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            width: 100%;
            transition: background-color 0.2s;
        }

        button:hover {
            background-color: var(--accent-hover);
        }

        .analytics-header {
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 12px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 8px;
        }

        .stat-row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
            font-size: 0.95rem;
        }

        .stat-value {
            font-weight: 600;
            color: var(--accent);
        }

        .alert-box {
            background-color: var(--alert-bg);
            border: 1px solid #7c2d12;
            color: var(--alert-text);
            padding: 12px;
            border-radius: 8px;
            font-size: 0.9rem;
            margin-top: 10px;
        }

        .hidden {
            display: none;
        }
    </style>
</head>
<body>

    <div class="container">
        <header>
            <h1>StorageSentry v1.0</h1>
            <p>Automated Directory Organizer & Disk Analytics Engine</p>
        </header>

        <!-- Input Section -->
        <div class="card">
            <div class="form-group">
                <label for="targetPath">Target Directory Path</label>
                <input type="text" id="targetPath" placeholder="e.g., /Users/username/Downloads or C:\Users\...\Downloads">
            </div>
            <button onclick="runStorageSentry()">Run Directory Organizer</button>
        </div>

        <!-- Results / Analytics Section (Hidden by default until run) -->
        <div id="resultsCard" class="card hidden">
            <div class="analytics-header">Analytics Report</div>
            <div class="stat-row">
                <span>Total Storage Processed:</span>
                <span id="totalStorage" class="stat-value">0.00 MB</span>
            </div>

            <div style="margin-top: 16px; font-weight: 500; font-size: 0.9rem; color: var(--text-muted);">Category Distribution:</div>
            <div id="categoryDistribution" style="margin-top: 8px;">
                <!-- Dynamically populated stats will go here -->
            </div>

            <div class="analytics-header" style="margin-top: 20px;">Rule Alerts</div>
            <div id="alertContainer">
                <div class="stat-row" style="color: var(--text-muted);">No storage spikes or oversized files detected.</div>
            </div>
        </div>
    </div>

    <script>
        function runStorageSentry() {
            const pathInput = document.getElementById('targetPath').value;
            if (!pathInput) {
                alert('Please enter a valid directory path.');
                return;
            }

            // Mock interaction feedback (Replace this fetch call when connecting to a Flask/FastAPI backend)
            document.getElementById('resultsCard').classList.remove('hidden');
            
            // Example simulated output rendering
            document.getElementById('totalStorage').innerText = "142.50 MB";
            
            const distContainer = document.getElementById('categoryDistribution');
            distContainer.innerHTML = `
                <div class="stat-row"><span>• Documents</span><span class="stat-value">45.20% (64,487,200 bytes)</span></div>
                <div class="stat-row"><span>• Images</span><span class="stat-value">35.10% (50,012,100 bytes)</span></div>
                <div class="stat-row"><span>• Videos</span><span class="stat-value">19.70% (28,093,516 bytes)</span></div>
            `;

            const alertBox = document.getElementById('alertContainer');
            alertBox.innerHTML = `
                <div class="alert-box">
                    [ALERT] Storage Spike Warning: Category 'Documents' occupies 45.20% of total storage.
                </div>
            `;
        }
    </script>
</body>
</html>
