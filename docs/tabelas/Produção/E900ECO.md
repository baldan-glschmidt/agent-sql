# E900ECO

## Descrição

O.P./O.S. - Apontamento Especificações Conformidade p/ Produto

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOri | String(003) | Não | Código da origem |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodPro | String(014) | Não | Código do Produto |
| CodDer | String(007) | Não | Derivação do produto |
| CodEct | String(014) | Não | Código da especificação técnica de conformidade do produto |
| VlrCe1 | Number(015,6) | Sim | Valor alvo atingido p/ conformidade do produto |
| VlrCe2 | Number(015,6) | Sim | Valor mínimo atingido p/ conformidade do produto |
| VlrCe3 | Number(015,6) | Sim | Valor máximo atingido p/ conformidade do produto |
| ObsEco | String(240) | Sim | Observações complementares |
| CodEtg | Number(004,0) | Sim | Código do Estágio de Produção da O.P./O.S. |
| SeqEoq | Number(005,0) | Sim | Sequência da movimentação da produção |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodPro
- CodDer
- CodEct

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E900ECO_002

**Tabela:** E900COP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |
| NumOrp | NumOrp |

### IR_E900ECO_003

**Tabela:** E075PRO

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |

### IR_E900ECO_005

**Tabela:** E094ECT

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodEct | CodEct |

