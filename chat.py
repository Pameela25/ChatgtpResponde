import openai
# Indica el API Key
openai.api_key = ""
# Uso de ChapGPT en Python
model_engine = "text-davinci-003"
prompt = "la suma de 5 mas 5"
completion = openai.Completion.create(engine=model_engine,
                                    prompt=prompt,
                                    max_tokens=1024,
                                    n=1,
                                    stop=None,
                                    temperature=0.7)
respuesta=""
for choice in completion.choices:
    respuesta=respuesta+choice.text


# Imprime la respuesta en la consola
print("Respuesta generada:", respuesta)

# Guarda la respuesta en un archivo de texto
with open("texto.txt", "w") as f:
    f.write(respuesta)

print("Archivo 'texto.txt' creado correctamente.") 