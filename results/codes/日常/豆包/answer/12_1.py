from PIL import Image

def replace_color_with_transparency(image_path, output_path):
    try:
        # 打开图片
        image = Image.open(image_path)
        # 转换为 RGBA 模式
        image = image.convert("RGBA")
        width, height = image.size
        for x in range(width):
            for y in range(height):
                r, g, b, a = image.getpixel((x, y))
                # 检查 RGB 值是否在指定范围内
                if 220 <= r <= 255 and 220 <= g <= 255 and 220 <= b <= 255:
                    # 将该像素的透明度设置为 0
                    image.putpixel((x, y), (r, g, b, 0))
        # 保存修改后的图片
        image.save(output_path)
        print(f"图片处理完成，已保存到 {output_path}")
    except FileNotFoundError:
        print(f"错误：未找到文件 {image_path}")
    except Exception as e:
        print(f"发生未知错误：{e}")


if __name__ == "__main__":
    input_image_path = "input_image.png"
    output_image_path = "output_image.png"
    replace_color_with_transparency(input_image_path, output_image_path)