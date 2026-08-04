# E140PPA

## Descrição

Vendas - Nota Fiscal de Saída - Dados do CTe - Modal Aéreo - Produto Perigoso

---

## Resumo

- Campos: 15
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída (CT-e) |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída (CT-e) |
| SeqPpa | Number(004,0) | Não | Sequência dos registros de produto perigoso |
| CodOnu | String(004) | Sim | Número ONU/UN |
| TotPer | String(020) | Sim | Quantidade total de volumes contendo artigos perigosos |
| QtdPer | Number(015,4) | Sim | Quantidade total de artigos perigosos |
| MedPer | Number(001,0) | Sim | Unidade de medida |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqPpa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140PPA_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

