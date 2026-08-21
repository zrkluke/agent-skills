# Luke Agent Skills

個人維護的 Agent Skills catalog，整理可跨專案重複使用，並以 Codex 與 Claude Code 為目標的工作流程。

## 定位

- 收錄自己經常使用、值得標準化的工作流程。
- 保持 project-agnostic：skill 不依賴特定產品、程式碼庫或組織內部環境。
- 以可攜性優先：共用指令可同時用於 Codex 與 Claude Code；平台差異使用最小的 adapter 處理。

## Skills

| 名稱 | 技術 ID | 說明 |
| --- | --- | --- |
| [提交審閱](skills/git-commit-review/) | `git-commit-review` | 檢查 Git 變更、規劃提交拆分，並在確認後安全建立 commit。 |
| [火烤程式碼審查](skills/code-review-roasted/) | `code-review-roasted` | 針對變更進行直接、嚴格且建設性的程式碼審查。 |
| [OpenSpec TDD](skills/openspec-use-tdd/) | `openspec-use-tdd` | 以獨立規劃 commit 與可觀察的 Red-Green-Refactor 證據實作 OpenSpec change。 |

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

## 安裝

將所需的 skill 目錄完整複製到目標工具的 skill discovery 位置。

- Codex：內建 skill installer 使用 `$CODEX_HOME/skills/<skill-name>/`（預設為 `~/.codex/skills/<skill-name>/`）；現行官方文件也列出使用者層級的 `~/.agents/skills/<skill-name>/` 與 repository 層級的 `.agents/skills/<skill-name>/`。請以 Codex 的 `/skills` 確認目前環境實際載入的位置。
- Claude Code：使用 `~/.claude/skills/<skill-name>/`，或專案內的 `.claude/skills/<skill-name>/`。

例如，安裝 `git-commit-review` 時，複製整個
`skills/git-commit-review/` 目錄，而不是只複製 `SKILL.md`。

## 驗證

在 repository 根目錄執行：

```powershell
python scripts/validate_skills.py
```

此檢查會驗證本 repo 的可攜性約定與基本 skill 結構。GitHub Actions 會在 push 與 pull request 時自動執行相同檢查。
