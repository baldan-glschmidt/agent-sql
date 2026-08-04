# E440RAT

## Descrição

Compras - Notas Fiscais de Entrada - Rateios

---

## Resumo

- Campos: 27
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodFor | Number(009,0) | Não | Código do fornecedor da nota fiscal de entrada |
| NumNfc | Number(009,0) | Não | Número da nota fiscal de entrada |
| CodSnf | String(003) | Não | Código da série da nota fiscal de entrada |
| SeqRat | Number(004,0) | Não | Sequência do rateio na nota fiscal de entrada |
| DatBas | Date | Sim | Data base contábil e financeira |
| TnsPro | String(005) | Sim | Código da transação de item de produto |
| TnsSer | String(005) | Sim | Código da transação de item de serviço |
| SeqIpc | Number(003,0) | Sim | Sequência do item de produto rateado |
| SeqIsc | Number(003,0) | Sim | Sequência do item de serviço rateado |
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
- CodFor
- NumNfc
- CodSnf
- SeqRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440RAT_004

**Tabela:** E440NFC

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodFor | CodFor |
| NumNfc | NumNfc |
| CodSnf | CodSnf |

