import re

def lexical_analyzer(code):
    reserved_words = {'if', 'else', 'while', 'for', 'return', 'int', 'float', 'print', 'def', 'class'}
    math_operators = r'[+\-*/%=<>!]=?'
    symbols = r'[()\[\]{};,.]'
    variables = r'[a-zA-Z_][a-zA-Z0-9_]*'
    numbers = r'\d+(\.\d+)?'

    master_pattern = re.compile(
        f'(?P<MATH>{math_operators})|'
        f'(?P<SYMBOL>{symbols})|'
        f'(?P<VAR>{variables})|'
        f'(?P<NUM>{numbers})'
    )

    results = {
        "Reserve Words": [],
        "Simbol & Tanda Baca": [],
        "Variabel": [],
        "Kalimat Matematika (Operator/Angka)": []
    }

    for match in master_pattern.finditer(code):
        token_type = match.lastgroup
        value = match.group()

        if token_type == 'VAR':
            if value in reserved_words:
                results["Reserve Words"].append(value)
            else:
                results["Variabel"].append(value)
        elif token_type == 'SYMBOL':
            results["Simbol & Tanda Baca"].append(value)
        elif token_type == 'MATH' or token_type == 'NUM':
            results["Kalimat Matematika (Operator/Angka)"].append(value)

    return results

print("--- TOKEN ANALYZER ---")
print("Ketik kode kamu lalu tekan Enter. Ketik 'exit' untuk berhenti.")

while True:
    input_user = input("\nInput Kode: ")
    
    if input_user.lower() == 'exit':
        print("Program selesai. Sampai jumpa!")
        break
        
    if not input_user.strip():
        continue

    hasil = lexical_analyzer(input_user)
    
    print("HASIL ANALISIS")
    for kategori, token_list in hasil.items():
        unique_tokens = list(dict.fromkeys(token_list)) 
        print(f"{kategori:35}: {', '.join(unique_tokens) if unique_tokens else '-'}")
