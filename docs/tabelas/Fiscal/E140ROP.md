# E140ROP

## Descrição

Vendas - Relacionamento da nota fiscal de retorno de industrialização com as ordens de produção

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| CodOri | String(003) | Não | Código da origem do produto/serviço fabricado na OP |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodPro | String(014) | Sim | Código do Produto/Serviço |
| CodDer | String(007) | Sim | Código da derivação |
| CodEtg | Number(004,0) | Sim | Código do estágio de produção |
| SeqCmp | Number(004,0) | Sim | Sequência do componente utilizado |
| QtdRnf | Number(014,5) | Não | Quantidade retornada dos componentes pela nota fiscal de retorno de industrialização |

---

## Chave Primária

- IdeUni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140ROP_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

