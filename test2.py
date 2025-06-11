



splits={"，","。","？","！",",",".","?","!","~",":","：","—","…",}#不考虑省略号
def split(todo_text):
    todo_text = todo_text.replace("……", "。").replace("——", "，")
    if todo_text[-1] not in splits:
        todo_text += "。"
    i_split_head = i_split_tail = 0
    len_text = len(todo_text)
    todo_texts = []
    while i_split_tail < len_text:
        if todo_text[i_split_tail] in splits:
            todo_texts.append(todo_text[i_split_head:i_split_tail + 1].strip())
            i_split_tail += 1
            i_split_head = i_split_tail
        else:
            i_split_tail += 1
    return todo_texts




text = "你好……，今天怎么样？——我很好。我们明天见！"

print(split(text))
