# PORTRAIT MASTER
# Created by AI Wiz Art (Stefano Flore)
# Version: 2.2
# https://stefanoflore.it
# https://ai-wiz.art

# 漢化 + 優化為讀取json文件：Zho
# 版本：2.2

import json
import os

def read_json_file(file_path):
    try:
        # Open file, load JSON content into python dictionary, and return it.
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            return json_data
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def get_name(json_data):
    # Check that data is a list
    if not isinstance(json_data, list):
        print("Error: input data must be a list")
        return None

    names = []

    # Iterate over each item in the data list
    for item in json_data:
        # Check that the item is a dictionary
        if isinstance(item, dict):
            # Check that 'name' is a key in the dictionary
            if 'name' in item:
                # Append the value of 'name' to the names list
                names.append(item['name'])

    return names

def get_prompt(json_data, template_name):
    try:
        # Check if json_data is a list
        if not isinstance(json_data, list):
            raise ValueError("Invalid JSON data. Expected a list of templates.")
            
        for template in json_data:
            # Check if template contains 'name' and 'prompt' fields
            if 'name' not in template or 'prompt' not in template:
                raise ValueError("Invalid template. Missing 'name' or 'prompt' field.")
            
            if template['name'] == template_name:
                prompt = template.get('prompt', "")
                print("Extracted prompt:", prompt)
                return prompt

        # If function hasn't returned yet, no matching template was found
        raise ValueError(f"No template found with name '{template_name}'.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


class PortraitMaster_中文版:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        # Get current file's directory
        p = os.path.dirname(os.path.realpath(__file__))

        # Paths for various JSON files
        shot_file_path = os.path.join(p, 'lists/shot_list.json')
        gender_file_path = os.path.join(p, 'lists/gender_list.json')
        eyes_color_file_path = os.path.join(p, 'lists/eyes_color_list.json')
        face_shape_file_path = os.path.join(p, 'lists/face_shape_list.json')
        facial_expressions_file_path = os.path.join(p, 'lists/face_expression_list.json')
        nationality_file_path = os.path.join(p, 'lists/nationality_list.json')
        hair_style_file_path = os.path.join(p, 'lists/hair_style_list.json')
        hair_color_file_path = os.path.join(p, 'lists/hair_color_list.json')
        light_type_file_path = os.path.join(p, 'lists/light_type_list.json')
        light_direction_file_path = os.path.join(p, 'lists/light_direction_list.json')
        #v2.2
        body_type_file_path = os.path.join(p, 'lists/body_type_list.json')
        beard_file_path = os.path.join(p, 'lists/beard_list.json')
        model_pose_file_path = os.path.join(p, 'lists/model_pose_list.json')

        # Read JSON from file
        self.shot_data = read_json_file(shot_file_path)
        self.gender_data = read_json_file(gender_file_path)
        self.eyes_color_data = read_json_file(eyes_color_file_path)
        self.face_shape_data = read_json_file(face_shape_file_path)
        self.facial_expressions_data = read_json_file(facial_expressions_file_path)
        self.nationality_data = read_json_file(nationality_file_path)
        self.hair_style_data = read_json_file(hair_style_file_path)
        self.hair_color_data = read_json_file(hair_color_file_path)
        self.light_type_data = read_json_file(light_type_file_path)
        self.light_direction_data = read_json_file(light_direction_file_path)
        #V2.2
        self.body_type_data = read_json_file(body_type_file_path)
        self.beard_data = read_json_file(beard_file_path)
        self.model_pose_data = read_json_file(model_pose_file_path)

        # Retrieve name from JSON data
        shot_list = get_name(self.shot_data)
        shot_list = ['-'] + shot_list
        gender_list = get_name(self.gender_data)
        gender_list = ['-'] + gender_list
        eyes_color_list = get_name(self.eyes_color_data)
        eyes_color_list = ['-'] + eyes_color_list
        face_shape_list = get_name(self.face_shape_data)
        face_shape_list = ['-'] + face_shape_list
        facial_expressions_list = get_name(self.facial_expressions_data)
        facial_expressions_list = ['-'] + facial_expressions_list
        nationality_list = get_name(self.nationality_data)
        nationality_list = ['-'] + nationality_list
        hair_style_list = get_name(self.hair_style_data)
        hair_style_list = ['-'] + hair_style_list
        hair_color_list = get_name(self.hair_color_data)
        hair_color_list = ['-'] + hair_color_list
        light_type_list = get_name(self.light_type_data)
        light_type_list = ['-'] + light_type_list
        light_direction_list = get_name(self.light_direction_data)
        light_direction_list = ['-'] + light_direction_list
        #V2.2
        body_type_list = get_name(self.body_type_data)
        body_type_list = ['-'] + body_type_list
        beard_list = get_name(self.beard_data)
        beard_list = ['-'] + beard_list
        model_pose_list = get_name(self.model_pose_data)
        model_pose_list = ['-'] + model_pose_list
        
        
        max_float_value = 1.75

        return {
            "required": {
                "鏡頭類型": (shot_list, {
                    "default": shot_list[0],
                }),
                "鏡頭權重": ("FLOAT", {
                    "default": 1.5,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "性別": (gender_list, {
                    "default": gender_list[0],
                }),
                "年齡": ("INT", {
                    "default": 20,
                    "min": 18,
                    "max": 90,
                    "step": 1,
                    "display": "slider",
                }),
                "國籍_1": (nationality_list, {
                    "default": nationality_list[0],
                }),
                "國籍_2": (nationality_list, {
                    "default": nationality_list[0],
                }),
                "國籍混合": ("FLOAT", {
                    "default": 0.5,
                    "min": 0,
                    "max": 1,
                    "step": 0.05,
                    "display": "slider",
                }),
                "體型": (body_type_list, {
                    "default": body_type_list[0],
                }),
                "體型權重": ("FLOAT", {
                    "default": 0,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "姿勢": (model_pose_list, {
                    "default": model_pose_list[0],
                }),
                "眼睛顏色": (eyes_color_list, {
                    "default": eyes_color_list[0],
                }),
                "面部表情": (facial_expressions_list, {
                    "default": facial_expressions_list[0],
                }),
                "面部表情權重": ("FLOAT", {
                    "default": 1.5,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "臉型": (face_shape_list, {
                    "default": face_shape_list[0],
                }),
                "臉型權重": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "面部對稱性": ("FLOAT", {
                    "default": 0.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "髮型": (hair_style_list, {
                    "default": hair_style_list[0],
                }),
                "頭髮顏色": (hair_color_list, {
                    "default": hair_color_list[0],
                }),
                "頭髮蓬鬆度": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "胡子": (beard_list, {
                    "default": beard_list[0],
                }),
                "皮膚細節": ("FLOAT", {
                    "default": 0.5,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皮膚毛孔": ("FLOAT", {
                    "default": 0.3,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "酒窩": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皺紋": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "雀斑": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "痣": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皮膚瑕疵": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "痘痘": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "小麥色膚色": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "眼睛細節": ("FLOAT", {
                    "default": 1.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "虹膜細節": ("FLOAT", {
                    "default": 1.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "圓形虹膜": ("FLOAT", {
                    "default": 1.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "圓形瞳孔": ("FLOAT", {
                    "default": 1.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "燈光類型": (light_type_list, {
                    "default": light_type_list[0],
                }),
                "燈光方向": (light_direction_list, {
                    "default": light_direction_list[0],
                }),
                "燈光權重": ("FLOAT", {
                    "default": 1.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "提高照片真實感": (["enable", "disable"],),
                "起始提示詞": ("STRING", {
                    "multiline": True,
                    "default": "raw photo, (realistic:1.5)"
                }),
                "補充提示詞": ("STRING", {
                    "multiline": True,
                    "default": "(white background:1.5)"
                }),
                "結束提示詞": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "負面提示詞": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            }
        }

    RETURN_TYPES = ("STRING","STRING",)
    RETURN_NAMES = ("positive", "negative",)
    FUNCTION = "pm"
    CATEGORY = "📸肖像大師"

    def pm(self, 鏡頭類型="-", 鏡頭權重=1, 性別="-", 體型="-", 體型權重=0, 眼睛顏色="-", 面部表情="-", 面部表情權重=0, 臉型="-", 臉型權重=0, 國籍_1="-", 國籍_2="-", 國籍混合=0.5, 年齡=20, 髮型="-", 頭髮顏色="-", 頭髮蓬鬆度=0, 酒窩=0, 雀斑=0, 皮膚毛孔=0, 皮膚細節=0, 痣=0, 皮膚瑕疵=0, 皺紋=0, 小麥色膚色=0,  眼睛細節=1, 虹膜細節=1, 圓形虹膜=1, 圓形瞳孔=1, 面部對稱性=0, 補充提示詞="", 起始提示詞="", 結束提示詞="", 燈光類型="-", 燈光方向="-", 燈光權重=0, 負面提示詞="", 提高照片真實感="disable", 胡子="-", 姿勢="-", 痘痘=0):

        shot = get_prompt(self.shot_data, 鏡頭類型)
        gender = get_prompt(self.gender_data, 性別)
        eyes_color = get_prompt(self.eyes_color_data, 眼睛顏色)
        face_shape = get_prompt(self.face_shape_data, 臉型)
        facial_expressions = get_prompt(self.facial_expressions_data, 面部表情)
        nationality_1 = get_prompt(self.nationality_data, 國籍_1)
        nationality_2 = get_prompt(self.nationality_data, 國籍_2)
        hair_style = get_prompt(self.hair_style_data, 髮型)
        hair_color = get_prompt(self.hair_color_data, 頭髮顏色)
        light_type = get_prompt(self.light_type_data, 燈光類型)
        light_direction = get_prompt(self.light_direction_data, 燈光方向)
        #V2.2
        body_type = get_prompt(self.body_type_data, 體型)
        beard = get_prompt(self.beard_data, 胡子)
        model_pose = get_prompt(self.model_pose_data, 姿勢)

        prompt = []

        if 性別 == "-":
            性別 = ""
        else:
            性別 = " " + gender + " "

        if 國籍_1 != '-' and 國籍_2 != '-':
            Anationality = f"[{nationality_1}:{nationality_2}:{round(國籍混合, 2)}]"
        elif 國籍_1 != '-':
            Anationality = nationality_1 + " "
        elif 國籍_2 != '-':
            Anationality = nationality_2 + " "
        else:
            Anationality = ""

        if 起始提示詞 != "":
            prompt.append(f"{起始提示詞}")

        if 鏡頭類型 != "-" and 鏡頭權重 > 0:
            prompt.append(f"({shot}:{round(鏡頭權重, 2)})")

        prompt.append(f"({Anationality}{性別}{round(年齡)}-years-old:1.5)")

        if 體型 != "-" and 體型權重 > 0:
            prompt.append(f"({body_type}, {body_type} body:{round(體型權重, 2)})")

        if 姿勢 != "-":
            prompt.append(f"({model_pose}:1.5)")

        if 眼睛顏色 != "-":
            prompt.append(f"({eyes_color} eyes:1.25)")
        
        if 面部表情 != "-" and 面部表情權重 > 0:
            prompt.append(f"({facial_expressions}, {facial_expressions} expression:{round(面部表情權重, 2)})")

        if 臉型 != "-" and 臉型權重 > 0:
            prompt.append(f"({face_shape} shape face:{round(臉型權重, 2)})")

        if 髮型 != "-":
            prompt.append(f"({hair_style} hairstyle:1.25)")

        if 頭髮顏色 != "-":
            prompt.append(f"({hair_color} hair:1.25)")

        if 胡子 != "-":
            prompt.append(f"({beard}:1.15)")
        
        if 頭髮蓬鬆度 != "-":
            prompt.append(f"(disheveled:{round(頭髮蓬鬆度, 2)})")

        if 補充提示詞 != "":
            prompt.append(f"{補充提示詞}")

        if 皮膚細節 > 0:
            prompt.append(f"(skin details, skin texture:{round(皮膚細節, 2)})")

        if 皮膚毛孔 > 0:
            prompt.append(f"(skin pores:{round(皮膚毛孔, 2)})")

        if 皮膚瑕疵 > 0:
            prompt.append(f"(skin imperfections:{round(皮膚瑕疵, 2)})")

        if 痘痘 > 0:
            prompt.append(f"(acne, skin with acne:{round(痘痘, 2)})")

        if 皺紋 > 0:
            prompt.append(f"(skin imperfections:{round(皺紋, 2)})")

        if 小麥色膚色 > 0:
            prompt.append(f"(tanned skin:{round(小麥色膚色, 2)})")

        if 酒窩 > 0:
            prompt.append(f"(dimples:{round(酒窩, 2)})")

        if 雀斑 > 0:
            prompt.append(f"(freckles:{round(雀斑, 2)})")

        if 痣 > 0:
            prompt.append(f"(skin pores:{round(痣, 2)})")

        if 眼睛細節 > 0:
            prompt.append(f"(eyes details:{round(眼睛細節, 2)})")

        if 虹膜細節 > 0:
            prompt.append(f"(iris details:{round(虹膜細節, 2)})")

        if 圓形虹膜 > 0:
            prompt.append(f"(circular iris:{round(圓形虹膜, 2)})")

        if 圓形瞳孔 > 0:
            prompt.append(f"(circular pupil:{round(圓形瞳孔, 2)})")

        if 面部對稱性 > 0:
            prompt.append(f"(facial asymmetry, face asymmetry:{round(面部對稱性, 2)})")

        if 燈光類型 != '-' and 燈光權重 > 0:
            if 燈光方向 != '-':
                prompt.append(f"({light_type} {light_direction}:{round(燈光權重, 2)})")
            else:
                prompt.append(f"({light_type}:{round(燈光權重, 2)})")
        
        if 結束提示詞 != "":
            prompt.append(f"{結束提示詞}")

        prompt = ", ".join(prompt)
        prompt = prompt.lower()

        if 提高照片真實感 == "enable":
            prompt = prompt + ", (detailed, professional photo, perfect exposition:1.25), (film grain:1.5)"

        if 提高照片真實感 == "enable":
            negative_prompt = 負面提示詞 + ", (shinny skin, reflections on the skin, skin reflections:1.5)"
        else:
            negative_prompt = 負面提示詞

        
        print("Portrait Master as generate the prompt:")
        print(prompt)

        return (prompt,negative_prompt,)



NODE_CLASS_MAPPINGS = {
    "PortraitMaster_中文版": PortraitMaster_中文版
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PortraitMaster_中文版": "📸 肖像大師_中文版_2.2"
}
