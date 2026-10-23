# R040ASD

## Descrição

Gozo do Prêmio Assiduidade

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| IniPer | Date | Não | Data Início do Período |
| IniAsd | Date | Não | Data Início do Prêmio Assiduidade |
| FimAsd | Date | Sim | Data do Fim do Prêmio Assiduidade |
| DiaAsd | Number(004,2) | Sim | Dias de Prêmio Assiduidade |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniPer
- IniAsd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R040ASD_003

**Tabela:** R040PER

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| IniPer | IniPer |

