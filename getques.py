import pandas as pd
import tkinter as tk
from tkinter import messagebox

# 加载 Excel 表格
df = pd.read_excel('questions.xlsx')

# 将 Excel 表格数据转换为一个列表，用于后面的展示和操作
ques = [list(row) for row in df.values]

# 创建窗口
root = tk.Tk()
root.title('答题系统，PowerdBy：赵子爽，李瑞晨，杨金旺，梁博，张春成')
root.geometry('1000x800')

# 创建题目展示标签和正误提示标签
topic_label = tk.Label(root, text='', font=("微软雅黑",20), wraplength=800)
# topic_label.grid(row=1, column=0)
topic_label.grid(row=0, column=0, sticky=tk.NSEW)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

topic_label.pack()

result_label = tk.Label(root, text='')
result_label.pack()

# 创建上一题按钮,下一题和提交按钮
prev_btn = tk.Button(root, text='上一题')
prev_btn.pack(side='right', padx=10)


next_btn = tk.Button(root, text='下一题')
next_btn.pack(side='right', padx=10)

submit_btn = tk.Button(root, text='提交')
submit_btn.pack(side='right', padx=10)

# option_vars = []
# option_btns = []
def set_choice(question_num):
    global option_vars, option_btns

    # 如果题目编号是 1，则创建单选框，否则创建复选框
    if question_num == 1:
        option_vars = []
        option_btns = []
        # 创建一组单选框
        option_var = tk.StringVar()
        for i in range(5):
            tk.Radiobutton(root, text=chr(ord('A') + i), variable=option_var, value=i, name=f'!radiobutton{i}', font=("微软雅黑", 12)).grid(row=i, column=0, padx=5, pady=5)
    else:
        option_vars = []
        option_btns = []
        # 创建一组复选框
        option_vars = []
        option_btns = []
        for i in range(5):
            option_vars.append(tk.BooleanVar())
            option_btns.append(tk.Checkbutton(root, text=chr(ord('A') + i), variable=option_vars[i], name=f'!checkbutton{i}', font=("微软雅黑", 12)))
            option_btns[i].grid(row=i, column=0, padx=5, pady=5)

# # 创建单选
# def singal():
#     # option_vars = []
#     # option_btns = []

#     for i in range(5):
#         option_vars.append(tk.BooleanVar())
#         option_btns.append(tk.Radiobutton(root, text=chr(ord('A') + i), variable=option_vars[i], value=i, name=f'!radiobutton{i}',font=("微软雅黑",20)))
#         option_btns[i].pack()
# def checkbox():
#     # option_vars = []
#     # option_btns = []

#     for i in range(5):
#         option_vars.append(tk.BooleanVar())
#         option_btns.append(tk.Checkbutton(root, text=chr(ord('A') + i), variable=option_vars[i], name=f'!checkbutton{i}',font=("微软雅黑",20)))
#         option_btns[i].pack()
# 创建选项按钮
# option_vars = []
# option_btns = []

# for i in range(5):
#     option_vars.append(tk.BooleanVar())
#     option_btns.append(tk.Checkbutton(root, text=chr(ord('A') + i), variable=option_vars[i], name=f'!checkbutton{i}',font=("微软雅黑",20)))
#     option_btns[i].pack()




# 当前所在的题号
current_idx = 0

# 显示第一道题
# 显示题目
def show_topic():
    global current_idx, prev_btn
    topic_label.config(text=f'第{ques[current_idx][0]}题：{ques[current_idx][1]}')
    set_choice(ques[current_idx][0])
    result_label.config(text='')
    for i in range(5):
        option_vars[i].set(False)
    for i in range(5):
        if ques[current_idx][i+2]:
            option_btn = root.nametowidget(f'!checkbutton{i}')
            option_btn.config(text=f'{chr(ord("A")+i)}. {ques[current_idx][i+2]}')
    if current_idx <= 0:
        prev_btn.config(state='disabled')
    else:
        prev_btn.config(state='normal')


# 点击上一题按钮
def prev_topic():
    global current_idx
    current_idx -= 1
    if current_idx < 0:
        messagebox.showinfo('提示', '已经是第一道题！',font=("微软雅黑",20),fg="red")
        current_idx = 0
    else:
        show_topic()



# 点击下一题按钮
def next_topic():
    global current_idx
    current_idx += 1
    if current_idx >= len(ques):
        messagebox.showinfo('提示', '已经是最后一道题！',font=("微软雅黑",20),fg="red")
        current_idx = len(ques) - 1
    else:
        show_topic()

def show_result():
    global current_idx
    selected = []
    for i in range(5):
        if option_vars[i].get():
            selected.append(chr(ord('A') + i))
    if not selected:
        result_label.config(text='您还没有选择答案！',font=("微软雅黑",20),fg="red")
        return
    correct = ques[current_idx][7]
    answer = ''.join(selected)
    if answer == correct:
        result_label.config(text='回答正确！',fg="green",font=("微软雅黑",20))
    else:
        result_label.config(text='回答错误！正确答案是：' + ' '.join(correct),fg="red",font=("微软雅黑",20))
        print(answer,correct)
    # 将选项按钮的状态重置
    for i in range(5):
        option_vars[i].set(False)

# def show_all_question():
#     for i in range (1,df.shape[0]):
#         print(ques[i][0])
#         print(ques[i][1])
#         for char in ques[i][7]:
#             if char == 'A':
#                 print(ques[i][2])
#             elif char == 'B':
#                 print(ques[i][3])
#             elif char == 'C':
#                 print(ques[i][4])
#             elif char == 'D':
#                 print(ques[i][5])
#             elif char == 'E':
#                 print(ques[i][6])
        



# 创建一个 Frame 框架
frame = tk.Frame(root)
# frame.grid(row=2, column=0)
# 使用 Text 组件来显示多行文本
output = tk.Text(frame, width=60, height=20, font=("微软雅黑", 12))

def show_all_question(output):
    for i in range (1,df.shape[0]):
        output.insert(tk.END,str(ques[i][0])+'\n')
        output.insert(tk.END,str(ques[i][1])+'\n')
        for char in ques[i][7]:
            if char == 'A':
                output.insert(tk.END,str(ques[i][2])+'\n')
            elif char == 'B':
                output.insert(tk.END,str(ques[i][3])+'\n')
            elif char == 'C':
                output.insert(tk.END,str(ques[i][4])+'\n')
            elif char == 'D':
                output.insert(tk.END,str(ques[i][5])+'\n')
            elif char == 'E':
                output.insert(tk.END,str(ques[i][6])+'\n')
            output.insert('\n')

# 在 Frame 中添加 Text 组件
output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 创建一个滚动条
scrollbar = tk.Scrollbar(frame, command=output.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 绑定文本和滚动条
output.config(yscrollcommand=scrollbar.set)

# 在 Frame 中添加滚动条
frame.pack(fill=tk.BOTH, expand=True)

# 在按钮单击时调用 show_all_question
# 使用 lambda 函数传递 Text 组件对象
btn = tk.Button(root, text="显示题库", command=lambda: show_all_question(output))
btn.pack()

next_btn.config(command=next_topic)
submit_btn.config(command=show_result)
prev_btn.config(command=prev_topic)
# show_btn.config(command=show_all_question)

root.mainloop()
