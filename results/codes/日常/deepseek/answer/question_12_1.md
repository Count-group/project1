以下是实现该功能的Python程序：

```python
from PIL import Image

def replace_color_with_transparency(input_path, output_path):
    # 打开图片并转换为RGBA模式（确保支持透明度）
    img = Image.open(input_path).convert("RGBA")
    pixels = img.load()  # 获取像素数据
    
    # 遍历每一个像素
    for x in range(img.width):
        for y in range(img.height):
            r, g, b, a = pixels[x, y]  # 获取当前像素的RGBA值
            
            # 检查RGB是否都在[220, 255]范围内
            if all(220 <= c <= 255 for c in (r, g, b)):
                # 将透明度设为0（完全透明）
                pixels[x, y] = (r, g, b, 0)
            else:
                # 保持原有颜色和不透明度（255为完全不透明）
                pixels[x, y] = (r, g, b, 255)
    
    # 保存为PNG格式（保留透明度）
    img.save(output_path, "PNG")
    print(f"处理完成，结果已保存至 {output_path}")

# 使用示例
input_image = "input.png"   # 输入图片路径
output_image = "output.png" # 输出图片路径
replace_color_with_transparency(input_image, output_image)
```

---

### 使用说明：
1. **安装依赖库**：
   ```bash
   pip install Pillow
   ```

2. **修改路径**：将代码中的 `input.png` 和 `output.png` 替换为实际文件路径。

3. **运行程序**：执行脚本后，满足条件的颜色将被替换为透明。

---

### 关键点解释：
1. **RGBA模式转换**：通过 `.convert("RGBA")` 确保图片有透明度通道。
2. **颜色范围判断**：使用 `all(220 <= c <= 255 for c in (r, g, b))` 检查颜色是否在浅灰色到白色范围内。
3. **透明度设置**：将符合条件的像素的Alpha值设为0，其他像素设为255以保留原有不透明度。
4. **输出格式**：必须保存为PNG等支持透明度的格式，JPG会丢失透明信息。

---

### 注意事项：
- 处理大图片时可能较慢，建议对分辨率过高的图片先进行缩放。
- 如果原图已有透明度，处理后会重置非目标区域的透明度为完全不透明（Alpha=255）。