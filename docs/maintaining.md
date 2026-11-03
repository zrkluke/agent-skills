# 維護說明

[回到 README](../README.md)

## 收錄原則

- 收錄自己經常使用、值得標準化的工作流程。
- Skill 不依賴特定產品、程式碼庫或組織內部環境，方便跨專案使用。
- 共用指令可同時用於 Codex 與 Claude Code；平台差異以最少的調整處理。

## 設計原則

- 每個 skill 只有一份 `SKILL.md`，作為跨平台的唯一指令來源。
- 共用 frontmatter 僅保留 Agent Skills 標準的 `name` 與 `description`。
- 不要在共用內容使用 `$ARGUMENTS`、`${CLAUDE_*}`、`!` command injection 或其他 Claude Code 預處理語法。
- Codex 專屬的 UI、呼叫政策與 MCP 依賴放在選用的 `agents/openai.yaml`。
- 只有兩個平台的執行流程確實不同時，才建立由共同來源產生的平台檔案；不要手動維護兩份幾乎相同的指令。

## 相容性基準與資料來源

本 repo 採用 [Agent Skills 規範](https://agentskills.io/specification) 的可攜子集：skill 目錄必須包含 `SKILL.md`，frontmatter 的 `name` 必須與目錄名稱一致，`description` 必須說明功能與使用時機。

- [OpenAI：Build skills](https://learn.chatgpt.com/docs/build-skills) 說明 Codex 的 skill 結構、載入位置與選用的 `agents/openai.yaml`。
- [Anthropic：Extend Claude with skills](https://code.claude.com/docs/en/slash-commands) 說明 Claude Code 的 `SKILL.md`、載入位置與平台專屬擴充語法。
- [scripts/validate_skills.py](../scripts/validate_skills.py) 將共用 frontmatter 限制為 `name` 與 `description`，並拒絕 Claude Code 專屬的參數替換、環境變數替換與 shell injection，避免共用內容只在單一平台生效。

## 驗證

在 repository 根目錄執行：

```powershell
python scripts/validate_skills.py
```

此檢查會驗證本 repo 的可攜性約定與基本 skill 結構。GitHub Actions 會在 push 與 pull request 時自動執行相同檢查。
