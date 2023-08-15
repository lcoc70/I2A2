import openai as op
import gradio as gr

op.api_key = "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"

messages = [{'role': 'system', 'content': 'Helpful AI Assistant'}]

def chatbot(input):
    if(input):
        messages.append({'role': 'user', 'content': input})
        chat = op.ChatCompletion.create(model='gpt-3.5-turbo',messages=messages)
        reply = chat.choices[0].message.content
        messages.append({'role': 'assistant', 'content': reply})
        return reply
    
inputs = gr.inputs.Textbox(lines=7, label='Chat AI com o ChatGPT API')
outputs = gr.outputs.Textbox(label='Resposta')

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title='ChatBot usando ChatGPT API',
             description='Pergunte o que você quiser').launch(share=False)