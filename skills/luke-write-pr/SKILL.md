---
name: luke-write-pr
description: 依 PR 相對 base branch（target branch）的淨變更，以繁體中文撰寫或改善 PR 的標題與說明。當使用者要求撰寫 PR、整理 PR 描述、確認合適的 base branch、將 branch 變更歸納為 review guide，或改寫既有 PR 草稿時使用。只產出草稿文字；不建立 commit、不 push、不開 PR，也不更新既有 PR。
---

# PR 說明撰寫

撰寫讓 reviewer 能快速理解與判斷的 PR 說明。預設只產出標題與 Markdown 草稿；除非使用者明確要求，請勿建立、更新或送出 PR。

## 先確認事實範圍

1. 確認 target branch 與目前 head；若無法從 Git 關係或使用者需求判斷，先詢問。
2. 以 `git diff <target>...HEAD` 為準，辨識 PR 的淨變更；不可只根據最新 commit、近期對話或功能摘要撰寫。
3. 盤點並區分：
   - 功能背景與核心設計
   - 重要程式與契約變更
   - dependency、config、migration 等會影響安裝、部署或相容性的變更
   - 已實際執行的驗證與其結果
   - 需要 reviewer 優先判斷的設計或風險

不要把 commit 數、開發過程或已撤回的嘗試當成 PR 內容；它們通常不幫助 reviewer 判斷目前的淨結果。

## Template 優先

先檢查目標 repo 是否有 PR template，例如 `.github/pull_request_template.md`。若存在，保留其區段與必要欄位，並依 template 內的註解填寫；不得為了套用本 skill 而覆蓋 repo 已有的團隊格式。

若 repo 沒有 template，讀取並使用 [PR 範本](references/pr_template.md)。範本的 HTML 註解只用來協助撰寫，不要保留在交付給使用者的 PR 草稿中。

## 交付格式

每次都先交付一行 PR title，再提供 PR body。title 要概括最主要的使用者或系統價值，不可只是 branch 名稱或逐條描述實作。

若 repo 有既有 title 慣例，沿用該慣例；否則使用簡潔的 `<type>(<scope>): <摘要>` 格式，例如：`feat(chart-gen-agent): 新增圖表生成子代理`。

## 語言與文風

- 使用自然、專業的台灣繁體中文，讓工程師能直接理解；不要逐字翻譯英文，也不要為了顯得正式而堆疊抽象名詞。
- 優先寫清楚「誰做什麼、為什麼」，例如「程式會依資料形狀判斷」；避免「由程式碼依資料形狀進行驗證」這類冗長被動句。
- 採用台灣常用詞，如「支援」、「設定」、「資料」；避免「支持」、「配置」、「數據」等非台灣技術文件慣用詞。
- 避免沒有具體意義的 AI 常見用語，例如「賦能」、「落地」、「閉環」或「提升效能」；必須明確說明實際改變的行為或結果。
- 程式模組、識別字與 CS 概念維持英文，不硬翻成中文，例如 `subagent`、`subgraph`、`node`、`state`、`reducer`、`config`、`semantic_type`、`Chart.js` 與 `structured output`。

## 內容邊界

- 不加入 follow-ups、TODO、未來構想或已決定不在本 PR 處理的事項。
- 不將歷史測試紀錄寫成這次已驗證；若需要引用，只能清楚標示為既有紀錄。
- 不使用本機絕對路徑、敏感資訊或內部帳密。
- 不為了完整而逐條翻譯 commits；以 reviewer 需要的決策資訊為準。
- 使用者要求改寫既有 PR 時，僅交付可供貼回的標題與內容草稿；若要實際更新遠端 PR，先取得明確外部寫入授權。
