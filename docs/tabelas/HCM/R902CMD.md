# R902CMD

## Descrição

Comandos customizados para extração de dados do sistema

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CMDID | String(255) | Não | Identificador do comando |
| CMDTYP | Number(001,0) | Não | Tipo de Informação |
| CMDPER | Number(001,0) | Sim | Frequência execução de comando/configuração |
| REFDAY | Number(002,0) | Sim | Dia de referência de execução do comando. Frequência semanal: 1 (segunda-feira) a 7(domingo). Frequência mensal: número do dia. Se o valor for maior que o possível para o periodo (8 dia da semana, dia 31 em fevereiro) o maior valor possível será usado. |
| VALTHE | Date | Sim | Data de validade da teoria |
| TMEOUT | Number(009,0) | Não | Timeout de execução |
| COMAND | String(8000) | Não | Comando SQL para extração de dados |
| LSTEXE | Date | Sim | Última execução |
| FLAG | String(015) | Sim | Flag |

---

## Chave Primária

- CMDID

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
