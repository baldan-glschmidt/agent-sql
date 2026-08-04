# E140EMI

## Descrição

Vendas - Notas Fiscais de Saída - Itens - Dados do Empreendimento Imobiliário

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| SeqEmi | Number(003,0) | Não | Sequência do empreendimento imobiliário |
| IndVin | String(001) | Sim | Indicador de Venda Inicial de Lote ou Imóvel na Planta |
| DocIde | String(014) | Sim | CNPJ do Empreendimento Imobiliário |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIpv
- SeqEmi

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140EMI_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140EMI_004

**Tabela:** E140IPV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |
| SeqIpv | SeqIpv |

