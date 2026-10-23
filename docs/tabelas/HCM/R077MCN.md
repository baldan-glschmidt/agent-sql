# R077MCN

## Descrição

Resultado da Avaliação de Conhecimentos

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CmpAva | Date | Não | Competência da Avaliação |
| FamCnc | String(004) | Não | Código da Família de Conhecimentos |
| CodCnc | String(005) | Não | Código do Conhecimento |
| NotCnc | Number(005,2) | Sim | Nota Média atingida no Conhecimento |
| PerCnc | Number(005,2) | Sim | % atingido no Conhecimento |
| SeqHcn | Number(003,0) | Sim | Sequência do Histórico de Conhecimento gerado na Certificação |
| LotRes | Number(009,0) | Sim | Número do lote em que foi gerado o Resultado |
| CodCic | Number(003,0) | Sim | Código do ciclo de avaliação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpAva
- FamCnc
- CodCnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R077MCN_005

**Tabela:** R125CNC

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |
| CodCnc | CodCnc |

