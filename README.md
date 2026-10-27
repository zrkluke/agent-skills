# Luke Agent Skills

個人維護的 Agent Skills catalog，整理可跨專案重複使用，並以 Codex 與 Claude Code 為目標的工作流程。

## 定位

- 收錄自己經常使用、值得標準化的工作流程。
- 保持 project-agnostic：skill 不依賴特定產品、程式碼庫或組織內部環境。
- 以可攜性優先：共用指令可同時用於 Codex 與 Claude Code；平台差異使用最小的 adapter 處理。

## Skills

| 名稱 | 技術 ID | 說明 |
| --- | --- | --- |
| [提交審閱](skills/luke-commit-review/) | `luke-commit-review` | 檢查 Git 變更、規劃提交拆分，並在確認後安全建立 commit。 |
| [火烤程式碼審查](skills/luke-code-review-roasted/) | `luke-code-review-roasted` | 針對變更進行直接、嚴格且建設性的程式碼審查。 |
| [OpenSpec TDD](skills/luke-openspec-use-tdd/) | `luke-openspec-use-tdd` | 以獨立規劃 commit 與可觀察的 Red-Green-Refactor 證據實作 OpenSpec change。 |
| [PR 說明撰寫](skills/luke-write-pr/) | `luke-write-pr` | 依 PR 淨變更撰寫清楚、易於審閱的 PR 草稿。 |
| [從研究到實作](skills/luke-research-to-code/) | `luke-research-to-code` | 依 CRISPY 八階段流程，先研究現況、對齊設計與大綱，再分段實作。 |

## 第三方 skill 推薦

以下 skills 由各自的上游專案維護，需另外安裝；本 repo 不收錄它們的內容。
使用 `npx skills` 的安裝指令需要 Node.js 與 npm，執行後可依提示選擇要使用的工具與 skills。

### Archify

[tt-a1i/archify](https://github.com/tt-a1i/archify) 可將需求、程式碼或 Mermaid 轉成互動式架構圖、流程圖等。

```sh
npx skills add tt-a1i/archify -g
```

### Diagram Design

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

### Ponytail

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

### Eval Skills

[ai-evals-course/evals-skills](https://github.com/ai-evals-course/evals-skills) 提供 LLM 評估相關 skills，包含評估流程健檢、失敗案例分析、合成資料、評審校準與 RAG 評估。

```sh
npx skills add https://github.com/ai-evals-course/evals-skills -g
```

只需要其中一個時，可以指定名稱，例如：

```sh
npx skills add https://github.com/ai-evals-course/evals-skills --skill eval-audit -g
```

`-g` 會安裝到使用者層級；若只想用在目前專案，可移除 `-g`。

### 第三方 skills 的更新方式

- **使用 `npx skills` 安裝**：獨立安裝的 skills 不會自動跟著上游更新。執行 `npx skills check` 檢查更新，再執行 `npx skills update` 更新；只更新使用者層級的 skills 可用 `npx skills update -g`。
- **使用 Codex plugin marketplace 安裝**：plugin 更新時，包含的 skills 也可隨 plugin 更新。Codex 會重新整理已設定的 Git marketplace；也可執行 `codex plugin marketplace upgrade <marketplace-name>` 手動重新整理。重新整理後開啟新對話，並確認安裝的 plugin 版本；來源、版本設定及平台行為都會影響取得的內容。[Codex plugin 文件](https://developers.openai.com/plugins/build/plugins)
- **使用 Claude Code plugin marketplace 安裝**：更新方式取決於 marketplace 的自動更新設定。第三方 marketplace 預設關閉自動更新，可在 `/plugin` 的 Marketplaces 分頁啟用；也可在 Installed 分頁選擇 Update now，或在終端機執行 `claude plugin update <plugin>@<marketplace>`。更新後執行 `/reload-plugins` 或開啟新對話。[Claude Code plugin 文件](https://code.claude.com/docs/en/discover-plugins#keep-plugins-updated)

不同安裝方式各自管理版本；安裝方式與可用的 skill 名稱以各上游文件為準。

## 設計原則

- 每個 skill 只有一份 `SKILL.md`，作為跨平台的唯一指令來源。
- 共用 frontmatter 僅保留 Agent Skills 標準的 `name` 與 `description`。
- 不要在共用內容使用 `$ARGUMENTS`、`${CLAUDE_*}`、`!` command injection 或其他 Claude Code 預處理語法。
- Codex 專屬的 UI、呼叫政策與 MCP 依賴放在選用的 `agents/openai.yaml`。
- 只有兩個平台的執行流程確實不同時，才建立由共同來源產生的平台 artifact；不要手動維護兩份幾乎相同的指令。

## 相容性基準與資料來源

本 repo 採用 [Agent Skills 規範](https://agentskills.io/specification) 的可攜子集：skill 目錄必須包含 `SKILL.md`，frontmatter 的 `name` 必須與目錄名稱一致，`description` 必須說明功能與使用時機。

- [OpenAI：Build skills](https://learn.chatgpt.com/docs/build-skills) 說明 Codex 的 skill 結構、載入位置與選用的 `agents/openai.yaml`。
- [Anthropic：Extend Claude with skills](https://code.claude.com/docs/en/slash-commands) 說明 Claude Code 的 `SKILL.md`、載入位置與平台專屬擴充語法。
- `scripts/validate_skills.py` 將共用 frontmatter 限制為 `name` 與 `description`，並拒絕 Claude Code 專屬的參數替換、環境變數替換與 shell injection，避免共用內容只在單一平台生效。

## Plugin 安裝

可將整套五個 skills 作為一個 plugin 安裝；skill 內容仍共用此 repository 的
`skills/` 目錄。

Codex：

```sh
codex plugin marketplace add zrkluke/agent-skills
codex plugin add luke-agent-skills@luke-agent-skills
```

Claude Code：

```text
/plugin marketplace add zrkluke/agent-skills
/plugin install luke-agent-skills@luke-agent-skills
```

## 手動安裝

將所需的 skill 目錄完整複製到目標工具的 skill discovery 位置。

- Codex：內建 skill installer 使用 `$CODEX_HOME/skills/<skill-name>/`（預設為 `~/.codex/skills/<skill-name>/`）；現行官方文件也列出使用者層級的 `~/.agents/skills/<skill-name>/` 與 repository 層級的 `.agents/skills/<skill-name>/`。請以 Codex 的 `/skills` 確認目前環境實際載入的位置。
- Claude Code：使用 `~/.claude/skills/<skill-name>/`，或專案內的 `.claude/skills/<skill-name>/`。

例如，安裝 `luke-commit-review` 時，複製整個
`skills/luke-commit-review/` 目錄，而不是只複製 `SKILL.md`。

## 驗證

在 repository 根目錄執行：

```powershell
python scripts/validate_skills.py
```

此檢查會驗證本 repo 的可攜性約定與基本 skill 結構。GitHub Actions 會在 push 與 pull request 時自動執行相同檢查。
