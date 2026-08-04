# E210TRA

## Descrição

Estoques - Valorização Transferências

---

## Resumo

- Campos: 27
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto transferido |
| CodDer | String(007) | Não | Código da Derivação do produto transferido |
| CodDep | String(010) | Não | Código do depósito transferido |
| DatMov | Date | Não | Data da movimentação do estoque |
| SeqMov | Number(006,0) | Não | Sequência de movimento na data de movimentação |
| FilFec | Number(005,0) | Sim | Código da filial |
| EmpNfv | Number(004,0) | Sim | Código da empresa da nota fiscal de saída |
| FilNfv | Number(005,0) | Sim | Código da filial da nota fiscal de saída |
| SnfNfv | String(003) | Sim | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Sim | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Sim | Sequência do item na nota fiscal de saída |
| PrmEst | Number(021,10) | Sim | Preço Médio do estoque total |
| ChvFec | String(050) | Sim | Chave Única do fechamento de estoques |
| DatIni | Date | Sim | Período inicial de validade para movimentações dos estoques |
| DatFin | Date | Sim | Período final de validade para movimentações dos estoques |
| CodLig | Number(009,0) | Sim | Código da ligação do movimento |
| FecAtu | String(001) | Sim | Fechamento ou Atualização de Estoques |
| DatGer | Date | Não | Data de geração do registro |
| CodFor | Number(009,0) | Sim | Código do fornecedor Nota fiscal de Compra |
| QtdMov | Number(014,5) | Sim | Quantidade do movimento |
| VlrMov | Number(015,2) | Sim | Valor do movimento |
| CodTns | String(005) | Não | Código da transação |
| EstEos | String(001) | Não | Entrada ou saída de estoque |
| NorCus | String(006) | Sim | Fechamento Normal ou Via Custos |
| HorGer | Number(005,0) | Sim | Hora da Geração do Registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E210TRAINDICE01

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro
- CodDer
- CodDep
- DatMov
- SeqMov

### E210TRAINDICE02

**Tipo:** Não unico

Campos:
- EmpNfv
- FilNfv
- SnfNfv
- NumNfv
- SeqIpv

---

## Relacionamentos

Nenhum relacionamento cadastrado.
