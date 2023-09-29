# -*- coding: utf-8 -*-
# 将每个目录下文件拆为
# 不需要指定目录了，只需调整为处理本目录的，即将文件会放在 /source,  或 /source_ent
# zh_CN_done.po
# zh_CN_todo.po
# 如果 本 模块目录下已有 _done文件，则无需再处理。 如果没有，则进行全流程。 全流程如下
# 如果有 todo条目 则拆，如果无则只加_done文件。


# -*- coding: utf-8 -*-

import polib
import os

# 指定目录
dir_path = os.path.dirname(os.path.realpath(__file__))

directory_list = os.listdir(dir_path)

# 循环遍历文件列表
for directory_name in directory_list:
    # 获取文件或目录的绝对路径
    abs_path = os.path.join(dir_path, directory_name, 'i18n')
    # 判断是否为文件
    if os.path.isfile(abs_path):
        print(directory_name)
    # 判断是否为目录
    elif os.path.isdir(abs_path):
        print('模块:', directory_name)
        # 如果是目录，则继续往下遍历
        sub_file_list = os.listdir(abs_path)
        for sub_file_name in sub_file_list:
            sub_abs_path = os.path.join(abs_path, sub_file_name)
            if os.path.isfile(sub_abs_path):
                original_po = polib.pofile(sub_abs_path)
                translated_po_path = os.path.join(abs_path, 'zh_CN_done.po')
                untranslated_po_path = os.path.join(abs_path, 'zh_CN_todo.po')

                translated_po = polib.POFile()
                translated_po.metadata = original_po.metadata
                translated_po.header = original_po.header
                untranslated_po = polib.POFile()
                untranslated_po.header = original_po.header
                untranslated_po.metadata = original_po.metadata

                for entry in original_po:
                    if (entry.msgid == entry.msgstr and len(entry.msgstr) > 30) or not entry.translated():
                        untranslated_po.append(entry)
                    else:
                        translated_po.append(entry)

                if len(translated_po) > 0:
                    translated_po.save(translated_po_path)
                if len(untranslated_po) > 0:
                    untranslated_po.save(untranslated_po_path)
