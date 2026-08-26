---
name: luke-openspec-use-tdd
description: 以規劃 commit 與 TDD 實作 OpenSpec change。當 proposal 完成後準備實作、開始或繼續 apply change、要求以 Red-Green-Refactor 完成 spec-driven 工作，或一路完成 OpenSpec change 時使用；不適用於純探索、只做 code review 或只封存 change。
---

# OpenSpec TDD

讓 OpenSpec 的規劃、實作與封存在 Git 歷史中保持可獨立 review，並以可觀察的 Red → Green → Refactor 證據完成每項行為。

## 先讀專案規則

開始前讀取目前 repo 與工作目錄適用的 agent instructions（例如 `AGENTS.md`、`CLAUDE.md`）、OpenSpec 指引及測試文件。以專案指定的命令、commit 規範與 change lifecycle 為準；不要假設固定語言、目錄或測試框架。

檢查 `git status`，保留使用者既有變更。只 stage 當前 change 的相關檔案，不把無關修改混入任何 commit。

## 固定節奏

### 1. 規劃先獨立 commit

建立或更新 proposal、design、specs 與 tasks 後：

1. 依 repo 規範驗證 OpenSpec artifacts。
2. 確認 artifacts 能描述可驗證的行為，且 `tasks.md` 將測試或 Red 證據安排在對應實作之前。
3. 在修改 production code 前，先提交規劃檔；優先使用 `docs(openspec): ...`，但若 repo 有更具體規範則遵從 repo。
4. 若規劃早已提交，先確認其 commit 存在再繼續，不重複建立空 commit。

當使用者要求 propose 後接續實作或一路做到完成時，規劃 commit 是流程的一部分，不得因連續執行、長時間任務或時間壓力省略。

### 2. 每個行為執行 TDD

對每一個待實作行為分別完成：

1. **Red**：先寫能表達缺少行為的最小測試。
2. 執行最聚焦的測試並確認它因預期原因失敗，保留命令與關鍵失敗結果作為證據。
3. 如果新測試一開始就通過，不得宣稱取得 Red；確認是否測錯、斷言不足，或行為其實已存在，並據此修正測試或重新評估 task。
4. **Green**：只寫讓目前測試通過所需的最小 production code，再執行聚焦測試。
5. **Refactor**：在測試保持綠燈下改善結構，避免順手擴張 scope。
6. 執行受影響範圍的回歸測試，再處理下一個行為。

即使 `tasks.md` 把「實作」與「測試」分成不同 group，也必須按行為交錯執行 Red → Green，不得先做完整個實作 group 再補測試。

## 找出正確測試命令

依序查找適用的 agent instructions、package scripts、Makefile、`pyproject.toml`、CI 設定與既有測試文件。優先使用 repo 已規定的入口；不要把某個專案的命令複製到其他專案。

若行為無法以一般單元測試覆蓋，先尋找 contract test、fake、mock、fixture 或 dependency injection。只有平台邊界必須由真實 runtime 驗證時，才增加 integration 或 end-to-end 測試，並在 change 內記錄限制。

## 技術棧中立

此 skill 只規範 OpenSpec 與 TDD 的節奏，不規定語言、框架、測試工具或部署平台。它必須能套用於前端、後端、monorepo、TypeScript、Node.js、Python、Java、GAS 與其他技術棧。

- 依 repo 現況選用既有的 Jest、Vitest、Node test runner、pytest、JUnit、Maven、Gradle 或其他測試入口；這些只是可能選項，不得預設任一工具必然存在。
- 先執行與目前行為最接近的最小測試，再依風險擴大到 package、module、service、integration 或完整 suite。
- 尊重 repo 對 working directory、環境變數、容器、fixture、資料庫與外部服務的既有規則。
- 語言或平台特有的測試、部署與安全限制屬於該 repo 的 agent instructions、runbook 或 repo-scoped skill，不寫進這個 global skill。

## 證據與 commit

完成每個 task 後才更新 checkbox，並在 `tasks.md` 或 repo 指定位置記錄：

- Red 的測試命令與預期失敗原因。
- Green／回歸的測試命令與通過結果。
- 無法本機測試的限制，以及採用的 contract、integration、run ID 或其他證據。

實作與測試完成後建立獨立的 `feat`、`fix` 或 `test` commit；不要 amend 規劃 commit 來隱藏開發過程。

若使用者要求一路完成並封存，先確認所有 tasks、測試及 OpenSpec validation 完成，再依 repo 的 archive 程序封存，最後建立獨立的 `docs(openspec): ...` archive commit。

## 不得虛構 TDD

- 沒有實際執行並觀察失敗，就不能把測試記為 Red。
- test-after 不能回報成 TDD；若因既有實作或外部限制只能 test-after，明確揭露。
- 測試失敗若來自環境、語法或 fixture 損壞，而不是缺少的行為，不算有效 Red。
- 不得為了取得紅燈而破壞 production code。
