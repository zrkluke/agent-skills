---
name: git-commit-review
description: 依使用者與專案規範檢查、review、規劃及安全建立 Git commit。當使用者要求查看 changed 或 staged files、整理變更、草擬或修正 commit message、決定拆分策略、暫存檔案、建立 commit、amend 或 revert 時使用。
---

# Git Commit Review

以繁體中文撰寫 review 與 commit message，程式碼註解維持英文。遵守目前 repository 的 `AGENTS.md` 與使用者明示指示；若衝突，以較具體且較高優先序的指示為準。

## 適用情況

- 使用者想寫、修改或選擇 commit message，或整理本次變更重點。
- 使用者想 review changed 或 staged files、了解改了什麼，或判斷要不要拆 commit。
- 使用者要求 Conventional Commits 格式、暫存指定檔案或實際建立 commit。

## 判斷意圖

- 只要求檢視、review、規劃或草擬訊息時，只讀取 Git 狀態與 diff，不修改檔案或 Git 狀態。
- 要求提交時，先提出明確提交計畫並等待使用者確認；確認後才暫存選定檔案並建立 commit；不要預設 `git add .`。
- 未獲明確要求時，不執行 `push`、不建立或切換分支、不使用 `--amend`、不重寫歷史。

## Review 與規劃

依固定順序讀取：

1. `git status --short`，確認新增、修改、刪除、rename 與 staged 狀態。
2. `git diff`，閱讀未暫存變更。
3. `git diff --staged`，閱讀已暫存變更。
4. `git log --oneline -n 10`，對齊專案既有的提交語氣。

逐檔摘要「改了什麼」及有證據支持的「為什麼改」，並清楚區分 staged 與 unstaged 檔案。不要從 diff 臆測無法證實的業務動機。

檢查是否混入密鑰、憑證、`.env`、建置產物或大型無關檔案；發現疑慮時停止並說明，不要自行提交。

判斷拆分策略：

- 同一 commit 必須能回答「要解決哪一件事」；若需要不同脈絡理解，建議拆分。
- 將功能、修正、文件、重構與純機械性修改分開。
- format、rename、lint fix 等機械性修改應和邏輯修改分開。
- 檔案必須共同編譯、執行或驗證時可維持同一 commit，但在訊息中說明關聯。

對於 review 或訊息草擬，使用以下輸出；變更意義明確時提供一個推薦版本，語意有合理分歧時再提供最多兩個備選：

```markdown
## 變更摘要
- <主要變更群組與目的>

## staged 與 unstaged 狀態
- staged: <檔案與重點>
- unstaged: <檔案與重點>

## 建議 commit 策略
- <單一 commit / 拆成 N 個 commit>
- 理由: <原因>

## Commit message 建議

### 推薦
`<type>(<scope>): <subject>`
- <必要時的 body 重點>

### 多 commit 時

#### Commit 1：`<type>(<scope>): <subject>`
- 納入檔案：`<file 1>`、`<file 2>`
- 建議 body：<動機、關鍵決策與影響範圍>

#### Commit 2：`<type>(<scope>): <subject>`
- 納入檔案：`<file 3>`
- 建議 body：<動機、關鍵決策與影響範圍>
```

## Commit 訊息

使用格式：

```text
<type>(<scope>): <subject>

<body>

<footer>
```

- type 僅可用：`feat`、`fix`、`docs`、`style`、`refactor`、`perf`、`test`、`chore`、`revert`、`build`、`ci`、`security`、`deps`、`release`、`hotfix`。
- `feat` 為新能力；`fix` 為錯誤修正；`refactor` 為不改行為的結構改善；`perf` 為效能改善；`test` 為測試；`docs` 為文件；`style` 為不影響執行的格式；`chore` 為一般維護。
- `build` 用於建置系統或工具鏈；`ci` 用於持續整合；`deps` 用於相依套件；`security` 用於安全性修補；`release` 用於版本釋出；`hotfix` 僅用於需緊急發佈的正式環境修補；`revert` 用於撤銷既有 commit。
- scope 視影響範圍選用；body 與 footer 可省略。subject 使用繁體中文、不超過 50 個字、不加句點，描述結果而非執行過程。
- body 聚焦動機、關鍵決策與影響範圍；多項內容可使用列點，簡單情況可用短句；每行不超過 72 個字。
- 有任務編號時放入 footer；不相容變更以 `BREAKING CHANGE:` 說明影響、原因與遷移方式；不要加入 `Co-Authored-By` 行。
- 不要揭露帳號、金鑰、內網位址或其他敏感資訊；沒有測試證據時，不要聲稱測試已通過。

範例：

```text
fix(auth): 修正 token 過期判斷的邊界條件

- 修正臨界時間被誤判為有效的問題
- 補上過期前緩衝以降低時間競態
```

```text
refactor(api): 抽出共用的請求驗證邏輯

- 集中重複的參數檢查以降低維護成本
- 保持既有行為，僅調整結構以利後續擴充
```

## 執行提交

1. 依變更風險執行最相關且可用的驗證；無法執行時如實回報原因。
2. 呈現提交計畫：預計納入的檔案、commit message 與驗證結果；即使使用者已直接要求提交，也必須等待明確確認。
3. 使用者確認後，僅暫存預定檔案並建立 commit，保留既有的無關修改與未追蹤檔。
4. 回報 commit hash、訊息、驗證結果與仍保留的工作區變更。

## 特殊情況

- amend：僅在使用者明確要求時使用；先確認目標 commit 是否可能已推送，已公開歷史要先提醒風險。
- revert：優先使用 `git revert` 建立可追溯的反向 commit；除非使用者明確要求，不用 reset 或強制推送。
- 衝突：先呈現衝突範圍與可行處理方式；不要臆測業務語意或覆蓋使用者修改。
