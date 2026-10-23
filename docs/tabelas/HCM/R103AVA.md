# R103AVA

## Descrição

PSS - Avaliadores das Inspeções

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodPss | Number(003,0) | Não | Código do grupo de PSS |
| CodIns | Number(004,0) | Não | Número da Inspeção |
| TipCol | Number(001,0) | Não | Tipo do Avaliador |
| NumCad | Number(009,0) | Não | Cadastro do Avaliador |

---

## Chave Primária

- NumEmp
- CodPss
- CodIns
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R103AVA_002

**Tabela:** R103INS

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPss | CodPss |
| CodIns | CodIns |

