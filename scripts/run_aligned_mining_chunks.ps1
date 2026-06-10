param(
    [string]$Symbols = "EURUSD,GBPUSD,GBPJPY,USDJPY,EURJPY,GBPCHF,AUDUSD,GBPAUD,GBPNZD,EURGBP,XAUUSD,US30,USTEC",
    [int]$LimitPerSymbol = 2000,
    [int]$MinConfluence = 50,
    [int]$MinSpacingMinutes = 90,
    [switch]$WithCharts,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

$chunks = @(
    @{ Days = 90; Until = "2021-09-06" },
    @{ Days = 90; Until = "2021-12-05" },
    @{ Days = 90; Until = "2022-03-05" },
    @{ Days = 90; Until = "2022-06-03" },
    @{ Days = 90; Until = "2022-09-01" },
    @{ Days = 90; Until = "2022-11-30" },
    @{ Days = 90; Until = "2023-02-28" },
    @{ Days = 90; Until = "2023-05-29" },
    @{ Days = 90; Until = "2023-08-27" },
    @{ Days = 90; Until = "2023-11-25" },
    @{ Days = 90; Until = "2024-02-23" },
    @{ Days = 90; Until = "2024-05-23" },
    @{ Days = 90; Until = "2024-08-21" },
    @{ Days = 90; Until = "2024-11-19" },
    @{ Days = 90; Until = "2025-02-17" },
    @{ Days = 90; Until = "2025-05-18" },
    @{ Days = 90; Until = "2025-08-16" },
    @{ Days = 90; Until = "2025-11-14" },
    @{ Days = 90; Until = "2026-02-12" },
    @{ Days = 90; Until = "2026-05-13" },
    @{ Days = 26; Until = "2026-06-08" }
)

New-Item -ItemType Directory -Force -Path "logs\mining_chunks" | Out-Null

foreach ($chunk in $chunks) {
    $argsList = @(
        "-m", "helix_v3.backtest.historical_flashcard_miner", "mine",
        "--symbols", $Symbols,
        "--days", [string]$chunk.Days,
        "--until", $chunk.Until,
        "--min-confluence", [string]$MinConfluence,
        "--step-bars", "1",
        "--limit-per-symbol", [string]$LimitPerSymbol,
        "--min-spacing-minutes", [string]$MinSpacingMinutes,
        "--no-promote-library"
    )
    if (-not $WithCharts) {
        $argsList += "--no-charts"
    }

    $logPath = "logs\mining_chunks\mine_until_$($chunk.Until)_days_$($chunk.Days).log"
    $display = ".venv\Scripts\python.exe " + ($argsList -join " ")
    Write-Host "Chunk until $($chunk.Until), days $($chunk.Days)"
    Write-Host $display

    if ($DryRun) {
        continue
    }

    & ".venv\Scripts\python.exe" @argsList 2>&1 | Tee-Object -FilePath $logPath
    if ($LASTEXITCODE -ne 0) {
        throw "Mining chunk failed: until=$($chunk.Until), days=$($chunk.Days). See $logPath"
    }
}

$archiveArgs = @(
    "-m", "helix_v3.backtest.historical_flashcard_miner", "pair-study",
    "--archive-only",
    "--symbols", $Symbols,
    "--days", "1826",
    "--until", "2026-06-08",
    "--min-total", "10",
    "--min-favorable-rate", "55",
    "--min-avg-exit-pips", "0",
    "--baseline-favorable-rate", "85",
    "--baseline-avg-exit-pips", "10.9",
    "--split-min-total", "3",
    "--required-split-passes", "2",
    "--validation-days", "365",
    "--out-of-sample-days", "180",
    "--max-examples", "150"
)

$rebuildArgs = @(
    "-m", "helix_v3.backtest.validation_library", "rebuild",
    "--min-total", "10",
    "--min-favorable-rate", "85",
    "--min-avg-exit-pips", "10.9",
    "--min-symbols", "2"
)

$intelArgs = @("-m", "helix_v3.backtest.setup_intelligence", "rebuild")

foreach ($finalCommand in @($archiveArgs, $rebuildArgs, $intelArgs)) {
    $display = ".venv\Scripts\python.exe " + ($finalCommand -join " ")
    Write-Host $display
    if ($DryRun) {
        continue
    }
    & ".venv\Scripts\python.exe" @finalCommand
    if ($LASTEXITCODE -ne 0) {
        throw "Final mining/reporting command failed: $display"
    }
}
