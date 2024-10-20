import google.generativeai as genai
import os
from dotenv import load_dotenv

def get_car_ai_bio(model, brand, year):
    load_dotenv()
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f'''
        Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres. Fale coisas específicas desse modelo.
        Descreva especificações técnicas desse modelo de carro.
        ''')
    
    return response.text


#from openai import OpenAI
#
#
#client = OpenAI(
#    api_key='API_KEY'
#)
#
#
#def get_car_ai_bio(model, brand, year):
#    message = ''''
#    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
#    Descreva especificações técnicas desse modelo de carro.
#    '''
#    message = message.format(brand, model, year)
#    response = client.chat.completions.create(
#        messages=[
#            {
#                'role': 'user',
#                'content': message
#            }
#        ],
#        max_tokens=1000,
#        model='gpt-3.5-turbo',
#    )
#
#    return response.choices[0].message.content