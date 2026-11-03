# 第三方 skill 與工具推薦

[回到 README](../README.md)

以下 skills 與工具由各自的上游專案維護，需另外安裝或設定；本 repo 不收錄它們的內容。
使用 `npx skills` 的安裝指令需要 Node.js 與 npm，執行後可依提示選擇要使用的工具與 skills。

## Archify

[tt-a1i/archify](https://github.com/tt-a1i/archify) 可將需求、程式碼或 Mermaid 轉成互動式架構圖、流程圖等。

```sh
npx skills add tt-a1i/archify -g
```

## Diagram Design

[cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) 可製作架構圖、流程圖、時序圖、資料模型與各種圖表，也支援匯入 Mermaid 等格式。

Codex：

```sh
codex plugin marketplace add cathrynlavery/diagram-design
codex plugin add diagram-design@diagram-design
```

Claude Code：

```text
/plugin marketplace add cathrynlavery/diagram-design
/plugin install diagram-design@diagram-design
```

## Ponytail

[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) 協助在開發與審查時找出能完整解決問題的精簡做法，避免不必要的複雜度。

套件也提供以下 skills：

- `ponytail-review`：審查程式碼變更，檢查錯誤、安全性、測試、效能與多餘程式碼。
- `ponytail-audit`：檢查整個 repo，依影響程度整理問題。
- `ponytail-debt`：整理程式碼中標記的 `shortcut:` 技術債。
- `ponytail-gain`：查看 Ponytail 基準測試中測得的程式碼、成本與速度變化。
- `ponytail-help`：查看 Ponytail 的使用方式與指令。

Codex：

```sh
codex plugin marketplace add DietrichGebert/ponytail
codex plugin add ponytail@ponytail
```

接著依上游說明，在 Codex 開啟 `/hooks` 並信任兩個 lifecycle hooks，再開始新的對話。

Claude Code：

```text
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

## Eval Skills

[ai-evals-course/evals-skills](https://github.com/ai-evals-course/evals-skills) 提供 LLM 評估相關 skills，包含評估流程健檢、失敗案例分析、合成資料、評審校準與 RAG 評估。

```sh
npx skills add https://github.com/ai-evals-course/evals-skills -g
```

只需要其中一個時，可以指定名稱，例如：

```sh
npx skills add https://github.com/ai-evals-course/evals-skills --skill eval-audit -g
```

`-g` 會安裝到使用者層級；若只想用在目前專案，可移除 `-g`。

## pstack

[pstack 原始專案](https://github.com/cursor/plugins/tree/main/pstack) 由 [Lauren Tan（poteto）](https://github.com/poteto) 撰寫，收錄於 Cursor 官方的 `cursor/plugins` repo；[plugin 設定檔](https://github.com/cursor/plugins/blob/main/pstack/.cursor-plugin/plugin.json) 也標示 Lauren Tan 為作者。

以 `poteto-mode` 為主要入口，依任務選擇程式碼理解、設計、除錯、審查與驗證等工作流程，並搭配多模型與平行執行。

Cursor：

```text
/add-plugin pstack
```

安裝後，先執行 `/setup-pstack` 設定模型與推理預算，再用 `/poteto-mode` 開始任務。

Claude Code（[上游安裝說明](https://github.com/cursor/plugins/blob/main/pstack/README.md#install)）：

```text
/plugin marketplace add cursor/plugins
/plugin install pstack@cursor-plugins
```

在 Claude Code 中，使用 `/pstack:setup-pstack` 設定，再以 `/pstack:poteto-mode` 開始任務；Cursor 專屬功能的對應與限制見[上游相容說明](https://github.com/cursor/plugins/blob/main/pstack/docs/harness/claude-code.md)。

Codex 等工具另有 [michael-denyer/pstack-claude](https://github.com/michael-denyer/pstack-claude) 社群移植版，由不同維護者管理；安裝方式與原版差異請以該專案文件為準。

## auto-harness

[neosigmaai/auto-harness](https://github.com/neosigmaai/auto-harness) 是獨立的 agent harness 最佳化專案。從運作方式來看，可視為 meta-harness：由外層 agent 分析內層 agent 的失敗紀錄，修改提示詞、工具與執行邏輯，再以評估結果決定是否保留改動。

依[上游設定說明](https://github.com/neosigmaai/auto-harness#first-run-checklist)選定 benchmark、設定環境並執行 baseline，再讓外層 agent 讀取產生的 `PROGRAM.md`，開始「執行評估 → 分析失敗 → 修改 harness → 驗證 → 記錄」的循環。修好的訓練案例會加入回歸集，累積成後續改動的檢查項目。

使用時要留意目前的[驗證方式](https://github.com/neosigmaai/auto-harness/blob/main/gating.py)：

- 每輪都以 test 分數決定是否保留改動，實際上扮演驗證集的角色；若要驗收泛化，應另留一份不參與選版的最終測試集。
- 回歸集預設要求通過率達 80%，再要求 test 平均分數不低於歷來最佳值，仍可能有個別案例退步。
- [最佳化流程](https://github.com/neosigmaai/auto-harness/blob/main/program_templates/base.md)沒有內建上線前的人工審查；正式採用改動前，需另外檢查品質、token 用量、延遲與成本。

專案更新請依上游 repo 的說明處理。

## 第三方 skills 的更新方式

- **使用 `npx skills` 安裝**：獨立安裝的 skills 不會自動跟著上游更新。執行 `npx skills check` 檢查更新，再執行 `npx skills update` 更新；只更新使用者層級的 skills 可用 `npx skills update -g`。
- **使用 Codex plugin marketplace 安裝**：plugin 更新時，包含的 skills 也可隨 plugin 更新。Codex 會重新整理已設定的 Git marketplace；也可執行 `codex plugin marketplace upgrade <marketplace-name>` 手動重新整理。重新整理後開啟新對話，並確認安裝的 plugin 版本；來源、版本設定及平台行為都會影響取得的內容。[Codex plugin 文件](https://developers.openai.com/plugins/build/plugins)
- **使用 Claude Code plugin marketplace 安裝**：更新方式取決於 marketplace 的自動更新設定。第三方 marketplace 預設關閉自動更新，可在 `/plugin` 的 Marketplaces 分頁啟用；也可在 Installed 分頁選擇 Update now，或在終端機執行 `claude plugin update <plugin>@<marketplace>`。更新後執行 `/reload-plugins` 或開啟新對話。[Claude Code plugin 文件](https://code.claude.com/docs/en/discover-plugins#keep-plugins-updated)

不同安裝方式各自管理版本；安裝方式與可用的 skill 名稱以各上游文件為準。
