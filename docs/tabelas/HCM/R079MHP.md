# R079MHP

## Descrição

Resultado da Avaliação de Excelência

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CmpAva | Date | Não | Competência da Avaliação |
| CodHpe | String(004) | Não | Código da Habilidade Pessoal |
| NotMed | Number(005,2) | Sim | Nota Média atingida na Habilidade Pessoal |
| PerExc | Number(005,2) | Sim | % atingido na Habilidade Pessoal |
| LotRes | Number(009,0) | Sim | Número do lote em que foi gerado o Resultado |
| CodCic | Number(003,0) | Sim | Código do ciclo de avaliação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpAva
- CodHpe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R079MHP_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R079MHP_004

**Tabela:** R079HPE

| Origem | Destino |
|--------|---------|
| CodHpe | CodHpe |

