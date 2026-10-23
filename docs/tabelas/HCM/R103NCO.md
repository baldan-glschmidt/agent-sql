# R103NCO

## Descrição

PSS - Inspeções - Não-conformidades

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodPss | Number(003,0) | Não | Código do grupo de PSS |
| CodIns | Number(004,0) | Não | Número da Inspeção |
| SeqNco | Number(003,0) | Não | Número sequencial da Não-conformidade |
| DesNco | String(200) | Sim | Descrição da Não-conformidade |
| IndCon | String(001) | Sim | Situação da Inspeção(S-Concluído/N-Não Concluído) |

---

## Chave Primária

- NumEmp
- CodPss
- CodIns
- SeqNco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R103NCO_002

**Tabela:** R103INS

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPss | CodPss |
| CodIns | CodIns |

