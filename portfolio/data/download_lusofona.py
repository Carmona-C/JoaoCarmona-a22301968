import requests
import json
import os

schoolYear = '202526'
course = 260  # LEI

base_path = "portfolio/data/lusofona"
os.makedirs(base_path, exist_ok=True)

print("Pasta destino:", base_path)

for language in ['PT', 'ENG']:
    print(f"\nA obter curso em {language}...")

    url = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'
    payload = {
        'language': language,
        'courseCode': course,
        'schoolYear': schoolYear
    }
    headers = {'content-type': 'application/json'}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=20)
        print("Status code curso:", response.status_code)
        response.raise_for_status()
        response_dict = response.json()
    except requests.exceptions.Timeout:
        print("Erro: pedido à API demorou demasiado tempo.")
        continue
    except requests.exceptions.RequestException as e:
        print("Erro no pedido do curso:", e)
        continue
    except Exception as e:
        print("Erro ao ler JSON do curso:", e)
        continue

    file_path = os.path.join(base_path, f"curso_{language}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(response_dict, f, indent=4, ensure_ascii=False)

    print("Criado:", file_path)

    if 'courseFlatPlan' not in response_dict:
        print("A chave 'courseFlatPlan' não existe.")
        print(response_dict)
        continue

    for uc in response_dict['courseFlatPlan']:
        uc_code = uc.get('curricularIUnitReadableCode')
        if not uc_code:
            print("UC sem código:", uc)
            continue

        print("A obter UC:", uc_code)

        url_uc = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails'
        payload_uc = {
            'language': language,
            'curricularIUnitReadableCode': uc_code,
        }

        try:
            response_uc = requests.post(url_uc, json=payload_uc, headers=headers, timeout=20)
            print("Status code UC:", response_uc.status_code)
            response_uc.raise_for_status()
            response_uc_dict = response_uc.json()
        except requests.exceptions.Timeout:
            print(f"Erro: timeout na UC {uc_code}")
            continue
        except requests.exceptions.RequestException as e:
            print(f"Erro no pedido da UC {uc_code}:", e)
            continue
        except Exception as e:
            print(f"Erro ao ler JSON da UC {uc_code}:", e)
            continue

        uc_file = os.path.join(base_path, f"{uc_code}-{language}.json")
        with open(uc_file, "w", encoding="utf-8") as f:
            json.dump(response_uc_dict, f, indent=4, ensure_ascii=False)

        print("Criado:", uc_file)

print("\nDownload concluído!")