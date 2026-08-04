# E900EOF

## Descrição

O.P./O.S. - Movimentação Ferramentas/Equipamentos utilizados no apontamento

---

## Resumo

- Campos: 10
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOri | String(003) | Não | Código da origem |
| NumOrp | Number(009,0) | Não | Número da OP/OS |
| CodEtg | Number(004,0) | Não | Código do estágio de produção |
| SeqEoq | Number(005,0) | Não | Sequência da movimentação de OP/OS na produção |
| CodFrt | String(014) | Não | Código da ferramenta |
| DerFrt | String(007) | Não | Código da derivação da ferramenta |
| CodEqp | String(020) | Não | Código do equipamento ligado a ferramenta/série |
| TaxFrt | Number(008,2) | Sim | Taxa de utilização da ferramenta (padrão = 1) |
| UtiFrt | Number(009,0) | Sim | Quantidade/tempo total utilizado da ferramenta |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodEtg
- SeqEoq
- CodFrt
- DerFrt
- CodEqp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900EOF_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900EOF_003

**Tabela:** E093ETG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEtg | CodEtg |

### IR_E900EOF_004

**Tabela:** E900EOQ

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |
| CodEtg | CodEtg |
| SeqEoq | SeqEoq |

