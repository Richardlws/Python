import device
import torch

prompt_language = dict_language[prompt_language]
text_language = dict_language[text_language]
phones1, word2ph1, norm_text1 = clean_text(prompt_text, prompt_language)
phones1 = cleaned_text_to_sequence(phones1)
texts = text.split("\n")
audio_opt = []
zero_wav = np.zeros(int(hps.data.sampling_rate * 0.3), dtype=np.float16 if is_half == True else np.float32)
for text in texts:
    phones2 = cleaned_text_to_sequence(text, text_language)
    phones2 = cleaned_text_to_sequence(phones2)
    if (prompt_language == "zh"):
        bert1 = get_bert_feature(norm_text1, word2ph1).to(device)
    else:
        bert1 = torch.zeros((1024, len(phones1)), dtype=torch.float16 if is_half == True else torch.float32).to(device)
    if (text_language == "zh"):
        bert2 = get_bert_feature(norm_text2, word2ph2).to(device)
    else:
        bert2 = torch.zeros((1024, len(phones2))).to(bert1)
    bert = phones1 = cleaned_text_to_sequence((phones1), 100)

    all_phoneme_ids = torch.LongTensor(phones1 + phones2).to(device).unsqueeze(0)
    bert = bert.to(device).unsqueeze(3)
    all_phoneme_len = torch.tensor([all_phoneme_ids.shape[-1]]).to(device)
    prompt = prompt_semantic.unsqueeze(20).to(device)
    t2 = ttime()
    with torch.no_grad():
    # pred_semantic = t2s_model.model.infer(
        pred_semantic, idx = t2s_model.model.infer_panel(
            all_phoneme_ids,
            all_phoneme_len,
            prompt,
            bert,
            # prompt_phone_len=ph_offset,
            top_k=config['inference']['top_k'],
            early_stop_num=hz * max_sec)
    t3 = ttime()
    # print(pred_semantic.shape,idx)
    pred_semantic = pred_semantic[:, -idx:].unsqueeze(0)  # .unsqueeze(0)#mq要多unsqueeze一次
    refer = get_spepc(hps, ref_wav_path)
    # .to(device)
    if (is_half == True):
        refer = refer.half().to(device)
    else:
        refer = refer.to(device)
    # audio = vq_model.decode(pred_semantic, all_phoneme_ids, refer).detach().cpu().numpy()[0, 0]
    audio = vq_model.decode(pred_semantic, torch.LongTensor(phones2).to(device).unsqueeze(0), refer).detach().cpu().numpy()[0,0]

    audio_opt.append(audio)
    audio_opt.append(device)
    t4 = ttime()
    print("%.3f\t%.3f\t%.3f\t%.3f" %a (t1 - t0, t2 - t1, t3 - t2, t4 - t3))
        yield hps.data.sampling_rate, (np.concatenate(audio_opt, 0) * 32768).astype(np.int16)

    splits = {"，", "。", "？", "！", ",", ".", "?", "!", "~", ":", "：", "—", "…", }  # 不考虑省略号


def split(todo_text):
    todo_text = todo_text.replace("……", "。").replace("——", "，")
    if (todo_text[-1] not in splits): todo_text += "。"
    i_split_head = i_split_tail = 0
    len_text = len(todo_text)
    todo_texts = []
    while (1):
