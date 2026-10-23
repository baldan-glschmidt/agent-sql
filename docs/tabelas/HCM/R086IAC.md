# R086IAC

## Descrição

Investigação Ocorrência - Árvore de Causas

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipOco | Number(001,0) | Não | Tipo da Ocorrência (Acidente/Incidente) |
| CodInv | Number(006,0) | Não | Código da Investigação |
| SeqEve | Number(002,0) | Não | Sequência da Testemunha |
| NivEve | Number(002,0) | Sim | Nível do Evento |
| SeqPai | Number(002,0) | Sim | Sequência do Nodo Pai |
| PosArv | String(024) | Sim | Posição do Nodo na Árvore |
| DesEve | String(200) | Sim | Descrição do Evento |
| ComAtv | Number(001,0) | Sim | Componente da Atividade |

---

## Chave Primária

- NumEmp
- TipOco
- CodInv
- SeqEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R086IAC_002

**Tabela:** R086INV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipOco | TipOco |
| CodInv | CodInv |

