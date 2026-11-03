# Luke Agent Skills

整理可跨專案使用、支援 Codex 與 Claude Code 的 skills，也保存個人全域指令。

由 [Luke（zrkluke）](https://github.com/zrkluke) 維護 · [部落格](https://lukedevnotes.com/en) · [原始專案與最新版本](https://github.com/zrkluke/agent-skills)。

## Skills

| 名稱 | 技術 ID | 說明 |
| --- | --- | --- |
| [提交審閱](skills/luke-commit-review/) | `luke-commit-review` | 檢查 Git 變更、規劃提交拆分，並在確認後安全建立 commit。 |
| [火烤程式碼審查](skills/luke-code-review-roasted/) | `luke-code-review-roasted` | 針對變更進行直接、嚴格且建設性的程式碼審查。 |
| [OpenSpec TDD](skills/luke-openspec-use-tdd/) | `luke-openspec-use-tdd` | 以獨立規劃 commit 與可觀察的 Red-Green-Refactor 證據實作 OpenSpec change。 |
| [PR 說明撰寫](skills/luke-write-pr/) | `luke-write-pr` | 依 PR 淨變更撰寫清楚、易於審閱的 PR 草稿。 |
| [從研究到實作](skills/luke-research-to-code/) | `luke-research-to-code` | 依 CRISPY 八階段流程，先研究現況、對齊設計與大綱，再分段實作。 |

## 安裝

可透過 plugin 安裝全部 skills：

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

### 手動安裝

將所需的 `skills/<skill-name>/` 目錄完整複製到下列位置，包含 `SKILL.md` 與其附屬檔案：

| 工具 | 使用者層級 | 目前專案 |
| --- | --- | --- |
| Codex | `~/.agents/skills/<skill-name>/` | `.agents/skills/<skill-name>/` |
| Claude Code | `~/.claude/skills/<skill-name>/` | `.claude/skills/<skill-name>/` |

載入細節見 [Codex](https://learn.chatgpt.com/docs/build-skills) 與 [Claude Code](https://code.claude.com/docs/en/slash-commands) 官方文件。

## 第三方 skill 與工具推薦

以下 skills 與工具由各自的上游專案維護，需另外安裝或設定；本 repo 不收錄它們的內容。

| 名稱 | 用途 |
| --- | --- |
| [Archify](https://github.com/tt-a1i/archify) | 將需求、程式碼或 Mermaid 轉成互動式圖表。 |
| [Diagram Design](https://github.com/cathrynlavery/diagram-design) | 製作架構圖、流程圖、資料模型與各種圖表。 |
| [Ponytail](https://github.com/DietrichGebert/ponytail) | 精簡開發做法，並提供變更審查、整個 repo 檢查與技術債整理。 |
| [Eval Skills](https://github.com/ai-evals-course/evals-skills) | 協助 LLM 評估、失敗案例分析、合成資料與 RAG 評估。 |
| [pstack](https://github.com/cursor/plugins/tree/main/pstack) | poteto 的工程工作流程，涵蓋程式碼理解、設計、除錯、審查與驗證。 |
| [auto-harness](https://github.com/neosigmaai/auto-harness) | 根據失敗紀錄反覆改善 agent harness，並透過評估與回歸檢查決定是否保留改動。 |

安裝設定、功能與更新方式請見[第三方 skill 與工具使用說明](docs/third-party-skills.md)。

## 全域指令

`global/` 保存個人全域指令，檔案與預設套用位置如下：

| Repo 內檔案 | 本機預設位置 |
| --- | --- |
| [global/codex/AGENTS.md](global/codex/AGENTS.md) | `~/.codex/AGENTS.md` |
| [global/claude/CLAUDE.md](global/claude/CLAUDE.md) | `~/.claude/CLAUDE.md` |

需自行複製到對應位置；安裝本 repo 的 plugin 不會自動套用或同步這些檔案。

## 驗證

在 repository 根目錄執行：

```powershell
python scripts/validate_skills.py
```

GitHub Actions 會執行相同檢查。設計原則、相容性約定與資料來源見[維護說明](docs/maintaining.md)。

## 授權與來源標示

Skills、文件與設定採用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh-hant)，`scripts/` 程式碼採用 [MIT](scripts/LICENSE)。

適用範圍與條款見 [LICENSE](LICENSE)；署名要求與轉載範例見[來源標示說明](docs/attribution.md)。
