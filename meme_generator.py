from PIL import Image, ImageDraw, ImageFont

def create_meme():
    # 顯示模板選單
    print("可用的梗圖模板：")
    print("1. Distracted Boyfriend")
    print("2. Success Kid")
    
    # 選擇模板
    choice = input("請選擇模板 (輸入編號)：")
    template_path = f"templates/{choice}.jpg"
    
    try:
        # 載入圖片
        image = Image.open(template_path)
    except FileNotFoundError:
        print("模板不存在，請確認 templates 資料夾中的檔案！")
        return
    
    # 獲取用戶輸入的文字
    top_text = input("輸入頂部文字：")
    bottom_text = input("輸入底部文字：")
    
    # 創建繪圖對象
    draw = ImageDraw.Draw(image)
    
    # 載入字體（使用系統預設字體或下載一個 .ttf 字體）
    try:
        font = ImageFont.truetype("arial.ttf", 40)  # 可替換為其他字體檔案
    except:
        font = ImageFont.load_default()  # 若無字體檔案，使用預設字體
    
    # 計算圖片寬度
    img_width = image.width
    
    # 添加頂部文字（白色文字，黑邊框）
    top_bbox = draw.textbbox((0, 0), top_text, font=font)
    top_text_width = top_bbox[2] - top_bbox[0]
    top_x = (img_width - top_text_width) // 2
    draw.text((top_x-2, 10-2), top_text, font=font, fill="black")  # 黑邊框
    draw.text((top_x+2, 10+2), top_text, font=font, fill="black")
    draw.text((top_x, 10), top_text, font=font, fill="white")      # 白色文字
    
    # 添加底部文字
    bottom_bbox = draw.textbbox((0, 0), bottom_text, font=font)
    bottom_text_width = bottom_bbox[2] - bottom_bbox[0]
    bottom_x = (img_width - bottom_text_width) // 2
    bottom_y = image.height - bottom_bbox[3] - 10
    draw.text((bottom_x-2, bottom_y-2), bottom_text, font=font, fill="black")
    draw.text((bottom_x+2, bottom_y+2), bottom_text, font=font, fill="black")
    draw.text((bottom_x, bottom_y), bottom_text, font=font, fill="white")
    
    # 保存生成的梗圖
    image.save("meme.jpg")
    print("梗圖已生成，保存為 meme.jpg！")

if __name__ == "__main__":
    create_meme()