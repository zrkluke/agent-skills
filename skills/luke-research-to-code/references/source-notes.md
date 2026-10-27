# 來源與改寫界線

整理／審閱日期：2026-10-27。這是依來源自行撰寫的跨專案技能，不是 Dex 或 HumanLayer 發布的官方技能。

## 文章版本

[〈我錯了，還是要讀程式碼：Dex Horthy 重新檢討 AI 寫程式流程〉](https://blog.aihao.tw/2026/06/01/dexter-rpi-crispy/)，2026-06-01。

本文轉述的八階段為：提問、研究、設計、結構大綱、計畫、Worktree、實作、PR。CRISPY 是流程名稱，不要自行替每個字母編造固定含義。

本技能保留的原則：需求先轉為現況問題、研究使用另一份上下文、短設計與短大綱供人修正方向、垂直切分、實際閱讀程式碼、分階段處理指令及將重要脈絡寫入文件。

約 200 行設計、兩頁大綱、每階段少於 40 條指令及上下文百分比，是文章所述的經驗參考，不當作各模型通用的硬性界線。文末 2FA 案例明示為作者補充，不是 Dex 原話。

文章連到[原演講影片](https://www.youtube.com/watch?v=YwZR6tc7qYg)。本次讀取的是文章及下列官方文件，未取得可逐句核對的原演講逐字稿。

## 官方補充與版本差異

- [How workflow phases fit together](https://docs.humanlayer.com/explanation/workflow-phases)：用於核對研究／設計的分工、可驗證增量及人掌握重要決定的原則。
- [Skills and workflows reference](https://docs.humanlayer.com/reference/skills-workflows)：用於核對各階段產物。查閱時的現行 RPI 預設由大綱直接進入實作；詳細計畫仍可用，但被列為較早版本的路徑。本技能依使用者指定文章，保留第 5 階段，不把現行簡化版冒充該次演講。
- [Run a workflow in HumanLayer](https://docs.humanlayer.com/guide/skills-workflows)：補充依任務大小選路徑、保存交接決定與既有工作區的使用方式。
- [Workspace setup](https://docs.humanlayer.com/guide/workspaces)：補充來源版本、實際工作區與準備程序的核對。沒有照抄 HumanLayer 專用命令或設定檔。

## 為可執行技能補上的規則

規劃／接續模式、建議檔名、授權邊界、隔離能力不足時的揭露，以及沿用專案驗證方式，是為執行補上的約定，不能稱為原演講逐項明定。進度直接寫入既有大綱／計畫；沒有新增獨立進度表、測試套數、逐步確認或分支清理流程。

技能沒有附自動編排程式。階段切換與研究輸入分隔要由實際代理工具或執行平台實現；技能本身不能證明它們一定被強制執行。
