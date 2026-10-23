# R101ACO

## Descrição

Avaliação de Resultado - Objetivos - Acompanhamento

---

## Resumo

- Campos: 15
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CodCic | Number(003,0) | Não | Código do ciclo de avaliação |
| TipAva | Number(002,0) | Não | Sequência do tipo de avaliação |
| SeqAva | Number(002,0) | Não | Sequência da avaliação |
| IdeObj | Number(006,0) | Não | Identificação dos objetivos |
| DatAco | Date | Não | Data do Acompanhamento |
| NotAco | Number(014,2) | Sim | Resultado do Acompanhamento |
| PerAco | Number(014,2) | Sim | Percentual do Acompanhamento |
| DesRes | String(2000) | Sim | Descrição do resultado |
| EmpRes | Number(004,0) | Sim | Código da Empresa do responsável pelo registro do acompanhamento |
| TipRes | Number(001,0) | Sim | Tipo do colaborador responsável pelo registro do acompanhamento |
| CadRes | Number(009,0) | Sim | Código do Colaborador responsável pelo registro do acompanhamento |
| VisAvl | String(001) | Sim | Define se o acompanhamento é visível para o avaliado |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- TipAva
- SeqAva
- IdeObj
- DatAco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R101ACO_004

**Tabela:** R101CTA

| Origem | Destino |
|--------|---------|
| CodCic | CodCic |
| TipAva | TipAva |

### IR_R101ACO_006

**Tabela:** R101RES

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodCic | CodCic |
| TipAva | TipAva |
| SeqAva | SeqAva |
| IdeObj | IdeObj |

