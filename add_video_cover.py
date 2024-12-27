import datetime
import os
from PIL import Image, ImageDraw, ImageFont

import subprocess



'''
在视频的第一帧增加一个封面,封面截取视频中某一个帧
在图片上加上标题,并生成一张封面图片的新视频,发布时使用这个新视频
'''

# 使用合适的中文字体，例如微软雅黑或黑体
font_path = r'msyhbd.ttc'

def get_video_duration(input_video_path):
    command = [
        'ffprobe',
        '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        input_video_path
    ]

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,encoding='utf-8')

    if result.returncode != 0:
        raise ValueError(f"ffprobe 停止工作，错误信息：{result.stderr}")

    return float(result.stdout.strip())




# 在视频中截取图片,制作封面图片
def create_thumbnail(input_video_path, output_thumbnail_path, time='00:03:00', title_text='经典动画'):
    """
    从视频中提取封面图并添加标题文字
    :param input_video_path: 输入视频文件路径
    :param output_thumbnail_path: 输出封面图片文件路径
    :param time: 提取封面的时间，格式为 "HH:MM:SS" 或 "秒数"
    :param title_text: 中心标题文字
    """
    # 提取视频的指定帧
    command = [
        'ffmpeg',
        '-i', input_video_path,
        '-ss', str(time),  # 提取时间
        '-vframes', '1',   # 只提取一帧
        output_thumbnail_path
    ]
    print("执行提取指定帧命令:", command)  # 调试打印
    subprocess.run(command, check=True, encoding='utf-8')

    # 创建新的输出文件名，添加 "_1" 后缀
    base, ext = os.path.splitext(output_thumbnail_path)
    new_output_thumbnail_path = f"{base}_1{ext}"

    print('图片地址',output_thumbnail_path)
    # 读取图片，获取尺寸
    with Image.open(output_thumbnail_path) as img:
        width, height = img.size

        # 创建字体对象，设置字体大小
        fontsize = int(height / 8)  # 根据高度设置字体大小
        font = ImageFont.truetype(font_path, fontsize)  # 创建字体对象

        # 创建绘图对象
        draw = ImageDraw.Draw(img)

        # 计算文字的宽度和高度，使用 textbbox 方法来获取文本的边界框
        text_bbox = draw.textbbox((0, 0), title_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]  # 计算宽度
        text_height = text_bbox[3] - text_bbox[1]  # 计算高度
        # 计算居中位置
        x = (width - text_width) / 2  # 文字在宽度中央
        y = (height - text_height) * 0.5  # 文字在高度的80%处

    # 在提取的封面图上添加标题文字
    overlay_command = [
        'ffmpeg',
        '-i', output_thumbnail_path, # 输入图片地址
         '-vf', (
            f"drawtext=text='{title_text}':"  
            f"fontfile='{font_path}':"  
            f"fontcolor=yellow:fontsize={fontsize}:x={x}:y={y}:"
            f"box=1:"  # 启用填充框  
            f"boxcolor=black@0.1:"  # 设置填充框颜色为半透明黑色  
            f"borderw=2:"  # 设置边框宽度  
            f"bordercolor=black"  # 设置边框颜色为黑色
        ),
        '-y',  # 强制覆盖输出文件
        new_output_thumbnail_path  # 输出到新的文件
    ]
    print("执行缩略图叠加文本命令:", overlay_command)  # 调试打印
    # 执行 FFmpeg 命令
    try:
        result = subprocess.run(overlay_command, check=True, encoding='utf-8', stderr=subprocess.PIPE)
        print("FFmpeg 输出:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"处理视频时发生错误: {e.stderr}")
        return  # 返回以避免后续删除文件

    # 删除源文件
    os.remove(output_thumbnail_path)
    print(f"已删除源文件: {output_thumbnail_path}")
    return new_output_thumbnail_path


def add_image_as_first_frame_fast(input_video_path, image_path, output_video_path):


    """将图片覆盖到视频的第一帧，但后续帧正常播放"""
    try:
        # 获取视频的宽度和高度
        ffprobe_cmd = [
            "ffprobe", "-v", "error", "-select_streams", "v:0",
            "-show_entries", "stream=width,height", "-of", "csv=s=x:p=0",
            input_video_path
        ]
        result = subprocess.run(ffprobe_cmd, capture_output=True, text=True, check=True)
        width, height = map(int, result.stdout.strip().split('x'))

        # 使用 overlay 滤镜，仅在第一帧生效
        ffmpeg_cmd = [
            "ffmpeg",  "-y",  "-i", input_video_path,                    # 输入视频
            "-i", image_path,                                   # 输入图片
            "-filter_complex", (
                f"[1:v]scale={width}:{height}[img];"            # 调整图片大小  
                f"[0:v][img]overlay=0:0:enable='lte(t,1)'[v]"   # 仅在第一帧叠加图片
            ),
            "-map", "[v]",                                      # 映射处理后的视频流
            "-map", "0:a?",                                     # 映射音频流（如果有音频）
            "-c:v", "libx264",                                  # 使用 H.264 编码
            "-crf", "23",                                       # 控制质量
            "-preset", "fast",                                  # 设置编码速度
            "-c:a", "copy",                                     # 原样保留音频
            output_video_path
        ]

        # 执行 FFmpeg 命令
        subprocess.run(ffmpeg_cmd, check=True, encoding='utf-8')
        print("图片已成功添加到视频的第一帧")

    except subprocess.CalledProcessError as e:
        print(f"FFmpeg 错误: {e.stderr}")
    except Exception as e:
        print(f"发生错误: {e}")




def start(video_path,title):
    print("视频处理开始！", datetime.datetime.now())

    title_text = title  # 中心标题文字


    # 输出视频路径，带时间戳
    out_name = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')  # 格式化时间戳


    # 封面地址
    thumbnail_jpg = f'./{out_name}.jpg'
    try:

        thumbnail_output = thumbnail_jpg  # 输出封面图路径

        # 创建封面图并添加中心标题
        cover_img = create_thumbnail(video_path, thumbnail_output, '00:00:03', title_text)  # 提取第3秒钟的帧作为封面

        print("封面图已保存：", cover_img)

        # 创建一个新的视频, 将封面图作为第一帧
        base, ext = os.path.splitext(video_path)
        watermarked_output_new = f"{base}_1{ext}"

        add_image_as_first_frame_fast(video_path, cover_img, watermarked_output_new)

        # 删除水印输出文件

        print("视频处理完成！", watermarked_output_new)
        print("视频处理完成！", datetime.datetime.now())


        return watermarked_output_new
    except subprocess.CalledProcessError as e:
        print(f"处理视频时出现错误: {e}")
    except ValueError as ve:
        print(ve)
    return None

# 示例使用
if __name__ == "__main__":
    path=r'G:\BaiduNetdiskDownload\动物王国大冒险（抖音主播同款）\S.少儿英语小故事\少儿英语小故事A Lazy Boy Who Became a Cow - 1.A Lazy Boy Who Became a Cow - What are(Av65788949,P1).mp4'
    start(path,'少儿英语故事1')

    #auto_release_kuaishou(video_path='J:\\202410视频剪辑\\猫和老鼠\\python\\37_20241222_171333_1.mp4',cover_image_path='J:\\202410视频剪辑\\猫和老鼠\\python\\37_20241222_171333_1.jpg',title='狗和耗子')