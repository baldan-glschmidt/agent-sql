# E140RAT

## Descrição

Vendas - Notas Fiscais de Saída - Rateios

---

## Resumo

- Campos: 26
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqRat | Number(004,0) | Não | Sequência do rateio do item de produto |
| DatBas | Date | Sim | Data base contábil e financeira |
| TnsPro | String(005) | Sim | Transação de produto |
| TnsSer | String(005) | Sim | Transação de serviço |
| SeqIpv | Number(003,0) | Sim | Sequência do item rateado |
| SeqIsv | Number(003,0) | Sim | Sequência do item de serviço |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| SomSub | Number(001,0) | Não | Somar ou subtrair o valor no plano financeiro/centro de custos |
| NumPrj | Number(008,0) | Sim | Número do projeto |
| CodFpj | Number(004,0) | Sim | Código da fase do projeto |
| CtaFin | Number(007,0) | Sim | Conta financeira reduzida |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |
| PerCta | Number(007,4) | Sim | Percentual rateado para a conta |
| VlrCta | Number(015,2) | Sim | Valor rateado para a conta |
| CodCcu | String(009) | Sim | Código do centro de custos |
| PerRat | Number(007,4) | Sim | Percentual rateado para o centro de custos |
| VlrRat | Number(015,2) | Sim | Valor rateado para o centro de custos |
| ObsRat | String(120) | Sim | Observação do rateio |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| TipOri | String(001) | Sim | Origem do Rateio |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140RAT_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

