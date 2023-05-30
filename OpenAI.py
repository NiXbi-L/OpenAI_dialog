import openai

import cfg
openai.api_key = cfg.OpenAI_API  # замените на свой API-ключ


# создание диалога с помощью модели "davinci"
def generate_dialog(prompt, model, token_max_length):
    response = openai.Completion.create(
        engine=model,
        prompt="\n".join([f"Human: {prompt}", "AI:"]),
        max_tokens=token_max_length, #устанавливает максимальное количество токенов в ответе. Чем больше эта величина, тем длиннее ответ.
        n=1, #задает количество вариантов ответа, которые следует сгенерировать.
        stop=None, #определяет строку, которая остановит генерацию текста.
        temperature=0.7,
        #устанавливает параметр "температуры", который влияет на вероятность выбора каждого следующего слова.
        #Чем выше значение этого параметра, тем больше вероятность случайного выбора следующего слова.
    )

    answer = response.choices[0].text.strip()
    return answer
