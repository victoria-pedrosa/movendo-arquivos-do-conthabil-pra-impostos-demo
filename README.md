# Demonstração — Limpeza de arquivos temporários nas pastas de impostos

> Projeto de portfólio de **Victória Pedrosa**. **Demonstração** de limpeza de arquivos temporários nas pastas de impostos — versão com dados fictícios (nomes, CNPJs, e-mails e IDs internos substituídos).

## Problema de negócio
Arquivos temporários (XML/CSV) acumulavam nas pastas de impostos.

## Antes x depois
| | Antes | Depois |
|---|---|---|
| Como é feito | Limpeza manual das pastas. | Script localiza e remove os arquivos listados, com modo simulação por padrão. |

## Ganho
- Pastas limpas com segurança.

## Tecnologias
Python, SQLite

## Arquivos
- `apagarxmlcsv_1impostos.py`
- `requirements.txt`

## Como rodar
1. `pip install -r requirements.txt`
2. Copie `.env.exemplo` para `.env` e preencha os caminhos.
3. Execute o script principal.

## Autora
Victória Pedrosa — Product Owner do Time de IA, automação de processos contábeis e fiscais.
