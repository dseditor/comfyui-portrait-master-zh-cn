# ComfyUI Portrait Master 繁體中文版

https://github.com/dseditor/comfyui-portrait-master-zh-tw/blob/main/screenshot/TCSD3.png


## 項目介紹 | Info

- 人物肖像提示詞生成模塊，優化肖像生成，選擇永遠比填空更適合人類！

- 優化 + 漢化 自 [ComfyUI Portrait Master](https://github.com/florestefano1975/comfyui-portrait-master.git)

- 版本：基於ZHO V2.2版本的Fork、繁體中文化及內容增補，並將說明繁體中文化，保留ZHO原作說明內容，其他說明待後續增補

- 版本說明：版本越高內容越多，但隨著提示詞逐漸增多，每項參數的最終效果可能會被削弱，因此並非版本越高越好用，請選擇適合自己的版本

## 參數說明 | Parameters

- 鏡頭類型：頭像、肩部以上肖像、半身像、全身像、臉部肖像
- 性別：女性、男性、男孩、女孩 (繁體中文版增加男孩女孩)
- 國籍_1：193個國家可選
- 國籍_2：193個國家可選
- 體型:瘦、正常、超重等4種 
- 姿勢：回眸、S曲線、高級時尚等18種 
- 眼睛顏色：琥珀色、藍色等8種 
- 面部表情：開心、傷心、生氣、驚訝、害怕等24種
- 臉型：橢圓形、圓形、梨形等12種
- 髮型：法式波波頭、卷髮波波頭、不對稱剪裁等20種
- 頭髮顏色：金色、栗色、灰白混合色等9種 
- 鬍子：山羊鬍、扎帕鬍等20種 
- 燈光類型：柔和環境光、日落餘暉、攝影棚燈光等32種 
- 燈光方向：上方、左側、右下方等10種 
- 起始提示詞：寫在開頭的提示詞
- 補充提示詞：寫在中間用於補充信息的提示詞
- 結束提示詞：寫在末尾的提示詞
- 提高照片真實感：可強化真實感 
- 負面提示詞：負面提示詞輸出 

## 繁體中文版追加參數說明 | Parameters

- 配件：60種以上頭部配件 
- 眼鏡：17種眼鏡類型 
- 耳環：16種耳環類型 
- 背景：20種背景類型 
- 上衣：100種上衣類型，內衣、禮服、制服等等，可輸入關鍵字查詢 

## 提示詞合成順序 | Prompt composition order
- 起始提示詞
- 鏡頭類型 + 鏡頭權重
- 國籍 + 性別 + 年齡
- 體型 
- 姿勢 
- 眼睛顏色 
- 面部表情 + 面部表情權重
- 臉型
- 髮型
- 頭髮顏色 
- 鬍子 
- 眼鏡
- 配件
- 頭髮蓬鬆度
- 補充提示詞
- 皮膚細節
- 皮膚毛孔
- 皮膚瑕疵
- 痘痘 
- 皺紋 
- 小麥色膚色 
- 酒窩
- 雀斑
- 痣
- 眼睛細節
- 虹膜細節
- 圓形虹膜
- 圓形瞳孔
- 面部對稱性
- 耳環
- 背景
- 上衣
- 燈光類型 + 燈光方向 
- 結束提示詞
- 提高照片真實感 

## 姿勢庫 | Model Pose Library

特別提醒：由於肖像大師的本質是提示詞，因此想要通過純提示詞實現姿勢的穩定生成需要大量抽卡才能實現，這是我測試抽卡了一下午精選的結果，所以建議配合 openpose 實現姿勢的精確控製，別為難自己！

![poselist_](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/assets/140084057/0eac37da-6aee-4591-9755-19e3b317724c)


## 自定義 | Customizations

可將需要自定義增加的內容寫到lists文件夾中對應的json文件裡（如髮型、表情等）

## 使用建議 | Practical advice

- 註意：隨著提示詞逐漸增多，每項參數的最終效果可能會被削弱，不建議滿鋪所有參數
  
- 皮膚和眼睛細節等參數過高時可能會覆蓋所選鏡頭的設置。在這種情況下，建議減小皮膚和眼睛的參數值，或者插入否定提示(closeup, close up, close-up:1.5)，並根據需要修改權重。

- 要實現完美的姿勢控製，請配合 ControlNet 使用，同時將鏡頭類型設置為空（-）

## 安裝 | Install

- 手動安裝：
    1. `cd custom_nodes`
    2. `git clone https://github.com/dseditor/comfyui-portrait-master-zh-tw`
    3. 重啟 ComfyUI

## 工作流 | Workflow

### V2.2工作流

- [V2.2 For SD1.5 or SDXL](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/blob/main/workflows/Portrait%20Master%20%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%E7%89%88%20V2.2%E3%80%90Zho%E3%80%91.json)

![Dingtalk_20231221171315](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/assets/140084057/f36c43f7-5381-470b-a5f5-8abed834e2e2)

### V2.0工作流

- [V2.0 For SD1.5 or SDXL](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/blob/main/workflows/Portrait%20Master%20%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%E7%89%88%20V2.0%E3%80%90Zho%E3%80%91.json)

![Dingtalk_20231218163927](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/assets/140084057/606e1ef4-429c-4f8d-99fb-0a19f2350d0e)

- [V2.0 For SDXL Turbo（non-commercial）](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/blob/main/workflows/Portrait%20Master%20%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%E7%89%88%20SDXL%20Turbo%20V2.0%E3%80%90Zho%E3%80%91.json)

![Dingtalk_20231218165449](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/assets/140084057/e0b188af-7d0a-47b8-8327-13dd630cea91)

- [V2.0 for SAG + SVD 視頻工作流](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/blob/main/workflows/Portrait%20Master%20%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%E7%89%88%20V2.0%20%2B%20SAG%20%2B%20SVD%E3%80%90Zho%E3%80%91.json)


https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/assets/140084057/8e3915be-2d45-4f94-af0c-0a270378712b

![Dingtalk_20231218185612](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/assets/140084057/e9316a7a-dbe5-4e20-bd50-1e622551c7ab)


### V1.0工作流

- [SD1.5 or SDXL](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/blob/main/workflows/Portrait%20Master%20%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%E7%89%88%E3%80%90Zho%E3%80%91.json)

![image](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/assets/140084057/e1269817-36e6-4f20-92f6-7119128b65d4)


- [SDXL Turbo（non-commercial）](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/blob/main/workflows/Portrait%20Master%20%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%E7%89%88%20SDXL%20Turbo%E3%80%90Zho%E3%80%91.json)

![image](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/assets/140084057/459162f0-a079-42af-990b-e916f32a0ff7)


## 更新日誌 | Changelog

20231221

- 更新為V2.2版，新增6項參數：
    - 體型（4種）
    - 姿勢（18種）
    - 鬍子（20種）
    - 痘痘
    - 皺紋
    - 小麥色膚色
 
- 已登陸 manager 不用手動安裝了

20231218

- 更新為V2.0版，新增6項參數，擴充2項參數，優化代碼：
    - 眼睛顏色（8種）
    - 頭髮顏色（9種）
    - 燈光類型（32種）
    - 燈光方向（10種）
    - 提高照片真實感
    - 負面提示詞
    - 鏡頭類型（+3種）
    - 髮型（+19種）

![Dingtalk_20231218164020](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/assets/140084057/38d305cb-64f3-4dcf-a389-5ad3f84be7b3)

20231216

- 完成代碼優化，將原本讀取txt文件調整成讀取json文件，更加方便使用、自定義和擴展
  ![image](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/assets/140084057/7b183c08-a95f-4464-9e51-979894cb2b60)

20231215

- 對 [ComfyUI Portrait Master](https://github.com/florestefano1975/comfyui-portrait-master.git) 完成漢化


## Stars 

[![Star History Chart](https://api.star-history.com/svg?repos=ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn&type=Date)](https://star-history.com/#ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn&Date)

<!---
[![Star History Chart](https://api.star-history.com/svg?repos=ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn&type=Timeline)](https://star-history.com/#ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn&Timeline)
--->


## 關於我 | About me

📬 **聯繫我**：
- 郵箱：zhozho3965@gmail.com
- QQ 群：839821928

🔗 **社交媒體**：
- 個人頁：[-Zho-](https://jike.city/zho)
- Bilibili：[我的B站主頁](https://space.bilibili.com/484366804)
- X（Twitter）：[我的Twitter](https://twitter.com/ZHOZHO672070)
- 小紅書：[我的小紅書主頁](https://www.xiaohongshu.com/user/profile/63f11530000000001001e0c8?xhsshare=CopyLink&appuid=63f11530000000001001e0c8&apptime=1690528872)

💡 **支持我**：
- B站：[B站充電](https://space.bilibili.com/484366804)
- 愛髮電：[為我充電](https://afdian.net/a/ZHOZHO)


## Credits

[ComfyUI Portrait Master](https://github.com/florestefano1975/comfyui-portrait-master.git)


