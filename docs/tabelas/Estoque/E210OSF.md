# E210OSF

## Descrição

Estoques - Saldos físicos mensais - Observações

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| MesIni | Date | Não | Mês e ano inicial correspondente as informações |
| MesFin | Date | Não | Mês e ano final correspondente as informações |
| DatGer | Date | Sim | Data base da geração do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geraçao do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| OriSel | String(250) | Sim | Origens selecionadas para o processamento |
| FamSel | String(250) | Sim | Famílias selecionadas para o processamento |
| ProSel | String(250) | Sim | Produtos selecionados para o processamento |
| DerSel | String(250) | Sim | Derivações selecionadas para o processamento |
| DepSel | String(250) | Sim | Depósitos selecionados para o processamento |
| QtdSfe | Number(014,5) | Sim | Quantidade de registros inseridos no processamento |
| RegUlm | String(001) | Sim | Indicativo se o sistema deve inserir registros sem movimentações no mês |

---

## Chave Primária

- CodEmp
- CodFil
- MesIni
- MesFin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E210OSF_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E210OSF_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

