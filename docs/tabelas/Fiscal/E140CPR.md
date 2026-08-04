# E140CPR

## Descrição

Tabelas - Integrações - Detalhamento Venda Cartão Presente

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| NumCpr | String(020) | Não | Número do Cartão Presente |
| SeqHcp | Number(009,0) | Não | Sequencia de histórico de movimentos do Cartão Presente |
| NumTit | String(015) | Não | Número do título a receber |
| CodTpt | String(003) | Não | Código do tipo de título a receber |
| CodEqu | Number(003,0) | Não | Código do equipamento fiscal |
| CroEcf | Number(006,0) | Não | Cont. de Reinício de Operação do ECF |
| NumCoo | Number(009,0) | Não | Contador da Ordem de Operação que emitiu o recebimento na ECF |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv

---

## Índices

### E140CPRIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- NumCpr

### E140CPRIndice2

**Tipo:** Não unico

Campos:
- CodTpt

---

## Relacionamentos

### IR_E140CPR_007

**Tabela:** E002TPT

| Origem | Destino |
|--------|---------|
| CodTpt | CodTpt |

