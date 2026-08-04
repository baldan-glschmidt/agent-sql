# E140CPK

## Descrição

Vendas - Notas Fiscais de Saída - Componentes do Produto KIT

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Não | Sequência do item na nota fiscal de saída |
| SeqCpk | Number(003,0) | Não | Sequência do componente do produto kit |
| CodPro | String(014) | Não | Código do produto componente do produto kit |
| CodDer | String(007) | Sim | Código da derivação do produto componente do produto kit |
| QtdFat | Number(014,5) | Não | Quantidade faturada/baixada do estoque do componente do produto kit |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqIpv
- SeqCpk

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140CPK_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

